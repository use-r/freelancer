import requests
from bs4 import BeautifulSoup
import re
import operator
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def scrape():
    baseurl = 'https://qiita.com/tags/Python/items?page={}'
    page = 1
    tag_dict = {}
    is_end = False

    while not is_end:
        print('page:', page)
        url = baseurl.format(page)
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'lxml')
        items = soup.select('article.ItemLink')
        cnt = 0

        for item in items:
            post_date = item.select('div.ItemLink__info')[0].text
            post_date = re.search(r'(\S+\s\d+,\s\d+)', post_date).group(1).strip()
            if post_date.split(', ')[-1] == '2016':
                cnt += 1
                if cnt > 5:
                    is_end = True
                    break
                else:
                    continue

            tags = [x.text.strip() for x in item.select('li.TagList__item')]
            for tag in tags:
                if tag not in tag_dict:
                    tag_dict[tag] = 1
                else:
                    tag_dict[tag] += 1

        page += 1

    with open('python_tags.csv', 'w', encoding='utf-8') as f:
        tag_list = sorted(tag_dict.items(), key=operator.itemgetter(1), reverse=True)
        for tag in tag_list:
            f.write(','.join(map(str, tag)) + '\n')

    print('scrape done')


def make_graph():
    tags = []
    nums = []
    with open('python_tags.csv', 'r', encoding='utf-8') as f:
        for line in f:
            tag, num = line.strip().split(',')
            if 'python' not in tag.lower():
                tags.append(tag + ' (' + num + ')')
                nums.append(num)
            if len(tags) == 20: break

    tags = tags[::-1]
    nums = nums[::-1]
    x = np.arange(1, 21)

    fig = plt.figure()
    fp = FontProperties(fname=r'yugothib.ttf', size=10)
    fig.patch.set_facecolor('white')
    plt.barh(x, nums, tick_label=tags, align='center')
    plt.yticks(fontproperties=fp)
    plt.show()


def main():
    scrape()
    make_graph()


if __name__ == '__main__':
    main()
