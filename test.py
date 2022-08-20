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

wb = openpyxl.load_workbook("完成.xlsx")
ws = wb["Sheet"]
name_list = []
url_list = []

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

wb = openpyxl.load_workbook("完成.xlsx")
ws = wb["Sheet"]
name_list = []
url_list = []
for name in list(ws.columns)[0]:
    name_list.append(name.value)
for url in list(ws.columns)[1]:
    url_list.append(url.value)
i = 0
for name1 in name_list:
    print(name1)
    print(url_list[i])
    i = i + 1
