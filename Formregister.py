import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from WebAutomation.test import TestSelenium

class Formregister(TestSelenium):
    name="//input[@id='name']"
    email="//input[@id='email']"
    phone="//input[@id='phone']"
    address="//textarea[@id='textarea']"
    gender_male="//input[@id='female']"
    gender_female="//input[@id='female']"
    days_sun="//input[@id='sunday']"
    days_mon="//input[@id='monday']"
    days_tue="//input[@id='tuesday']"
    days_wed="//input[@id='wednesday']"
    days_thu="//input[@id='thursday']"
    days_fri="//input[@id='friday']"
    days_sat="//input[@id='saturday']"
    country="//select[@id='country']/option[@value='uk']"
    colors_blue="//select[@id='colors']/option[@value='blue']"
    colors_green="//select[@id='colors']/option[@value='green']"
    sorted_list="//select[@id='animals']/option[@value='zebra']"
    submit="//button[@class='submit-btn']"

    def enter_details(self):
        self.enter_text("xpath",self.name,"Parthiban")
        self.enter_text("xpath",self.email,"parthi@gamil.com")
        self.enter_text("xpath",self.phone,"917111")
        self.enter_text("xpath",self.address,"122,fair")

    def click_submit(self):
        self.element_click("xpath",self.gender_male)
        self.element_click("xpath",self.days_mon)
        self.element_click("xpath",self.country)
        self.element_click("xpath",self.colors_blue)
        self.element_click("xpath",self.sorted_list)
        self.element_click("xpath",self.submit)
        time.sleep(10)

    def close_browser(self):
        self.driver.close()

obj=Formregister()
obj.initialize()
obj.launch_url("https://testautomationpractice.blogspot.com/")
obj.enter_details()
obj.click_submit()
obj.close_browser()