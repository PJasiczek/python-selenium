from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import csv
import unittest


class FirstTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./drivers/chromedriver.exe")

    def test_best_prices_product(self):
        driver = self.driver
        driver.set_page_load_timeout(10)
        driver.maximize_window()
        driver.get("https://www.x-kom.pl/")

        driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[2]/a') \
            .send_keys(Keys.ENTER)
        driver.find_element_by_xpath(
            '//*[@id="pageWrapper"]/div[3]/div[2]/aside/section/ul/li[2]'
            '/ul/li[2]/a').send_keys(Keys.ENTER)

        driver.refresh()

        driver.find_element_by_xpath('//*[@id="productListUtilitiesBar"]'
                                     '/div[3]/div/div').click()
        driver.find_element_by_xpath('//*[@id="productListUtilitiesBar"]'
                                     '/div[3]/div/ul/li[3]/a/label').click()

        driver.refresh()

        product_name = driver.find_element_by_xpath(
            '//*[@id="productList"]//*[@class="product-item product-impression"]//*[@class="description-wrapper"]//*[@class="name"]').text
        product_price = driver.find_element_by_xpath(
            '//*[@id="productList"]//*[@class="product-item product-impression"]//*[@class="price-wrapper"]//*[@class="prices"]//*[@class="price text-nowrap"]').text

        product_price = product_price.replace(' zł', '')
        product_price = product_price.replace(',', '.')

        print("The most expensive smartwatch from the store's offer: " +
              product_name + " : " + product_price)

        with open('results.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                print("The most expensive smartwatch from the store's offer from the previous test: ", row[0] + " " + row[1])

        smartwatches = [[product_name, product_price]]

        self.assertEqual(row[0] + " " + row[1],
                         product_name + " " + product_price)

        with open('results.csv', 'a') as writeFile:
            writeFile.seek(0)
            writeFile.truncate()
            writer = csv.writer(writeFile)
            writer.writerows(smartwatches)

        writeFile.close()

        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()