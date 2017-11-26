import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def main():
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
    fp = FontProperties(fname=r'yugothib.ttf', size=14)
    fig.patch.set_facecolor('white')
    plt.barh(x, nums, tick_label=tags, align='center')
    plt.yticks(fontproperties=fp)
    plt.show()

if __name__ == '__main__':
    main()
