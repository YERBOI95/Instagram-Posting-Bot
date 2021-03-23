from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import pyautogui
import time

options = Options()
useragent = "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36"
options.set_preference("general.useragent.override", useragent)
profile = FirefoxProfile("/home/cam/Documents")

user=""
password=""

driver = webdriver.Firefox(options=options,firefox_profile=profile, executable_path='/home/cam/Documents/geckodriver')
driver.get('https://instagram.com')
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div>button:nth-child(1)"))).click()
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label^='Phone']"))).send_keys(user)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label^='Pass']"))).send_keys(password)
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(5)
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button:nth-child(1)"))).click()
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "svg[aria-label^='New Post']"))).click()
#gotta figure this out
time.sleep(5)
print('pygui starting')
pyautogui.press(['left', 'down', 'down', 'enter','right','enter','down','down','up','enter'])
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.UP43G"))).click()
time.sleep(5)
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.UP43G"))).click()

