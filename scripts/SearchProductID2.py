from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class SearchProductID2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.zumiez.com/"
        self.verificationErrors = []
    
    def test_search_product_i_d2(self):
        driver = self.driver
        driver.get("/")
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys("188028")
        driver.find_element_by_css_selector("input.hover").click()
        driver.find_element_by_id("tile-410").click()
        driver.find_element_by_id("pdp-add-to-bag-button").click()
        driver.find_element_by_link_text("View Bag").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
