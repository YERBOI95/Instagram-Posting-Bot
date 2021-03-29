from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
from urllib.parse import unquote

options = Options()
useragent = "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36"
options.set_preference("general.useragent.override", useragent)

driver = webdriver.Firefox(options=options, executable_path='/home/cam/Documents/geckodriver')

#Line below is directing my browser to my search, which is just "space" copy the url on your search so you can collect from your own terms. 
driver.get('https://www.google.com/search?q=space&client=ubuntu&hs=95c&channel=fs&sxsrf=ALeKk02jskLYR689wExqeTtqtBFD_ScncQ:1616794665893&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjyoPC99c7vAhWRXc0KHc3gCGIQ_AUoAXoECAEQAw&biw=1366&bih=638')

#Here I am asking the webdriver to scroll to the bottom of a page 6 times so all of the images load
e=0
while e <= 5:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(5)
    e+=1


#This part was tricky, each image needs to be clicked, and then the source url needs to be scraped. Once it's scraped you ask urllib to put it into your destination folder. 
# The act of actually clicking on the image is the part that broke the original google-images-download API
images = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.isv-r>a.wXeWr')))
i=0
for image in images:
    try:
        image.click()
        badlink = image.get_attribute("href")
        #print(badlink)
        betterlink = unquote(badlink).split('..')[0].split('imgurl=')[1]
        goodlink = str(betterlink).split('&')[0]
        print(goodlink)
        filepath = str(i)+".jpg"
        urllib.request.urlretrieve(goodlink,filepath)
        i+=1
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.hm60ue'))).click()
    except:
        print('except')
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.hm60ue'))).click()

driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
time.sleep(5)