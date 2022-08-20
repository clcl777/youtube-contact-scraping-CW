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

wb = openpyxl.load_workbook("切り抜き.xlsx")
ws = wb.worksheets[0]
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

driver.get('https://www.lancers.jp/user/login?ref=header_menu')
time.sleep(1)
id_element = driver.find_element_by_id('UserEmail')
id_element.send_keys('tisk0711ngm@gmail.com')
password_element = driver.find_element_by_id('UserPassword')
password_element.send_keys('enla7777')
button_element = driver.find_element_by_id('form_submit')
button_element.click()
time.sleep(3)
driver.get('https://www.lancers.jp/work/detail/3751893')

#作業開始
start_element = driver.find_element_by_css_selector('#workDescriptionLink > div > div > div.grid__unit.grid__unit--3.work_detail_righter > div.show_popup_button > a')
start_element.click()

#同意して始める
start2_element = driver.find_element_by_css_selector('#form_end')
start2_element.click()

#作業を始める
start3_element = driver.find_element_by_css_selector('body > div.l-wrapper.l-wrapper--login.default-layout > div.inner > div > div.c-button-group.c-button-group--center > input')
start3_element.click()

#チャンネル名入力
id_element = driver.find_element_by_css_selector('#TaskCreateForm > section:nth-child(3) > p:nth-child(2) > textarea')
id_element.send_keys('')