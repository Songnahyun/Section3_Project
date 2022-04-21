import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

import pandas as pd

product = []
def Scrapping():
    driver = webdriver.Chrome('/Users/songnahyun/Section3_Project/chromedriver')
    for i in range(1,25):
        driver.get("https://www.glowpick.com/categories/" + str(i))
        driver.implicitly_wait(5)   
        driver.find_element_by_xpath('//*[@id="default-layout"]/div/div[1]/span/div/div[2]/div[2]/button[2]').click()
        ranking = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div/div/div[1]/div/div').find_elements_by_class_name('contents__ul__li')
        for i1 in ranking:
            item = {
                'Name' : str(i1.find_element_by_class_name('details__product').text),
                'brand' : str(i1.find_element_by_class_name('details__brand').text),
                'ratings' : float(i1.find_element_by_class_name('details__ratings').find_element_by_class_name('details__ratings__value').text),
                'volume_price' : str(i1.find_element_by_class_name('details__product__volume-price').text)
                }
            product.append(item)
    for i in range(32,66):
        driver.get("https://www.glowpick.com/categories/" + str(i))
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//*[@id="default-layout"]/div/div[1]/span/div/div[2]/div[2]/button[2]').click()
        ranking = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div/div/div[1]/div/div').find_elements_by_class_name('contents__ul__li')
        for i1 in ranking:
            items = {
                'Name' : str(i1.find_element_by_class_name('details__product').text),
                'brand' : str(i1.find_element_by_class_name('details__brand').text),
                'ratings' : float(i1.find_element_by_class_name('details__ratings').find_element_by_class_name('details__ratings__value').text),
                'volume_price' : str(i1.find_element_by_class_name('details__product__volume-price').text)
                }
            product.append(items)

    df = pd.DataFrame(product)
    print(df.shape)

    #csv파일로 저장
    df.to_csv("data1.csv")

Scrapping()
