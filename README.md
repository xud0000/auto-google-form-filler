# Auto Google Form Filler

> 🔧 自動填寫 Google 表單的 Python 工具，支援單選、複選、隨機選項與多份提交。適用於模擬測試、自動化實驗或資料填答練習。

---

## 🎯 專案目的

本工具協助使用者模擬大量問卷填寫，用於教學、測試或研究用途。  
使用 `Python` 撰寫，搭配 `Selenium` 與 `multiprocessing`，提供基本數量控制，支援自動填答、隨機選項與高效率提交。

---

## 🧩 功能特色

- ✅ 自動辨識題目型態（單選 / 複選）
- ✅ 隨機選項填答
- ✅ 支援多份填寫與自訂次數
- ✅ 多執行緒同時填寫，提高效率
- ✅ 可啟用 Headless 模式（背景執行）
- ✅ 已提供 Windows `.exe` 執行檔，無須安裝 Python

---

## 📥 Windows EXE 下載

👉 [點我前往 Releases 下載 EXE](https://github.com/xud0000/auto-google-form-filler/releases)

### 🔹 執行方式（免安裝 Python）：

1. 下載檔案 `auto_form_windows_x64_v1.0.0.exe`
2. 直接雙擊執行（程式將自動打開 Google 表單並填寫）
3. 如出現 Windows 安全警告，請點「更多資訊」→「仍要執行」

---

## 🛠 原始碼使用方式

若需自行修改表單網址、填寫邏輯等，可直接運行 Python 原始碼：

```bash
pip install -r requirements.txt
python auto_form.py
```

## 🔧 執行環境需求

- 作業系統：Windows / macOS / Linux
- Python：3.7 或以上版本
- 瀏覽器：Google Chrome
- 驅動程式：對應版本的 ChromeDriver

## 📜 授權 License

本專案以 [MIT License](https://opensource.org/licenses/MIT) 授權開源。
