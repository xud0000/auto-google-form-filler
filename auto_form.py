import random
import time
from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"
]

def fill_form(index, url, total_q, opt_counts, show_window):
    chrome_opts = Options()
    chrome_opts.add_argument("--incognito")
    chrome_opts.add_argument("--disable-logging")
    chrome_opts.add_argument("--log-level=3")
    chrome_opts.add_argument(f"user-agent={random.choice(USER_AGENTS)}")
    if not show_window:
        chrome_opts.add_argument("--headless")

    try:
        driver = webdriver.Chrome(options=chrome_opts)
        wait = WebDriverWait(driver, 6)
        driver.get(url)

        question_blocks = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-params]")))

        for i in range(total_q):
            if i >= len(question_blocks):
                print(f"[{index}] ❌ 題目區塊不足（第{i+1}題）")
                break
            block = question_blocks[i]
            try:
                checks = block.find_elements(By.CSS_SELECTOR, "div[role='checkbox']")
                if len(checks) == opt_counts[i]:
                    pick_num = random.randint(1, opt_counts[i])
                    picks = random.sample(checks, pick_num)
                    for c in picks:
                        driver.execute_script("arguments[0].click();", c)
                    print(f"[{index}] ✅ 第{i+1}題（複選，{pick_num}/{opt_counts[i]}）")
                    continue

                radios = block.find_elements(By.CSS_SELECTOR, "div[role='radio']")
                if len(radios) == opt_counts[i]:
                    ans = random.choice(radios)
                    driver.execute_script("arguments[0].click();", ans)
                    print(f"[{index}] ✅ 第{i+1}題（單選）")
                    continue

                print(f"[{index}] ⚠️ 第{i+1}題格式不符或選項數量不同（表單實際選項數={max(len(radios),len(checks))}，你輸入={opt_counts[i]}）")
            except Exception as err:
                print(f"[{index}] ⚠️ 第{i+1}題錯誤：{err}")

        submit_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[role='button']")))
        found = False
        for b in submit_buttons:
            if "提交" in b.text or "Submit" in b.text:
                driver.execute_script("arguments[0].click();", b)
                found = True
                break
        if found:
            print(f"[{index}] ✅ 表單成功送出")
        else:
            print(f"[{index}] ❌ 找不到提交按鈕")
        if show_window:
            print(f"[{index}] 檢查視窗")
            time.sleep(3)
    except Exception as e:
        print(f"[{index}] ⚠️ 發生錯誤：{e}")
    finally:
        driver.quit()

def fill_forms(url, total_q, opt_counts, total_forms, concurrent):
    processes = []
    for i in range(total_forms):
        show_window = (i % concurrent == 0)
        p = Process(target=fill_form, args=(i+1, url, total_q, opt_counts, show_window))
        processes.append(p)
        p.start()
        if (i + 1) % concurrent == 0:
            for proc in processes:
                proc.join()
            processes = []
    for proc in processes:
        proc.join()

if __name__ == '__main__':
    form_url = input("輸入Google表單連結：")
    total_q = int(input("輸入題目總數："))
    opt_counts_str = input("輸入每題選項數量（用空白分隔，例如4 4 4 5 2）：")
    opt_counts = [int(x) for x in opt_counts_str.strip().split()]
    if len(opt_counts) != total_q:
        print("❌ 題目數與選項數不符")
        exit(1)
    total_forms = int(input("要填寫幾份："))
    concurrent = int(input("同時填寫份數（例如10）："))
    fill_forms(form_url, total_q, opt_counts, total_forms, concurrent)
