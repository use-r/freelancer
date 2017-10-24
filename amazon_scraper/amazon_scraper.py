from selenium import webdriver
import time


def main():
    url = 'http://www.amazon.com/'
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    cnt = 0

    try:
        input_form = driver.find_element_by_id('twotabsearchtextbox')
        input_form.send_keys('Asus laptop')
        submit_btn = driver.find_element_by_css_selector('input.nav-input')
        submit_btn.click()

        for _ in range(3):
            results = driver.find_elements_by_css_selector(
                'h2.a-size-medium.s-inline.s-access-title.a-text-normal'
            )
            prices = driver.find_elements_by_css_selector(
                'span.a-color-base.sx-zero-spacing'
            )

            print(len(results))
            print(len(prices))

            for result, price in zip(results, prices):

                cnt += 1
                print(
                    str(cnt) + ' : ' + result.text[0:10] +
                    ', ' + price.get_attribute('aria-label')
                )

            next_url = driver.find_element_by_id('pagnNextLink').get_attribute('href')
            driver.get(next_url)

        driver.quit()

    except Exception as e:
        driver.quit()
        print(e)


if __name__ == '__main__':
    main()
