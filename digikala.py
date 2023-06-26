from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scan(searched):   
    #starting driver
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get('https://www.digikala.com/search/?q='+ searched)

    #the section that goods are in there
    section = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME,'section')))
    #check if goods are loaded
    WebDriverWait(section, 3).until(
            EC.presence_of_element_located((By.TAG_NAME,'a')))
    #finding goods
    goods = section.find_elements(By.TAG_NAME,'a')
    goods_dict = {}
    for good in goods:

        try:
            #find title
            title = good.find_element(By.TAG_NAME,'h3').text
        except:
            title = 'NETWORK ERROR'
        
        try:
            #find price
            price = good.find_element(By.XPATH,".//div[@class='d-flex ai-center jc-end gap-1 color-700 color-400 text-h5 grow-1']").text
        except:
            price = 'NETWORK ERROR'

        try:
            #get link
            link = good.get_attribute('href')
        except:
            link = 'NETWORK ERROR'
        
        goods_dict[title] = [price,link]
    return goods_dict