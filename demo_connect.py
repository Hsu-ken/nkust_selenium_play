# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 17:20:46 2021

@author: idblab
"""

from time import sleep
from selenium import webdriver




driver = webdriver.Chrome()
driver.get("https://webap.nkust.edu.tw/nkust/")
# html = driver.page_source 目前抓取html

#轉到document上一層 https://stackoverflow.com/questions/38363643/python-selenium-get-inside-a-document/38363681
frame = driver.find_elements_by_tag_name('frame')[0]
driver.switch_to.frame(frame)
#login_form = driver.find_element_by_xpath("//td[@id='uid']")

#sleep(5)
#找到輸入框
account = driver.find_element_by_name("frm1")
account = driver.find_element_by_name("uid")
password = driver.find_element_by_name("pwd")
#element = driver.find_element("id", "input")
account.clear()
password.clear()
#輸入內容
print("請輸入帳號:")
account_i=input()
print("請輸入密碼:")
password_i=input()

account.send_keys(account_i);
password.send_keys(password_i);
#提交表單
sub = driver.find_element_by_name('chk').submit()


frame = driver.find_elements_by_tag_name('frame')[1]
button = driver.find_elements_by_tag_name('frame')[2]

driver.switch_to.frame(frame)
html = driver.page_source

search = driver.find_element_by_id('fspan1')
search.click()

print("個人資料輸入1,學期成績輸入2,")
chose_i=input()
if(chose_i == "1"):
    driver.execute_script("of_display('AG003')")
if(chose_i == "2"):

    driver.execute_script("of_display('AG008')")
    #切回主文黨
    driver.switch_to.default_content()
    button = driver.find_elements_by_tag_name('frame')[2]
    driver.switch_to.frame(button)
    driver.find_element_by_css_selector('tr td input.button').click()

   # driver.execute_script("switch_yms()")

#要先click打開 才有學雜費收據列印
# <span id="fspan1" onclick="work2(document.getElementById('fimg1'),document.getElementById('ffod1'))">查詢</span>


#aa=driver.find_element_by_css_selector('tbody tr td table tbody tr td table tbody tr td table tbody td.ob_td div').click*()
#content = driver.find_element_by_css_selector('p.content')

#account = driver.find_element_by_link_text("學雜費繳費收據列印").click