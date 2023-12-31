# kalayab
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scan(searched):
    # starting driver
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get('https://divar.ir/s/tehran?q=' + searched)

    # the section that goods are in there
    section = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME,'main')))
    # check if goods are loaded
    try:
        WebDriverWait(section, 3).until(
            EC.presence_of_element_located((By.TAG_NAME,'a')))
    except:
        return {} #no results
    # finding goods
    goods = section.find_elements(By.TAG_NAME, 'a')
    goods_dict = {}
    for i in goods:  # Iterate over the first 10 items
        try:
            # find title
            title = i.find_element(By.TAG_NAME, 'h2').text
        except:
            title = 'NETWORK ERROR'

        try:
            # find prices
            prices = i.find_elements(By.XPATH, ".//div[@class='kt-post-card__description']")
            price_list = [price.text for price in prices]
        except:
            price_list = ['NETWORK ERROR']

        try:
            # get link
            link = i.get_attribute('href')
        except:
            link = 'NETWORK ERROR'

        goods_dict[title] = [price_list,link]
    return goods_dict