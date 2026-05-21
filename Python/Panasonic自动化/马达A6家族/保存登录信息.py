from playwright.sync_api import sync_playwright


def save_session():
    with sync_playwright() as p:
        print("🚀 正在啟動錄製瀏覽器...")
        # 這裡不加任何 Cookie，完全乾淨地啟動
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 打開登入頁面或主頁
        page.goto("https://device.panasonic.cn/ac/c/index.jsp")

        print("\n========================================================")
        print("📢 請在彈出的瀏覽器中【手動完成登入】。")
        print("📢 登入成功並看到你的個人帳號後，回到 PyCharm 控制台。")
        print("========================================================")

        # 卡住程序，等你手動登入
        input("👉 登入成功後，請在 PyCharm 控制台按下【回車鍵 (Enter)】來保存狀態...")

        # 🎯 核心：Playwright 會把當前所有的 Cookie、Session、安全標記打包存進這個檔案
        context.storage_state(path="panasonic_auth.json")
        print("🎉 身分狀態已完美保存到 panasonic_auth.json 檔案中！")

        browser.close()


if __name__ == "__main__":
    save_session()