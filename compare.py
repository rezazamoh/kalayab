# kalayab
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import digikala ,divar ,sheypoor
import re

def multi_search(link):
    p=link
    goods_dict_asli={}
    goods_dict  =digikala.scan(p)
    goods_dict_2=sheypoor.scan(p)
    goods_dict_3=divar.scan(p)
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
            return similar_keys
        else:
            return 0
    
def single_search(title):
    p = title
    goods_dict_2 = sheypoor.scan(p)
    goods_dict_3 = divar.scan(p)
    goods_dict_asli={}
    goods_dict_asli.update(goods_dict_2)
    goods_dict_asli.update(goods_dict_3)
    keys = list(goods_dict_asli.keys())

    similar_keys = []
    for i in range(len(keys)):
        if re.search(title, keys[i]) or re.search(keys[i], title):
            if re.search(r'\bdivar.ir\b',goods_dict_asli[keys[i]][1]):
                site = 'دیوار'
            else:
                site = 'شیپور'
            similar_keys.append([site,goods_dict_asli[keys[i]]])

    return similar_keys