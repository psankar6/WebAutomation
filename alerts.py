# import webdriver
from selenium import webdriver
import time

# import Alert
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
# get ide.geeksforgeeks.org
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)
# create alert object
driver.find_element(By.XPATH, "//button[@id='alertBtn']").click()
time.sleep(2)
# alert = Alert(driver)
alert = driver.switch_to.alert
# alert=Alert(driver)
time.sleep(2)
text = alert.text
alert.accept()
time.sleep(2)
print("alert text", text)
# driver.find_element(By.XPATH, "//input[@type='file']").send_keys("C:\Users\PARTHIBAN\Desktop\upload.txt")
time.sleep(5)
driver.close()
