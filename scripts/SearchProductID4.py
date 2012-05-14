from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class SearchProductID4(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.zumiez.com/"
        self.verificationErrors = []
    
    def test_search_product_i_d4(self):
        driver = self.driver
        driver.get("/modcheckout/multipage/step3")
        driver.find_element_by_id("card_number").clear()
        driver.find_element_by_id("card_number").send_keys("41111111111111")
        # ERROR: Caught exception [ERROR: Unsupported command [select]]
        # ERROR: Caught exception [ERROR: Unsupported command [select]]
        driver.find_element_by_name("card_cvNumber").clear()
        driver.find_element_by_name("card_cvNumber").send_keys("1111")
        driver.find_element_by_css_selector("div.step3_next_step > input.hover").click()
        driver.find_element_by_id("card_number").clear()
        driver.find_element_by_id("card_number").send_keys("4111111111111111")
        driver.find_element_by_css_selector("div.step3_next_step > input.hover").click()
        # ERROR: Caught exception [ERROR: Unsupported command [getAlert]]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
