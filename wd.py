from selenium import webdriver
import tts2

driver = webdriver.Chrome()


def google_search(whatToSearch):
    driver.get('https://www.google.com')

    search = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    search.click()
    search.send_keys(whatToSearch)

    element = driver.find_element_by_xpath('//*[@id="hplogo"]')
    element.click()


    searchbtn = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
    searchbtn.click()


def wikipedia_search(whatToSearch):
    driver.get('https://www.wikipedia.org/')

    search = driver.find_element_by_xpath('//*[@id="searchInput"]')
    search.click()
    search.send_keys(whatToSearch)

    searchbtn = driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
    searchbtn.click()

    para = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[3]')
    readable_text = para.text
    tts2.speak(readable_text)

def youtube_search(whatToSearch):
    driver.get('https://www.youtube.com/results?search_query=' + whatToSearch)
    
