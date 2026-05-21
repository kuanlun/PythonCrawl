import os
from playwright.sync_api import sync_playwright


def playwright_api_download():
    # 1. 你的产品清单
    product_list = [
        {"name": "cn-23a-cc2", "f_cd": "4238499"},
        # CN-23A-CC2 (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/cn-23a-cc2.dxf?f_cd=4238499" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
        {"name": "cn-23al-cc2", "f_cd": "4238507"},
        # CN-23AL-CC2 (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/cn-23al-cc2.dxf?f_cd=4238507" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
        {"name": "cn-24-cc2", "f_cd": "4238515"},
        # CN-24-CC2 (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/cn-24-cc2.dxf?f_cd=4238515" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
        {"name": "cn-24l-cc2", "f_cd": "4238523"},
        # CN-24L-CC2 (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/cn-24l-cc2.dxf?f_cd=4238523" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
        {"name": "gx-204sk", "f_cd": "4238475"},
        # GX-204SK□ (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/gx-204sk.dxf?f_cd=4238475" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
        {"name": "gx-205mk", "f_cd": "4238491"},
        # GX-205MK□ (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/gx-205mk.dxf?f_cd=4238491" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
        {"name": "gx-205sk", "f_cd": "4238483"},
        # GX-205SK□ (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/gx-205sk.dxf?f_cd=4238483" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
        {"name": "gx-208mk", "f_cd": "4238335"},
        # GX-208MK□ (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/gx-208mk.dxf?f_cd=4238335" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
        {"name": "gx-208mk-z", "f_cd": "4238411"},
        # GX-208MK□-Z (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/gx-208mk-z.dxf?f_cd=4238411" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
        {"name": "gx-208mlk", "f_cd": "4238343"},
        # GX-208MLK□ (原始 HTML: <a href="/ac/c_download/fasys/sensor/proximity/cad/2d_dxf/gx-208mlk.dxf?f_cd=4238343" target="mewdownload"><img src="/ac/c/dl_center/images/cad/dl_button_2d_dxf.png" alt="2D-DXF" width="70" height="20"></a>)
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
            url = f"https://device.panasonic.cn/ac/c_download/fasys/sensor/proximity/cad/3d_step/{name}.STEP?f_cd={f_cd}&via=ok"
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