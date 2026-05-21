import os
from playwright.sync_api import sync_playwright


def extract_cad_info_all_and_limit():
    # 数量控制变量：在这里设定你要生成多少个产品到最终的数组代码中
    MAX_EXPORT_COUNT = 10

    target_url = "https://device.panasonic.cn/ac/c/dl_center/cad/index.jsp?c=search"

    with sync_playwright() as p:
        print("正在启动自动化浏览器...")
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print(f"正在访问目标网页:\n{target_url}")
        page.goto(target_url, wait_until="networkidle")

        print("正在自动执行分类筛选...")
        try:
            category_area = page.locator(".search_block").nth(1)

            category_area.locator("select").nth(0).select_option(label="传感器")
            print("  第 1 级: 已选择 [传感器]")
            page.wait_for_timeout(1000)

            category_area.locator("select").nth(1).select_option(label="接近传感器")
            print("  第 2 级: 已选择 [接近传感器]")
            page.wait_for_timeout(1000)

            category_area.locator("select").nth(2).select_option(label="接近传感器 GX-100")
            print("  第 3 级: 已选择 [接近传感器 GX-100]")

            print("正在点击检索按钮...")
            category_area.locator("input[type='image']").click()

            print("等待检索结果加载...")
            page.wait_for_selector(".titlecell", timeout=15000)
            print("列表加载完毕，开始解析底层 HTML...")

        except Exception as e:
            print(f"自动化选择过程中出现错误: {e}")
            browser.close()
            return

        # 获取完整的 HTML 源码备份
        html_content = page.content()
        current_folder = os.path.dirname(os.path.abspath(__file__))
        html_save_path = os.path.join(current_folder, "page_source.html")
        with open(html_save_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        # 核心抓取逻辑
        products = page.evaluate(r'''() => {
            let result = [];
            let rows = document.querySelectorAll("tr");

            rows.forEach(row => {
                let titleCell = row.querySelector(".titlecell");
                let aTag = row.querySelector("a[href*='f_cd=']");

                if (titleCell && aTag) {
                    let rawTitle = titleCell.innerText.trim();
                    let href = aTag.getAttribute("href");
                    let rawHtml = aTag.outerHTML;

                    let match = href.match(/\/([^\/]+)\.[a-zA-Z0-9_]+\?f_cd=(\d+)/i);

                    if (match) {
                        result.push({
                            name: match[1],
                            f_cd: match[2],
                            raw_title: rawTitle,
                            raw_html: rawHtml
                        });
                    }
                }
            });

            const uniqueResult = [];
            const seen = new Set();
            for (const item of result) {
                const key = item.name + '|' + item.f_cd;
                if (!seen.has(key)) {
                    seen.add(key);
                    uniqueResult.push(item);
                }
            }

            return uniqueResult;
        }''')

        # ---------------------------------------------------------
        # 第一阶段：输出所有抓取到的产品数据清单
        # ---------------------------------------------------------
        print(f"\n========================================================")
        print(f"提取完成！底层共解析到 {len(products)} 个独立产品。")
        print(f"========================================================")
        print("【所有产品数据完整清单】如下：")

        for idx, p in enumerate(products, start=1):
            # 在全览列表中也清理掉占位符，保持显示一致
            clean_name = p['name'].replace("□", "")
            print(f"  [{idx}] 网页显示: {p['raw_title'].ljust(15)} | name: {clean_name.ljust(15)} | f_cd: {p['f_cd']}")

        # ---------------------------------------------------------
        # 第二阶段：根据设定的数量，生成指定长度并清洗过字符串的 Python 数组
        # ---------------------------------------------------------
        limited_products = products[:MAX_EXPORT_COUNT]

        print(f"\n========================================================")
        print(f"正在根据 MAX_EXPORT_COUNT = {MAX_EXPORT_COUNT} 截取数据...")
        print(f"请直接复制以下代码，替换到下载程序的 product_list 变量中：\n")

        print("product_list = [")
        for p in limited_products:
            # 核心修改：生成最终数组时，剔除 name 字段中的特殊方块符号
            clean_name = p["name"].replace("□", "")
            print(
                f'    {{"name": "{clean_name}", "f_cd": "{p["f_cd"]}"}},  # {p["raw_title"]} (原始 HTML: {p["raw_html"]})')
        print("]")

        browser.close()


if __name__ == "__main__":
    extract_cad_info_all_and_limit()