import os
import sys
import time
import csv
import codecs
import requests
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ast

url = 'https://bitcoincharts.com/charts/chart.json?m=bitstampUSD&SubmitButton=Draw&r=30&i=15-min&c=0&s=&e=&Prev=&Next=&t=S&b=&a1=&m1=10&a2=&m2=25&x=0&i1=&i2=&i3=&i4=&v=1&cv=0&ps=0&l=0&p=0&'
# html = urlopen(url).read().decode('utf-8')
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')

l = ast.literal_eval(soup.find('body').text.strip())
for i, x in enumerate(l): print(i, x)