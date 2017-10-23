
from selenium import webdriver
import time


def main():
    main_url = 'http://www.youtube-mp3.org/'
    driver = webdriver.Chrome()
    driver.get(main_url)
    cnvt_btn = driver.find_element_by_id('submit')
    url_form = driver.find_element_by_id('youtube-url')

    with open('song_urls.txt', 'r', encoding='utf-8') as f:
        song_urls = [line.strip() for line in f]

    for song_url in song_urls:
        url_form.clear()
        url_form.send_keys(song_url)
        cnvt_btn.click()
        time.sleep(3)

        try:
            dl_btn = driver.find_element_by_link_text('Download')
            dl_btn.click()

        except Exception as e:
            print('Unable to download')
            continue

    driver.quit()


if __name__ == '__main__':
    main()
