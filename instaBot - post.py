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
while True:
    options = Options()
    useragent = "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36"
    options.set_preference("general.useragent.override", useragent)
    #profile = FirefoxProfile("/home/cam/Documents")

    user=""
    password=""

    #you will have to modify this to match the directory your webdriver sits. 
    driver = webdriver.Firefox(options=options, executable_path='/home/cam/Documents/geckodriver')

    #this is where the bot visits instagram, logs you in, if you filled in your usr and password above, and then starts making a new post. 
    driver.get('https://instagram.com')
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div>button:nth-child(1)"))).click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label^='Phone']"))).send_keys(user)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label^='Pass']"))).send_keys(password)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    time.sleep(5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button:nth-child(1)"))).click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "svg[aria-label^='New Post']"))).click()
    time.sleep(5)

    #This part is going to be spesific to your own OS's file manager. I am using arrows because this is running on Linux Lite, 
    #but you could probably just tell pyautogui to type in a folder directory, and use the while loop I have here to pic from your folder from random.
    #You will likely have to look up the documentation and use your brain here.
    print('pygui starting')
    fileDir = ['left','down','down','down','down',"down","down",'enter','right','down']
    i = 0
    t = random.randint(0,338)
    print(t)
    while i<= t:
        fileDir.append("down")
        i+=1
    fileDir.append('enter')
    #print(fileDir)
    pyautogui.press(fileDir)
    
    #now the bot will post your randomly selected image from your folder that holds a bank of images, and will give it hashtags that are from a bank of hashtags. 
    # Using the same hashtags multiple times flags you as spam which is why this is using a sampling method. 
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.UP43G"))).click()
    time.sleep(5)
    #To get a bank of hashtags just grab some from keywordtool.io. they are not bot friendly so Just do this once mannualy. 
    words = "#spacex #spaceisfake #spacejam #spaceart #spaceaesthetic #spaceandtime #spaceace #spacebabe #spacebetween #spacebattleshipyamato #bspace #bspacecakestudio #bspacemy #bspacesalon #bspacebbb #spacecraft #cspace #cspacekingedward #cspacefood #cspacefps #cspaceinteriors #spaced #spacedad #spacedandy #dspace #dspacesalon #dspacestore #dspaceston #dspacestudio #spaceexplorer #spaceecho #spaceengineers #espace #espacevert #espacetricot #espacewahiba #espacekilly #spaceflight #spacefox #spaceframe #fspace #fspacevyshgorod #fspacestudio #fspaced #fspacecharity #gspace #gspace_моделированиебровей #gspaceisland #gspace722 #gspaceid #spacehulk #spacehistory #spacehippie #spacehoax #spacehorse #hspace #hspacestudio #hspaceguaruja #hspacegallery #hspaceinteriors #spaceistheplace #ispace #ispaceswim #ispacesolutions #ispaceaustralia #ispacegh #spacejam2 #spacejam11s #spacejesus #jspaceman #jspace #jspacecreative #jspace_tv #jspacemen #spacek #spacekidschallenge #spacekid #spacekids #spacekru #spacelover #spacelove #spacelife #spacemarines40k #mspace #mspaceinvisiblegrills #mspacestall #mspaceinstock #mspaceพรี #spacenk #spacenerd #spacenails #spacenter #spaceodyssey #spaceorks #spaceoverdose #ospace #ospaceman #ospacearchitects #ospace2017 #ospaceshop #spacepainting #spacepics #spaceporn #pspace #pspacebrand #pspaceplyn #pspacegirl #pspacefur #spacequotes #spacequeen #spacequest #spaceq #spacequiz #qspace #qspacestudio #qspace_ala #qspaces #qspacemusic #spacer #spacerpolesie #spacerówka #rspace #rspaceporto #rspacehome #rspacebu #rspacegallery #spaces #spaceships #sspacesstore #sspace #ßpace #sspacestore #sspacerc #spacetime #spacetoon #spacetoday #tspace #tspacerhinebeck #tspaceavail #tspaceflower #tspacegallery #spaceunicorn #spaceutopian #spaceup #spaceutilization #spaceunit #uspace #uspacegallery #uspacela #uspaceвишневыйсад #uspaceyoga #spacevalley #spacevideos #spacevideo #spacevibes #spaceview #vspace #vspace成功店 #vspace文興店 #vspace縣政店 #vspaceconceptstorepadova #spacewolf #spaceweather #wspace #wspacekl #wspacevillacamilla #wspacerówce #wspacecollection #spacexdragon #spacexfalcon9 #spacexploration #xspace #xspacebali #xspacer #xspaceid #xspaceatx #spacey #spaceyacht #spaceylon #kevinspacey #spaceykacey #yspace #yspacelife #yspacesfeelgood #yspaceattheyuchengcomuseum #yspacecentralcoast #spacez #spacezoom #spacezebra #spacezeropoint #spacezone #zspace #zspaceuk #zspacesf #zspacetürkiye #zspacedesign #space07salon #space07 #space00cadetclothing #space01 #space0 #0space #0spaceman9 #0spaceshiplegohb #0spacers #0spacedog #space1999 #space10 #space15twenty #space115 #space1 #1spaceamplifier #1spacedad #1space #1spaceprojects #1spacefitness #space2 #space23 #space2flow #space220 #space25 #space3d #space3 #space39 #space360 #space364 #3space #3spaces #3spacesleft #3spaceships #3spacedesignstudio #space4d #space46boutique #space4 #space4women #space4humanity #4spaces #4space #4spaceshop #4spacedesign #4spacesleft #space5 #space519 #space55 #space538 #space550 #5space #5spacesleft #5spaces #5spacesavailable #5spacebound #space63 #space66 #space60stattoostudio #space6 #space65 #6spaces #6spacesleft #6space #6spacegray #6spacegrey #space7 #space776 #space704 #space7gallery #space71x #7space_yg #7space #7spaces #7spacesmensfashion #7spaced #space8 #space8kk #space8foxtrotinventory #space85jewelry #space85 #8spacegarden #8space #8space_garden #8spaces #8spacesleft #space9 #space91🌌 #space92 #space9community #space99 #9space #9spaces #9spacenterprodaction #9spacejam #9spaces9trees"
    words = words.split(" ")
    words = random.sample(words, 30)
    print(words)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))).send_keys(str(words))
    time.sleep(5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.UP43G"))).click()
    
    #driver then waits 2 hours to post again. 
    time.sleep(7200)
    driver.close()


