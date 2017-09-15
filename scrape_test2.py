
import os
import sys
import time
import csv
import codecs
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

url = 'https://bitcoincharts.com/charts/bitstampUSD#rg30zig15-minztgSzm1g10zm2g25zv'
chrome_path = r'C:\Users\c1269\Desktop\personal\scraping\chromedriver.exe'
driver = webdriver.Chrome(chrome_path)
driver.get(url)

driver.find_element_by_link_text('Load raw data').click()
time.sleep(10)
