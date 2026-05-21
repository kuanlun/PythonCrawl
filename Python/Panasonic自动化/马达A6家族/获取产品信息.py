from playwright.sync_api import sync_playwright


def automate_panasonic_search():
    with sync_playwright() as p:
        # 启动浏览器 (headless=False 可观察自动化过程)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://device.panasonic.cn/ac/c/dl_center/cad/index.jsp?c=search")

        category_area = page.locator(".search_block").nth(1)
        # 1. 选择“电机” (假设第一个下拉框 name 为 medium)
        category_area.locator("select").nth(0).select_option(label="电机")
        print("  第 1 级: 已选择 [电机]")
        page.wait_for_timeout(1000)

        category_area.locator("select").nth(1).select_option(label="AC伺服电机")
        print("  第 2 级: 已选择 [AC伺服电机]")
        page.wait_for_timeout(1000)

        category_area.locator("select").nth(2).select_option(label="MINAS A6 家族 伺服电机")
        print("  第 3 级: 已选择 [MINAS A6 家族 伺服电机]")

        #print("正在点击检索按钮...")
        #category_area.locator("input[type='image']").click()

        print("等待检索结果加载...")
        page.wait_for_selector(".titlecell", timeout=15000)
        print("列表加载完毕，开始解析底层 HTML...")

        # 5. 等待表格加载
        page.wait_for_selector("table[summary='CAD列表']", timeout=10000)

        # 6. 提取产品型号 (titlecell)
        product_names = page.evaluate('''() => {
            return Array.from(document.querySelectorAll('td.titlecell')).map(td => td.innerText.trim());
        }''')

        print(f"提取到产品型号: {product_names}")
        browser.close()


if __name__ == "__main__":
    automate_panasonic_search()