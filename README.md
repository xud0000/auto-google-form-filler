# Auto Google Form Filler

> 🔧 自動填寫 Google 表單的 Python 工具，支援單選、複選、隨機選項與多份提交。適用於模擬測試與學術自動化實驗。

---

## 🎯 專案目的

本工具幫助學生進行問卷資料收集模擬、填答行為分析與自動化腳本練習。以 `Python` 搭配 `Selenium` 與 `multiprocessing` 撰寫，具備簡單的互動介面與可調參數設計。

---

## 🧩 功能特色

- ✅ 自動判別題目型態（單選/複選）
- ✅ 支援隨機選項選擇
- ✅ 支援多份填寫（可指定份數）
- ✅ 支援多執行緒並行處理（提升填表效率）
- ✅ 可切換是否顯示瀏覽器（headless 模式）

---

## 🔧 環境需求

- Python 3.7+
- Chrome 瀏覽器
- ChromeDriver（需與 Chrome 版本相符）
- pip 套件管理工具

---

## 📦 安裝方式

1. 安裝必要套件：
   ```bash
   pip install -r requirements.txt
