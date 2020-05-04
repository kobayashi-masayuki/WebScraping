from selenium import webdriver
from selenium.webdriver.common.by import By
from unicodedata import category
import requests
from line_notify_bot import LINENotifyBot

bot = LINENotifyBot(access_token='yBjdrdNMMJpuIeWW8rZI7PJPJu6oO1Qp0TE2UEaPDIv')

url = "https://notify-api.line.me/api/notify"
access_token = 'yBjdrdNMMJpuIeWW8rZI7PJPJu6oO1Qp0TE2UEaPDIv'
headers = {'Authorization': 'Bearer ' + access_token}

options = webdriver.ChromeOptions()

options.add_argument('--headless')
driver = webdriver.Chrome(options=options) 

driver.get('https://www.apple.com/jp/shop/refurbished/mac/2019') 

r = driver.find_elements_by_class_name('as-producttile-tilelink')
len = len(r)
list =[]
for i in range(len):
    r = driver.find_elements_by_class_name('as-producttile-tilelink')[i].get_attribute('data-display-name')
    list.append(r)
    if "15.4インチMacBook Pro 2.2GHz" in r and "スペースグレイ" in r:
        detail = driver.find_elements_by_class_name('as-producttile-tilelink')[i].get_attribute("href")
        driver.get(detail)
        if driver.find_elements_by_class_name('ac-gn-bagview-nav-link ac-gn-bagview-nav-link-signIn'):
            login = driver.find_element_by_class_name('ac-gn-bagview-nav-link ac-gn-bagview-nav-link-signIn').get_attribute("href")
            driver.get('login')
            driver.find_element_by_id("loginHome.customerLogin.appleId-label").send_keys("hoge@gmail.com")
            driver.find_element_by_id("loginHome.customerLogin.password-label").send_keys("hoge")
            driver.find_element_by_id("signin-button-submit").click()
        driver.find_element_by_name("add-to-cart").click()
        bot.send(
            message='入荷有り'+r
        )
        driver.get('https://www.apple.com/jp/shop/refurbished/mac/2019') 
driver.quit()

print(list)
import pandas as pd
df = pd.Series(list)
df.to_csv("Item.csv", encoding='utf_8_sig')