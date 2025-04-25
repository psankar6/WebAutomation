from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Initialize WebDriver (choose your browser)
driver = webdriver.Chrome()  # Or Firefox, Edge, etc.  Make sure you have the correct webdriver installed.
driver.get("https://testautomationpractice.blogspot.com/")  # Replace with the URL of the page containing your table
# c) By XPath (use with caution, can be brittle):
driver.maximize_window()
table = driver.find_element(By.XPATH, "//div[@class='column-center-inner']")  # Selects the first table on the page (less reliable)
# ***It's crucial to use the most specific locator possible to avoid selecting the wrong table.***
rows = table.find_elements(By.TAG_NAME, "tr")  # Find all rows (tr elements)
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")  # Find all data cells (td elements) in each row
    for cell in cells:
        print(cell.text, end=" | ")  # Print cell content
    print()  # Newline after each row
# Instead of time.sleep(), use WebDriverWait to wait for the table to load:
try:
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='column-center-inner']"))  # Or your chosen locator
    )
    # ... (rest of your table interaction code)
except Exception as e:
    print(f'Table not found: {e}')
    driver.close()