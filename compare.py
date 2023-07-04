# kalayab
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def digikala(searched):   
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
    global goods_dict
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


def sheypoor(searched):   
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
    global goods_dict_2
    goods_dict_2 = {}
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
            price = 'NETWORK ERROR'

        try:
            #get link
            link = good.find_element(By.TAG_NAME, 'a').get_attribute('href')
        except:
            link = 'NETWORK ERROR'
        
        goods_dict_2[title] = [price,link]
   # print(goods_dict_2)
    return goods_dict_2



def divar(searched):
    # starting driver
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get('https://divar.ir/s/tehran?q=' + searched)

    # the section that goods are in there
    section = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME,'main')))
    # check if goods are loaded
    WebDriverWait(section, 3).until(
        EC.presence_of_element_located((By.TAG_NAME,'a')))
    # finding goods
    goods = section.find_elements(By.TAG_NAME, 'a')
    global goods_dict_3
    goods_dict_3 = {}
    for i in range(10):  # Iterate over the first 10 items
        good = goods[i]
        try:
            # find title
            title = good.find_element(By.TAG_NAME, 'h2').text
        except:
            title = 'NETWORK ERROR'

        try:
            # find prices
            prices = good.find_elements(By.XPATH, ".//div[@class='kt-post-card__description']")
            price_list = [price.text for price in prices]
            
        except:
            price_list = ['NETWORK ERROR']

        try:
            # get link
            link = good.get_attribute('href')
        except:
            link = 'NETWORK ERROR'
        goods_dict_3[title] = [price_list,link]

       # goods_dict_3[title] = {'prices': price_list, 'link': link}

  #  for title, data in goods_dict_3.items():
    #    print('Title:', title)
    #    print('Prices:', data['prices'])
     #   print('Link:', data['link'])
     #   print()

    return goods_dict_3

p = input()
goods_dict_asli={}
digikala(p)
sheypoor(p)
divar(p)
#make goods_dict_asli in this dictionary we have all 
goods_dict_asli.update(goods_dict)
goods_dict_asli.update(goods_dict_2)
goods_dict_asli.update(goods_dict_3)


def print_similar_keys(dictionary):
    keys = list(dictionary.keys())
    similar_keys = []

    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            if re.search(keys[i], keys[j]) or re.search(keys[j], keys[i]):
                similar_keys.append(keys[i])
                similar_keys.append(keys[j])

    if len(similar_keys) > 0:
        print("Similar keys found:")
        for i in range(0, len(similar_keys), 2):
            key1 = similar_keys[i]
            key2 = similar_keys[i + 1]
            value1 = dictionary[key1]
            value2 = dictionary[key2]
            print(f"{key1}: {value1}")
            print(f"{key2}: {value2}")
            print()
    else:
        print("No similar keys found.")


print_similar_keys(goods_dict_asli)








