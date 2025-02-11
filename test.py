import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import none_of
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver =None

class TestSelenium(object):

    def __init__(self):
        super().__init__()
        self.driver=driver

    def initialize(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def launch_url(self,url):
        self.driver.get(url)

    def get_locator_type(self,type):
        if type.upper()=="ID":
            return By.ID
        elif type.upper()=="CLASS":
            return By.CLASS_NAME
        elif type.upper()=="TAG":
            return By.TAG_NAME
        elif type.upper()=="XPATH":
            return By.XPATH
        elif type.upper()=="LINK TEXT":
            return By.LINK_TEXT
        elif type.upper()=="PARTIAL LINK TEXT":
            return By.PARTIAL_LINK_TEXT
        elif type.upper()=="CSS":
            return By.CSS_SELECTOR

    def enter_text(self, locatorType, locator, inputText):
        #element = self.get_web_element(locatorType, locator)
        element = self.wait_until_element_visible(locatorType, locator)
        element.send_keys(inputText)

    def element_click(self,locatorType, locator):
        element=self.wait_until_element_visible(locatorType, locator)
        element.click()

    def wait_until_element_visible(self, locatorType, locator, timeout=60):
        locatorType = self.get_locator_type(locatorType)
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located((locatorType, locator)))

    def wait_until_element_present(self, locatorType, locator, timeout=60):
        locatorType = self.get_locator_type(locatorType)
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located((locatorType, locator)))









