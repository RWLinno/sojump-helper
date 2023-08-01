from selenium import webdriver
from selenium.webdriver.common.by import By
import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth 
import random
import selenium
import time

def click_button_by_class(browser, class_name):
    try:
        # 使用 class 名称找到按钮元素并点击
        button = browser.find_element(By.CLASS_NAME, class_name)
        button.click()
        time.sleep(2)
    except Exception as e:
        print(f"出现错误：{str(e)}")

def auto_fillout(url):    
    driver_path = "chromedriver.exe"

    # 可以避免智能验证码的选项
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)

    # 创建 Chrome 浏览器对象
    browser = webdriver.Chrome(options=option)
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
    browser.get(url)
    time.sleep(2)

    # 先遍历
    for num in range(30):
        answerxyz = browser.find_elements(By.CSS_SELECTOR,'#q'+str(num))
        for answer in answerxyz:
            try:
                answer.click()
                ans = str(random.randint(1010998244353, 101210102020304567891))
                answer.send_keys(ans)
                #time.sleep(0.5)
            except Exception as e:
                print(f'error q{num}!!!')

    # 选择题
    answerxx = browser.find_elements(By.CSS_SELECTOR,'.ui-radio')
    for answer in answerxx:
        try:
            answer.click()
            #time.sleep(0.5)
        except Exception as e:
            print("error clickx!!!")

    answeryy = browser.find_elements(By.CSS_SELECTOR,'.column1')
    for answer in answeryy:
        try:
            answer.click()
            #time.sleep(0.5)
        except Exception as e:
            print("error clickx!!!")
    answerdd = browser.find_elements(By.CSS_SELECTOR,'.ui-checkbox')
    for answer in answerdd:
        try:
            answer.click()
            #time.sleep(0.5)
        except Exception as e:
            print("error clickd!!!")

    #填空题部分
    answerzz = browser.find_elements(By.CSS_SELECTOR,'textarea')
    for answer in answerzz:
        try:
            ans = str(random.randint(1010998244353, 101210102020304567891))
            print(ans)
            answer.send_keys(ans)
        except Exception as e:
            print("error fillout!!!")

    # 提交
    click_button_by_class(browser, 'voteDiv')
    time.sleep(2)
    check = browser.find_elements(By.CLASS_NAME,'.formfield.formfieldComplete')
    browser.quit()
    for any in check:
        return True
    return False
