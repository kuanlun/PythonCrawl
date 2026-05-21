import os
from playwright.sync_api import sync_playwright


def playwright_smart_download():
    # --- 1. 配置中心 ---
    # 只需要填入 name 和 f_cd，程序会自动判断如何拼接后缀
    product_list = [
        {"name": "gx-108mk", "f_cd": "4186218"},  # GX-100系列：会自动处理成 gx-108mk.step.STEP
        {"name": "gx-208mlk", "f_cd": "4238343"},  # GX-200系列：会自动处理成 gx-208mlk.STEP
    ]

    current_folder = os.path.dirname(os.path.abspath(__file__))
    download_dir = os.path.join(current_folder, "downloaded_cad")
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    cookies_list = [
        {"name": "JSESSIONID", "value": "185D996E6CEB6101688AB47848DF10F1", "domain": "device.panasonic.cn",
         "path": "/ac"},
        {"name": "acw_tc", "value": "2f61f27a17792615617301726eac93f25fa5cf248e03d13232d46c83ad7e2c",
         "domain": "device.panasonic.cn", "path": "/"}
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            channel="chrome",
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context()
        context.add_cookies(cookies_list)
        page = context.new_page()
        page.goto("https://device.panasonic.cn/ac/c/index.jsp", wait_until="networkidle")

        for index, product in enumerate(product_list, start=1):
            name = product["name"]
            f_cd = product["f_cd"]

            # --- 核心逻辑：智能拼接 ---
            # 如果 name 不含 .step，则拼成 name.step.STEP，否则直接拼 name.STEP
            if "step" not in name.lower():
                full_name = f"{name}.step"
                url = f"https://device.panasonic.cn/ac/c_download/fasys/sensor/proximity/cad/3d_step/{full_name}.STEP?f_cd={f_cd}&via=ok"
            else:
                url = f"https://device.panasonic.cn/ac/c_download/fasys/sensor/proximity/cad/3d_step/{name}.STEP?f_cd={f_cd}&via=ok"

            # 文件保存名
            save_path = os.path.join(download_dir, f"{name}.STEP")

            print(f"\n[{index}/{len(product_list)}] 正在下载: {name} ...")
            print(f"  URL: {url}")

            try:
                response = context.request.get(url, timeout=30000)
                if response.status == 200:
                    with open(save_path, "wb") as f:
                        f.write(response.body())
                    print(f"  [成功] 已保存至: {save_path}")
                else:
                    print(f"  [错误] 状态码: {response.status}")
            except Exception as e:
                print(f"  [异常] {e}")

        browser.close()


if __name__ == "__main__":
    playwright_smart_download()