from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import pyautogui
import time
import random

options = Options()
useragent = "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36"
options.set_preference("general.useragent.override", useragent)

user=""
password=""
uVar=[]

driver = webdriver.Firefox(options=options, executable_path='/home/cam/Documents/geckodriver')
driver.get('https://instagram.com')
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div>button:nth-child(1)"))).click()
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label^='Phone']"))).send_keys(user)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label^='Pass']"))).send_keys(password)
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(5)


#note that this got me kicked off instagram so maybe add some sleep timers and use a less popular account. I am not going to clean this up because you will probably get booted if you use it anyway. 
while True:
    driver.get('https://www.instagram.com/therock/')
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    
    posts = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.v1Nh3>a[tabindex='0']")))
    
    for post in posts:
        uVar.append(post.get_attribute('href'))
        print(post.get_attribute('href'))

    f=0
    while f <= len(posts):
        try:
            driver.get(uVar[f])
            f+=1
            time.sleep(5)
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.Nm9Fw>a.zV_Nj"))).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="dialog"]'))).click()
            time.sleep(5)
            
            try:
                time.sleep(3)
                users = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.Igw0E>button.sqdOP.L3NKy.y3zKF[type="button"]')))
                for user in users:
                    user.click()
                    print("clicked")
            except:
                print('error')
                continue
        except:
            print('post not working')
            f+=1
            continue