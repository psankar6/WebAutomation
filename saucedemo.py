import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from WebAutomation.base import BaseSelenium


class Saucedemo(BaseSelenium):

    user_name = "standard_user"
    password = "secret_sauce"
    login_button = "login-button"
    products_page_title = "//span[@data-test='title']"
    product1="//img[@data-test='inventory-item-sauce-labs-bike-light-img']"
    addtocart_button="//button[@id='add-to-cart']"
    shoppingcart_link="//a[@class='shopping_cart_link']"
    checkout="//button[@id='checkout']"
    firstname="//input[@id='first-name']"
    lastname="//input[@id='last-name']"
    postalcode="//input[@id='postal-code']"
    continuebutton=" //input[@id='continue']"
    finishbutton="//button[@id='finish']"
    openmenu="//button[@id='react-burger-menu-btn']"
    logout="//a[@id='logout_sidebar_link']"

    def authentication(self):
        self.enter_text("id", "user-name", self.user_name)
        self.enter_text("id", "password", self.password)

    def login(self):
        self.click_element("id", self.login_button)
        time.sleep(5)

    def productpage(self):
        exppagetitle='Products'
        actpage1=self.get_element_text("xpath", self.products_page_title)
        print(f"page title:{actpage1}")
        assert exppagetitle == actpage1
        self.click_element("xpath", self.product1)
        # time.sleep(3)

    def addtocart(self):
        self.click_element("xpath",self.addtocart_button)
        self.click_element("xpath",self.shoppingcart_link)

    def yourcart(self):
        self.click_element("xpath",self.checkout)

    def enter_customerinformation(self):
        self.enter_text("xpath",self.firstname,"Parthiban")
        self.enter_text("xpath",self.lastname,"Sankaran")
        self.enter_text("xpath",self.postalcode,"1234")
        self.click_element("xpath",self.continuebutton)

    def checkoutoverview(self):
        self.click_element("xpath",self.finishbutton)
        # time.sleep(3)

    def checkoutcomplete(self):
        self.click_element("xpath",self.openmenu)
        self.click_element("xpath",self.logout)


obj=Saucedemo()
obj.initialize()
obj.launchurl("https://www.saucedemo.com/")
obj.authentication()
obj.login()
obj.productpage()
obj.addtocart()
obj.yourcart()
obj.enter_customerinformation()
obj.checkoutoverview()
obj.checkoutcomplete()
obj.closebrowser()


