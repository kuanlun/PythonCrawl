import os
from playwright.sync_api import sync_playwright


def playwright_api_download():
    # 1. 你的产品清单
    product_list = [
        {"name": "gx-108mk", "f_cd": "4186216"},
        # GX-108MK□ (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/gx-108mk.dxf?f_cd=4186216" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
        {"name": "gx-108mlk", "f_cd": "4186248"},
        # GX-108MLK□ (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/gx-108mlk.dxf?f_cd=4186248" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
        {"name": "gx-108ml", "f_cd": "4186232"},
        # GX-108ML□ (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/gx-108ml.dxf?f_cd=4186232" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
        {"name": "gx-108m", "f_cd": "4183115"},
        # GX-108M□ (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/gx-108m.dxf?f_cd=4183115" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
        {"name": "gx-112mk", "f_cd": "4186220"},
        # GX-112MK□ (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/gx-112mk.dxf?f_cd=4186220" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
        {"name": "gx-112mlk", "f_cd": "4186252"},
        # GX-112MLK□ (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/gx-112mlk.dxf?f_cd=4186252" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
        {"name": "gx-112ml", "f_cd": "4186236"},
        # GX-112ML□ (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/gx-112ml.dxf?f_cd=4186236" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
        {"name": "gx-112m", "f_cd": "4183119"},
        # GX-112M□ (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/gx-112m.DXF?f_cd=4183119" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
        {"name": "gx-118mk", "f_cd": "4186224"},
        # GX-118MK□ (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/gx-118mk.dxf?f_cd=4186224" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
        {"name": "gx-118mlk", "f_cd": "4186256"},
        # GX-118MLK□ (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/gx-118mlk.dxf?f_cd=4186256" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
    ]

    current_folder = os.path.dirname(os.path.abspath(__file__))
    download_dir = os.path.join(current_folder, "downloaded_cad")
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # 2. 填入你最新的 Cookie（如果过期了，请换成最新的 JSESSIONID 和 acw_tc）
    cookies_list = [
        {"name": "JSESSIONID", "value": "185D996E6CEB6101688AB47848DF10F1", "domain": "device.panasonic.cn",
         "path": "/ac"},
        {"name": "acw_tc", "value": "2f61f27a17792615617301726eac93f25fa5cf248e03d13232d46c83ad7e2c",
         "domain": "device.panasonic.cn", "path": "/"}
    ]

    with sync_playwright() as p:
        print("🚀 启动 Playwright 底层网络直连模式 (无视 Chrome 下载拦截)...")

        browser = p.chromium.launch(
            headless=False,
            channel="chrome",
            args=["--disable-blink-features=AutomationControlled"]
        )

        context = browser.new_context()
        context.add_cookies(cookies_list)

        # 3. 先访问一次主页，让服务器信任我们的 Cookie 和 IP 环境
        print("🌐 正在初始化安全网络环境...")
        page = context.new_page()
        page.goto("https://device.panasonic.cn/ac/c/index.jsp", wait_until="networkidle")

        for index, product in enumerate(product_list, start=1):
            name = product["name"]
            f_cd = product["f_cd"]

            # 使用包含 &via=ok 的极速下载直链
            url = f"https://device.panasonic.cn/ac/c_download/fasys/sensor/proximity/cad/3d_step/{name}.step.STEP?f_cd={f_cd}&via=ok"
            #       https://device.panasonic.cn/ac/c_download/fasys/sensor/proximity/cad/3d_step/gx-108mk.step.STEP?f_cd=4186218
            save_path = os.path.join(download_dir, f"{name}.STEP")

            print(f"\n[{index}/{len(product_list)}] 正在后台强行抽取文件流: {name}.STEP ...")

            try:
                # 📢 终极杀招：使用 Playwright 的浏览器原生 API 直接发 GET 请求
                # 这完全绕过了浏览器的 UI 下载器，直接把数据存在内存里
                response = context.request.get(url, timeout=30000)

                if response.status == 200:
                    # 检查是不是被踢回了网页（Cookie失效）
                    content_type = response.headers.get("content-type", "")
                    if "text/html" in content_type:
                        print("❌ 失败：服务器返回了网页代码。原因：Cookie可能已过期，请重新提取最新的 Cookie。")
                        continue

                    # 将提取到的二进制文件数据，用 Python 原生方法强行写入硬盘
                    body_data = response.body()
                    with open(save_path, "wb") as f:
                        f.write(body_data)

                    # 物理层检验文件
                    if os.path.exists(save_path):
                        file_size = os.path.getsize(save_path)
                        if file_size > 0:
                            print(f"✅ 下载成功！大小: {file_size / 1024:.2f} KB | 路径: {save_path}")
                        else:
                            print("⚠️ 警告：获取到的是 0 KB 空壳文件，已被自动删除。")
                            os.remove(save_path)
                    else:
                        print("❌ 写入硬盘失败，请检查 C 盘或项目文件夹是否有读写权限。")
                else:
                    print(f"❌ 请求失败，服务器返回状态码: {response.status}")

            except Exception as e:
                print(f"❌ 抽取数据环节出现异常: {e}")

        print("\n========================================================")
        print("🎉 批量拉取任务执行完毕！")
        input("按 [回车键 (Enter)] 退出程序...")

        browser.close()


if __name__ == "__main__":
    playwright_api_download()