
import requests
from bs4 import BeautifulSoup

def main():
	url = 'https://www.icoalert.com/'
	html = requests.get(url).text
	soup = BeautifulSoup(html, 'lxml')

	sep = '\t'
	header = 'Name-Type-Link'.split('-')
	fname = 'icoalert.txt'
	with open(fname, 'w', encoding='utf-8') as f:
		f.write(sep.join(header) + '\n'	)

	fname = 'icoalert.txt'
	sections = ['active', 'upcoming', 'recent']
	typs = ['active', 'upcoming', 'past']

	for section, typ in zip(sections, typs):
		icos = soup.find('div', {'class': section}).findAll('div', {'class': 'ico-wrap'})

		for ico in icos:
			name = ico.find('div', {'class': 'about'}).find('h3').text.split(' — ')[0]
			url = ico.find('div', {'class': 'ico-links'}).find('a')['href']

			output = [name, typ, url]
			with open(fname, 'a', encoding='utf-8') as f:
				f.write(sep.join(output) + '\n')
			try:
				print(output)
			except Exception as e:
				print('Character error')


if __name__ == '__main__':
	main()
