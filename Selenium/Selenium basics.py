from selenium import webdriver
from selenium.webdriver.common.by import By

path = r"C:\Users\malir\Desktop\chromedriver.exe"
browser = webdriver.Chrome(path)
browser.get('https://www.seleniumhq.org')
elem = browser.find_element(By.LINK_TEXT,'Downloads')
print(elem.text)
print(elem.get_attribute('href'))
elem.click()
