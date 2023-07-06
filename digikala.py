from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os ,shutil

def open(url):
    #starting driver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option('detach',True)
    driver = webdriver.Chrome("chromedriver.exe",options=options)
    driver.get(url)

def scan(searched):   
    #starting driver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome("chromedriver.exe",options=options)
    driver.get('https://www.digikala.com/search/?q='+ searched)
        
    #the section that goods are in there
    section = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME,'section')))
    time.sleep(2)

    #finding goods
    try:
        goods = section.find_elements(By.TAG_NAME,'a')
    except:
        return {} #no results
    
    driver.execute_script("arguments[0].scrollIntoView();", goods[-1])
    time.sleep(8)
    try:
        shutil.rmtree('/temp', ignore_errors=True)
    except:
        os.mkdir('temp')
    goods_dict = {}
    
    i = 0
    for i,good in enumerate(goods):

        try:
            #find title
            title = good.find_element(By.TAG_NAME,'h3').text
        except:
            title = ''
        try:
            #get_image
            img = good.find_element(By.XPATH,'./img[@class="w-100 radius-medium d-inline-block ls-is-cached lazyloaded"]')
            img.screenshot(f'temp/{i}.png')
        except:
            good.screenshot(f'temp/{i}.png')
                    
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

def itemscanner(link):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome("chromedriver.exe",options=options)
    driver.get(link)
    
    #screenshot good image
    good_section = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//div[@class="px-5-lg"]')))
    image =  WebDriverWait(good_section,5).until(EC.presence_of_element_located((By.XPATH,'//img[@style="width: 100%; height: auto; display: block; pointer-events: none;"]')))
    image.screenshot('good.png')

    #category
    cat = good_section.find_elements(By.XPATH,'.//a[@class="color-500 text-body-2 shrink-0"]')[-1]

    #more info 
    info_sec = WebDriverWait(good_section,5).until(EC.presence_of_element_located((By.XPATH,'//section[@class="mt-4-lg px-5 px-0-lg pb-5 styles_PdpProductContent__sectionBorder__39zAX"]')))
    driver.execute_script("arguments[0].scrollIntoView();", info_sec)
    time.sleep(1)
    driver.execute_script("arguments[0].scrollIntoView();", info_sec)
    time.sleep(3)
    try:
        buttons =  WebDriverWait(info_sec,5).until(EC.presence_of_all_elements_located((By.XPATH,'./span[@class="d-inline-flex ai-center pointer styles_Anchor--secondary__3KsgY text-button-2"]')))
        for button in buttons:
            if button.text == 'مشاهده بیشتر':
                try:
                    button.click()
                    break
                except:
                    pass
    except:
        pass
    time.sleep(1)
    info = {}

    try:
        cdiv1 = info_sec.find_element(By.XPATH,'./div[@class="mt-4 grow-1"]')
        cdiv2 = cdiv1.find_element(By.XPATH,'./div[@class="d-flex flex-column flex-row-lg pb-6 py-4-lg styles_SpecificationBox__main__JKiKI"]')
        cdiv3 = cdiv2.find_element(By.XPATH,'./div[@class="w-full w-auto-lg grow-1"]')
        blocks = cdiv3.find_elements(By.XPATH,'./div[@class="w-full d-flex last styles_SpecificationAttribute__valuesBox__gvZeQ"]')
    except: 
        cdiv2 = driver.find_element(By.XPATH,'//div[@class="d-flex flex-column flex-row-lg pb-6 py-4-lg styles_SpecificationBox__main__JKiKI"]')
        cdiv3 = cdiv2.find_element(By.XPATH,'./div[@class="w-full w-auto-lg grow-1"]')
        blocks = cdiv3.find_elements(By.XPATH,'./div[@class="w-full d-flex last styles_SpecificationAttribute__valuesBox__gvZeQ"]')

    for block in blocks:
        title = block.find_element(By.XPATH,'./p[@class="ml-4 text-body-1 color-500 py-2 py-3-lg p-2-lg shrink-0 styles_SpecificationAttribute__value__CQ4Rz"]')
        values = block.find_element(By.TAG_NAME,'div')
        info[title]=values
    return (cat,info)