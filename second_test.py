from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest


class SecondTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./drivers/chromedriver.exe")

    def test_one_product_cost_in_basket(self):
        driver = self.driver
        driver.set_page_load_timeout(10)
        driver.maximize_window()
        driver.get("https://www.x-kom.pl/")

        driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[2]/a').send_keys(Keys.ENTER)
        driver.find_element_by_xpath(
            '//*[@id="pageWrapper"]/div[3]/div[2]/aside/section/ul/li[2]/ul/li[2]/a').send_keys(Keys.ENTER)

        product_price = driver.find_element_by_xpath(
            "//*[@id='productList']//*[@class='product-item product-impression']//*[@class='price-wrapper']//*[@class='prices']//*[@class='price text-nowrap']").text

        driver.find_element_by_xpath('//*[@id="productList"]/div[1]/button').send_keys(Keys.ENTER)

        driver.refresh()

        price_in_basket = driver.find_element_by_xpath(
            "//*[@id='basketItemsWrapper']//*[@class='basket-summary']//*[@class='total-basket-price pull-right']//*[@class='price-value-label js-basket-price']").text

        print('Product price: ', product_price)
        print('Price of the product in the basket: ', price_in_basket)

        self.assertEqual(product_price, price_in_basket)

        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()