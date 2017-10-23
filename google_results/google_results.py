import time
import random
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_total(domains):
	driver = webdriver.PhantomJS()
	delay = 30
	google_url = 'https://www.google.nl'

	today = '{d.day}-{d.month}-{d.year}'.format(d=datetime.now())

	fname = 'output.txt'
	sep = '\t'
	header = sep.join(['Domain', 'Date', 'Total'])
	with open(fname, 'w', encoding='utf-8') as f:
		f.write(sep.join(header) + '\n')

	for i, domain in enumerate(domains):
		driver.get(google_url)
		search_form = WebDriverWait(driver, delay).until(
			EC.presence_of_element_located((By.NAME, 'q'))
		)
		search_form.send_keys('site:' + domain)
		time.sleep(0.1)

		while True:
			try:
				search_btn = WebDriverWait(driver, delay).until(
					EC.element_to_be_clickable((By.NAME, 'btnG'))
				)
				search_btn.click()
				break
			except Exception as e:
				print(e)
				time.sleep(0.1)
				continue

		total = WebDriverWait(driver, delay).until(
			EC.presence_of_element_located((By.ID, 'resultStats'))
		)
		total = total.text.split()[1].replace('.', '')
		output = [domain, today, str(total)]
		print(output)

		with open(fname, 'a', encoding='utf-8') as f:
			f.write(sep.join(output) + '\n')

		time.sleep(random.randint(50, 70))

	driver.quit()


if __name__ == '__main__':
	domains = ['freelancer.com', 'linkedin.com']
	get_total(domains)
