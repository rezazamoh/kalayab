# kalayab
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scan(searched):   
    #starting driver
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get('https://www.sheypoor.com/s/iran?q='+ searched)

    #the section that goods are in there
    section = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME,'main')))
    #check if goods are loaded
    WebDriverWait(section, 3).until(
            EC.presence_of_element_located((By.TAG_NAME,'article')))
    #finding goods
    goods = section.find_elements(By.TAG_NAME,'article')
    goods_dict = {}
    for good in goods:
        try:
            #find title
            title = good.find_element(By.TAG_NAME,'h2').text
        except:
            title = 'NETWORK ERROR'
        
        try:
            #find price
            price = good.find_element(By.XPATH,".//p[@class='price']").text
         
            
        except:
            price = 'توافقی'

        try:
            #get link
            link = good.find_element(By.TAG_NAME, 'a').get_attribute('href')
        except:
            link = 'NETWORK ERROR'
        
        goods_dict[title] = [price,link]
    print(goods_dict)
    return goods_dict
p=input()
scan(p)
