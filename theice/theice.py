import os
import sys
import time
import csv
import codecs
import calendar
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def main():
    url = 'https://www.theice.com/marketdata/reports/179'
    driver = webdriver.Chrome()
    driver.get(url)

    accept_btn = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn')))
    accept_btn.click()

    d1 = date(2015, 3, 20)  # start date
    d2 = date(2017, 8, 15)  # end date
    delta = d2 - d1         # timedelta
    date_list = []

    for i in range(delta.days + 1):
        x = str(d1 + timedelta(days=i))
        year, month, day = x.split('-')

        if month[0] == '0': month = month[1]
        month = calendar.month_abbr[int(month)]
        new_date = '-'.join([day, month, year])
        date_list.append(new_date)

    auc_times = ['morning', 'afternoon']

    fname = 'output.txt'
    with open(fname, 'w') as f: pass

    prev = ''

    for date in date_list:
    	report_date = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'reportDate')))
    	report_date.clear()
    	report_date.send_keys(date)
    	time.sleep(0.1)

    	for i, auc_time in enumerate(auc_times):
    		while True:
    			try:
    				time_selector = driver.find_element_by_id('sessionNumber_chosen')
    				time_selector.click()
    				break
    			except Exception as e:
    				time.sleep(0.1)
    				continue

    		options = time_selector.find_elements_by_css_selector('li.active-result')
    		options[i].click()

    		submit_btn = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//input[@name="htmlReport"]')))
    		submit_btn.click()
    		time.sleep(3)

    		if driver.find_elements_by_css_selector('div.alert-warning'):
    			output = []
    			output.append(date)
    			output.append(auc_time)
    			output.append('No results')
    			print(output)
    			continue

    		while True:
    			trs = driver.find_elements_by_css_selector('table.table-data > tbody > tr')
    			now = trs[0].find_elements_by_tag_name('td')[1].text
    			if prev != now:
    				prev = now
    				break
    			time.sleep(0.1)

    		time.sleep(0.5)

    		for tr in trs:
    			output = [date, auc_time]

    			for td in tr.find_elements_by_tag_name('td'):
    				output.append(td.text.strip())

    			print(output)
    			with open(fname, 'a') as f: f.write(';'.join(output) + '\n')

if __name__ == '__main__':
    main()
