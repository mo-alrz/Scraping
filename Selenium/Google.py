from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('https://www.google.com')
lang = browser.find_element(By.CLASS_NAME,'V5OCtd')
lang.click()

eng = browser.find_element(By.XPATH,'//*[@id="tbTubd"]/div/li[12]')
eng.click()

accept_all = browser.find_element(By.ID,'L2AGLb')
accept_all.click()
text_area = browser.find_element(By.XPATH,'//*[@id="APjFqb"]')
text_area.send_keys('How to automate with python')
text_area.send_keys(Keys.ENTER)
time.sleep(1000)
