
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict

fname_out = 'output.txt'


def getinfo(url):
	sep = '\t'

	html = requests.get(url).text
	soup = BeautifulSoup(html, 'lxml')

	title = soup.select('div.title > h1')[0].text.strip()
	loc = soup.find('span', {'class': 'location'}).text.strip()
	city, state = map(str.strip, loc.split(','))
	price = soup.find('strong', {'class': 'price'}).text.strip()
	img_srcs = soup.find('div', {'class': 'container'})

	if img_srcs:
		img_srcs = [x['href'] for x in img_srcs.findAll('a')]
	else:
		img_srcs = [soup.find('figure').find('img')['src']]

	infos = OrderedDict([
		('Metros Cuadrados', ''),
		('Estrato', ''),
		('Cuartos', ''),
		('Cuartos de', ''),
		('Antig', '')
	])

	info_keys = soup.find('ul', {'class': 'item_partials_optionals_view'}).findAll('strong')
	info_keys = [x.text.replace(':', '').strip() for x in info_keys]
	info_vals = soup.find('ul', {'class': 'item_partials_optionals_view'}).findAll('span')
	info_vals = [x.text.strip() for x in info_vals]

	for i, key in enumerate(infos.keys()):
		for info_key, info_val in zip(info_keys, info_vals):
			if key in info_key:
				infos[key] = info_val

	desc = soup.find('p', {'class': 'item_partials_description_view'})
	desc = desc.text.replace('\n', '').strip()

	output = [title, url, city, state, price]
	for key, value in infos.items():
		output.append(value)
	output.extend(img_srcs)

	with open(fname_out, 'a', encoding='utf-8') as f:
		f.write(sep.join(output) + '\n')


def main():
	base_url = 'https:'
	url = 'https://www.olx.com.co/nf/search/casas%20en%20medellin%20en%20ventas'
	html = requests.get(url).text
	soup = BeautifulSoup(html, 'lxml')

	with open(fname_out, 'w', encoding='utf-8') as f:
		pass

	cnt = 0
	while True:
		cnt += 1
		print('page ', cnt)
		home_urls = soup.find('ul', {'class': 'items-list'}).findAll('a')
		home_urls = [base_url + x['href'] for x in home_urls]

		for home_url in home_urls:
			print(home_url)
			getinfo(home_url)
		print()

		next_url = soup.find('a', {'rel': 'next'})

		if next_url:
			next_url = base_url + next_url['href']
			if 'https:#' in next_url:
				break
			else:
				html = requests.get(next_url).text
				soup = BeautifulSoup(html, 'lxml')
		else:
			break


if __name__ == '__main__':
	main()
