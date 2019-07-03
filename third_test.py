from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest


class ThirdTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./drivers/chromedriver.exe")

    def test_add_prices_product_in_basket(self):
        driver = self.driver
        driver.set_page_load_timeout(10)
        driver.maximize_window()
        driver.get("https://www.x-kom.pl/")

        driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[2]/a').send_keys(Keys.ENTER)
        driver.find_element_by_xpath(
            '//*[@id="pageWrapper"]/div[3]/div[2]/aside/section/ul/li[2]/ul/li[2]/a').send_keys(Keys.ENTER)

        product_price = driver.find_element_by_xpath(
            "//*[@id='productList']//*[@class='product-item product-impression']//*[@class='price-wrapper']//*[@class='prices']//*[@class='price text-nowrap']").text

        product_price = product_price.replace(' zł', '')
        product_price = product_price.replace(',', '.')

        sum_products_prices = product_price

        driver.find_element_by_xpath('//*[@id="productList"]/div[1]/button').send_keys(Keys.ENTER)

        driver.refresh()

        driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[2]/a').send_keys(Keys.ENTER)
        driver.find_element_by_xpath(
            '//*[@id="pageWrapper"]/div[3]/div[2]/aside/section/ul/li[2]/ul/li[2]/a').send_keys(
            Keys.ENTER)

        product_price = driver.find_elements_by_xpath(
            "//*[@id='productList']//*[@class='product-item product-impression']//*[@class='price-wrapper']//*[@class='prices']//*[@class='price text-nowrap']")[
            3].text

        product_price = product_price.replace(" zł", "")
        product_price = product_price.replace(',', '.')

        sum_products_prices = sum_products_prices.replace(" zł", "")
        sum_products_prices = sum_products_prices.replace(',', '.')

        sum_products_prices = float(sum_products_prices) + float(product_price)

        driver.find_element_by_xpath('//*[@id="productList"]/div[4]/button').send_keys(Keys.ENTER)

        driver.refresh()

        price_in_basket = driver.find_element_by_xpath(
            "//*[@id='basketItemsWrapper']//*[@class='basket-summary']//*[@class='total-basket-price pull-right']//*[@class='price-value-label js-basket-price']").text
        price_in_basket = price_in_basket.replace(" zł", "")
        price_in_basket = price_in_basket.replace(',', '.')
        driver.refresh()

        print('The sum of products: ', sum_products_prices, ' zł')
        print('Price of the product in the basket: ', float(price_in_basket), ' zł')

        self.assertEqual(sum_products_prices, float(price_in_basket))

        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
