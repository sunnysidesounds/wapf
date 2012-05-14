from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class SearchProductID3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.zumiez.com/"
        self.verificationErrors = []
    
    def test_search_product_i_d3(self):
        driver = self.driver
        driver.get("//")
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys("170205")
        driver.find_element_by_css_selector("input.hover").click()
        driver.find_element_by_id("tile-416").click()
        driver.find_element_by_id("pdp-add-to-bag-button").click()
        driver.find_element_by_link_text("View Bag").click()
        driver.find_element_by_css_selector("#cart-group-links > a > img.hover").click()
        driver.find_element_by_id("first_name").clear()
        driver.find_element_by_id("first_name").send_keys("Developer")
        driver.find_element_by_id("first_name").clear()
        driver.find_element_by_id("first_name").send_keys("John")
        driver.find_element_by_id("last_name").clear()
        driver.find_element_by_id("last_name").send_keys("Developer")
        driver.find_element_by_id("company_name").clear()
        driver.find_element_by_id("company_name").send_keys("Zumiez")
        driver.find_element_by_id("address1").clear()
        driver.find_element_by_id("address1").send_keys("123 Alpha Street")
        driver.find_element_by_id("city").clear()
        driver.find_element_by_id("city").send_keys("Redmond")
        # ERROR: Caught exception [ERROR: Unsupported command [select]]
driver.find_element_by_id("postal_code").clear()
driver.find_element_by_id("postal_code").send_keys("98052")
driver.find_element_by_id("primary_phone").clear()
driver.find_element_by_id("primary_phone").send_keys("123-456-6767")
driver.find_element_by_id("email").clear()
driver.find_element_by_id("email").send_keys("developer@zumiez.com")
        driver.find_element_by_css_selector("a[title=\"Next Step\"] > img.hover").click()
        driver.find_element_by_xpath("//input[@name='method' and @value='tableratestandard_bestway']").click()
        driver.find_element_by_css_selector("div.step2_next_step > input.hover").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
