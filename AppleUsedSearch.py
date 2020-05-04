from selenium import webdriver
from selenium.webdriver.common.by import By
from unicodedata import category

options = webdriver.ChromeOptions()

#options.add_argument('--user-data-dir=C:\\Users\\J100046079\\AppData\\Local\\Google\\Chrome\\User Python Data')
#options.add_argument('--headless')
driver = webdriver.Chrome(options=options)  # 今は chrome_options= ではなく options=

driver.get('https://www.apple.com/jp/shop/refurbished/mac/2019') 
'''
r = driver.find_elements_by_xpath("//*[@id='refurbished-category-grid']/div/div[3]/div[2]/div[2]/ul//h3/a")
len = len(r)
for i in range(len):
    r = driver.find_elements_by_xpath("//*[@id='refurbished-category-grid']/div/div[3]/div[2]/div[2]/ul//h3/a")[i].get_attribute('data-display-name')
#targetElement = driver.find_element_by_class_name("data-display-name")
'''
r = driver.find_elements_by_class_name('as-producttile-tilelink')
len = len(r)
list =[]
for i in range(len):
    r = driver.find_elements_by_class_name('as-producttile-tilelink')[i].get_attribute('data-display-name')
#targetElement = driver.find_element_by_class_name("data-display-name")
    #print(r)
    if "Intel Core i7" in r and "スペースグレイ" in r:
        r = r+" This is Target"
        detail = driver.find_elements_by_class_name('as-producttile-tilelink')[i].get_attribute("href")
        driver.get(detail)
        if driver.find_elements_by_class_name('ac-gn-bagview-nav-link ac-gn-bagview-nav-link-signIn'):
            login = driver.find_element_by_class_name('ac-gn-bagview-nav-link ac-gn-bagview-nav-link-signIn').get_attribute("href")
            driver.get('login')
            driver.find_element_by_id("loginHome.customerLogin.appleId-label").send_keys("snowbirdway@gmail.com")
            driver.find_element_by_id("loginHome.customerLogin.password-label").send_keys("Gapgap33")
            driver.find_element_by_id("signin-button-submit").click()
        driver.find_element_by_name("add-to-cart").click()
    driver.get('https://www.apple.com/jp/shop/refurbished/mac/2019') 
print(list)
import pandas as pd
df = pd.Series(list)
df.to_csv("Item.csv")


driver.quit()
'''
username = "kobayashi.masayuki2@nidec.com"
password = "J1000462"

driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys(username) 
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("Login").submit()


for i in range(5):
    base_url ='https://gp01.oc.nidec.com/group/ncj/contactbook?p_p_id=com_nidec_gp_ic_contactbook_portlet_GpContactBookPortlet_INSTANCE_YPPGALghrYRO&_com_nidec_gp_ic_contactbook_portlet_GpContactBookPortlet_INSTANCE_YPPGALghrYRO_workplace=%E6%BB%8B%E8%B3%80&_com_nidec_gp_ic_contactbook_portlet_GpContactBookPortlet_INSTANCE_YPPGALghrYRO_delta=200'
    page_num = i + 1
    page = '&_com_nidec_gp_ic_contactbook_portlet_GpContactBookPortlet_INSTANCE_YPPGALghrYRO_cur=' + str(page_num)
    driver.get(base_url+page)
    targetElement = driver.find_element_by_class_name("contactbook-search-container")
    r = driver.find_element_by_class_name('contactbook-search-container')
    #print(r.text)

    from bs4 import BeautifulSoup
    import urllib.request

    #driver.quit()

    #htmlソース。encoding='cp932'は文字化け
    html = driver.page_source
    import pandas as pd
    lst = pd.read_html(html)[0]
    lst.to_csv('pd'+str(page_num)+'.csv', encoding='utf-8_sig', index=False)
    
    with open('hoge'+str(page_num)+'.txt', 'w', encoding='utf-8',errors='replace') as f:
        f.write(html)
    '''