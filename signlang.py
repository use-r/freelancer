import os
import sys
import time
import csv
import codecs
import random
from urllib.request import urlretrieve
import json
import collections as cl
from collections import OrderedDict
import re
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup


# url = 'http://bslsignbank.ucl.ac.uk/media/bsl-video/DR/DROP.mp4'
# urlretrieve(url, 'test.mp4')

base_url1 = 'http://bslsignbank.ucl.ac.uk'
base_url2 = 'http://bslsignbank.ucl.ac.uk/dictionary/search/'
url = 'http://bslsignbank.ucl.ac.uk/dictionary/search/?query=A'
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')

next_pages = re.findall(r'<p>Jump to results page:(.*)</p>', html.replace('\n', ''))[0]
next_pages = [base_url2 + x['href'] for x in BeautifulSoup(next_pages, 'lxml').findAll('a')]
next_pages.append('')

for i, next_page in enumerate(next_pages):

	if (i == len(next_pages) - 1):
		break

	word_links = [base_url1 + x['href'] for x in soup.find('div', {'id': 'searchresults'}).findAll('a')]
	words = [x.text.strip() for x in soup.find('div', {'id': 'searchresults'}).findAll('a')]

	for word, word_link in zip(words, word_links):

		print(word, word_link)
		html = requests.get(word_link).text
		soup = BeautifulSoup(html, 'lxml')


		src_link = base_url1 + soup.find('iframe', {'id': 'videoiframe'})['src']

		html = requests.get(src_link).text
		soup = BeautifulSoup(html, 'lxml')

		src_link = base_url1 + soup.find('source', {'type': 'video/mp4'})['src']
		urlretrieve(src_link, word + '_' + src_link.split('/')[-1])

	print()

	print(next_page)
	html = requests.get(next_page).text
	soup = BeautifulSoup(html, 'lxml')

