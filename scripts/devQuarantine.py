from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class DevQuarantine(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://dev.zumiez.com/"
        self.verificationErrors = []
    
    def test_dev_quarantine(self):
        driver = self.driver
        driver.get(self.base_url + "/quarantine/index/verify")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("couch600")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
