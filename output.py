from selenium import webdriver
import requests
import urllib.request
import time
import re
from bs4 import BeautifulSoup
import lxml.html
import openpyxl
import pyautogui as pg
import os

wb = openpyxl.load_workbook("まとめ0803.xlsx")
ws = wb["Sheet1"]
name_list = []
url_list = []
for name in list(ws.columns)[0]:
    name_list.append(name.value)
for url in list(ws.columns)[1]:
    url_list.append(url.value)
i = 0


#ログイン
driver = webdriver.Chrome(executable_path="C:\\Users\\tisk0\\PycharmProjects\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://crowdworks.jp/login?back=1')
id_element = driver.find_element_by_css_selector('#username')
id_element.send_keys('tisk0711ngm@gmail.com')
password_element = driver.find_element_by_css_selector('#password')
password_element.send_keys('enwork777')
button_element = driver.find_element_by_css_selector('#Content > div > div > div.column.login.cw-well > form > p.submit > input.cw-button.cw-button_highlight')
button_element.click()
time.sleep(2)
driver.get('https://crowdworks.jp/public/jobs/6624136')

#作業履歴へ
button_element2 = driver.find_element_by_css_selector('#job_offer_detail > div > div.cw-column.sidebar > div > div > div.type_caption > div > p > a')
button_element2.click()

#作業を開始する
button_element2_1 = driver.find_element_by_css_selector('#new_task_work > input.cw-button.cw-button_highlight.cw-button_lg')
button_element2_1.click()

for name1 in name_list:
    #print(name1)
    #print(url_list[i])

    #フォーム開始
    #チャンネル名
    name_element = driver.find_element_by_css_selector('#task_work_contents_attributes_0_content_value')
    name_element.clear()
    name_element.send_keys(name1)

    #twitter
    #driver.execute_script("window.scrollTo(0, 1000);")
    button_element3 = driver.find_element_by_css_selector('#task_content_5983936_columns_0')
    #button_element3.click()
    driver.execute_script("arguments[0].click();", button_element3)

    url_element = driver.find_element_by_css_selector('#task_work_contents_attributes_2_content_value')
    url_element.send_keys(url_list[i])

    #はい１
    #driver.execute_script("window.scrollTo(0, 200);")
    button_element4 = driver.find_element_by_css_selector('#task_content_5983938_columns_0')
    #button_element4.click()
    driver.execute_script("arguments[0].click();", button_element4)

    #はい２
    #driver.execute_script("window.scrollTo(0, 200);")
    button_element5 = driver.find_element_by_css_selector('#task_content_5983939_columns_0')
    #button_element5.click()
    driver.execute_script("arguments[0].click();", button_element5)

    #time.sleep(30)

    #作業を完了する
    #button_element6 = driver.find_element_by_css_selector('#edit_task_work_53312408 > div.task_submit > input')
    button_element6 = driver.find_element_by_css_selector('.cw-button.cw-button_highlight.cw-button_lg.disable-at-expired.done')
    button_element6.click()
    #driver.execute_script("arguments[0].click();", button_element6)

    #ポップアップ
    button_element6_1 = driver.find_element_by_css_selector('#Content > div.cw-global_row > div.cw-modal_dialog.complete-modal > div > div.cw-modal_footer > button.cw-button.cw-button_highlight.modal-done')
    button_element6_1.click()

    #続けて作業する
    button_element7 = driver.find_element_by_css_selector('#new_task_work > input.cw-button.cw-button_highlight.large')
    #button_element7 = driver.find_element_by_class_name('cw-button cw-button_highlight cw-button_lg disable-at-expired done')
    button_element7.click()
    time.sleep(3)
    i = i + 1