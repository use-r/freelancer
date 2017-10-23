
import time
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

base_url = 'https://www.walletexplorer.com'


def getinfo(url):
	while True:
		try:
			html = requests.get(url, verify=False).text
			break
		except Exception as e:
			print('Requests error. Waiting for 60 seconds')
			time.sleep(60)
			continue
	soup = BeautifulSoup(html, 'lxml')

	fname = url.split('/')[-2] + '.txt'
	sep = '\t'
	is_last = False
	cnt = 0

	while True:
		cnt += 1
		print('page', cnt)
		trs = soup.findAll('tr')

		if cnt == 1:
			header = ['site'] + [x.text for x in trs[0].findAll('th')]
			print(header)
			with open(fname, 'w', encoding='utf-8') as f:
				f.write(sep.join(header) + '\n')  # create output file and write header

		for tr in trs[1:]:
			output = [fname.replace('.txt', '')]

			for td in tr.findAll('td'):
				output.append(td.text.replace('\xa0', ''))

			with open(fname, 'a', encoding='utf-8') as f:
				f.write(sep.join(output) + '\n')  # write ouptput

		pages = soup.find('div', {'class': 'paging'}).findAll('a')

		if not pages:
			print('This is the last page.')
			break
		else:
			for page in pages:  # iterate over page links to find next link
				is_last = True
				if 'Next' in page.text or 'Last' in page.text:  # means next page is found
					next_url = base_url + page['href']
					is_last = False
					break

		if is_last:
			print('This is the last page.')
			break
		else:
			html = requests.get(next_url).text
			soup = BeautifulSoup(html, 'lxml')
			print()


def getpage(url):
	html = requests.get(url).text
	soup = BeautifulSoup(html, 'lxml')
	page = soup.find('div', {'class': 'paging'}).text.split('/')[-1].strip()
	page = page.split()[0]
	print(page)

	return page


if __name__ == '__main__':
	top_url = 'https://www.walletexplorer.com/'
	html = requests.get(top_url).text
	soup = BeautifulSoup(html, 'lxml')
	table = soup.find('table', {'class': 'serviceslist'})
	urls = [base_url + x['href'] + '/addresses' for x in table.findAll('a')]

	with Pool(10) as p:
		p.map(getinfo, urls[0:10])
