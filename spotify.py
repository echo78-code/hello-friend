from selenium import webdriver
import time 
import tts2


driver = webdriver.Chrome()
driver.get('https://open.spotify.com/?utm_source=pwa_install')

loginbtn = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[4]/button[2]')
loginbtn.click()
time.sleep(3)

    #btn = driver.find_element_by_xpath('')

usrname = driver.find_element_by_xpath("//input[@placeholder='Email address or username']")
usrname.click()
usrname.send_keys('freakingud1@gmail.com')

pswrd = driver.find_element_by_xpath('//*[@id="login-password"]')
pswrd.click()
pswrd.send_keys('spotfreak')
btn2 = driver.find_element_by_xpath('//*[@id="login-button"]')
btn2.click()

def playPause():
    webelement = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/div[3]/button')
    webelement.click()

def close():
    driver.close()
    driver.quit()

def next():
    webelement = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/div[4]/button')
    webelement.click()

def prev():
    webelement = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/div[2]/button')
    webelement.click()

def mute():
    webelement = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/footer/div[1]/div[3]/div/div[3]/button')
    webelement.click()

def shuffle():
    webelement = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/div[1]/button')
    webelement.click()

def repeat():
    webelement = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/div[5]/button')
    webelement.click()

def like():
    webelement = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/footer/div[1]/div[1]/div/div[3]/div/button')
    webelement.click()
    state = webelement.get_attribute('title')
    if (state == "Save to Your Library"):
        tts2.speak("song unliked")
    else:
        tts2.speak("song liked")

def nowPlaying():
    tts2.speak(driver.title)

def search(param1):
    webelement1 = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/nav/ul/li[2]/a/span')
    webelement1.click()
    time.sleep(1)
    webelement2 = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input')
    webelement2.click()
    webelement2.send_keys(param1)
    time.sleep(1)
    webelement3 = driver.find_element_by_xpath('//*[@id="searchPage"]/div/div/section[1]/div/div[2]/div/div/div/div[4]')
    webelement3.click()
    time.sleep(1)
    webelement4 = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[4]/div[1]/div/div[2]/div/div/div[2]/section/div[3]/div/button[1]')
    webelement4.click()

def home():
    webelement = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/nav/ul/li[1]/a/span')
    webelement.click()