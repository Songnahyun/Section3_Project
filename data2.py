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

products = []
def Scrapping():
    driver = webdriver.Chrome('/Users/songnahyun/Section3_Project/chromedriver')
    for i in range(1,25):
        driver.get(f"https://www.glowpick.com/categories/{i}?tab=review")
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//*[@id="default-layout"]/div/div[1]/span/div/div[2]/div[2]/button[2]').click()
        review = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div/div/div[2]/div/ul').find_elements_by_class_name('reviews__list__item')
        for i1 in review:
            item = {
                'Age' : str(i1.find_elements_by_class_name('property__wrapper__item')[0].text),
                'type' : str(i1.find_elements_by_class_name('property__wrapper__item')[1].text),
                'gender' : str(i1.find_elements_by_class_name('property__wrapper__item')[2].text),
                'brand' : str(i1.find_elements_by_tag_name('p')[1].text),
                'Name' : str(i1.find_elements_by_tag_name('p')[2].text),
                'rating' : int(i1.find_elements_by_class_name('stars__rating')[0].text)
             }
            products.append(item)
    
    for i in range(32, 66):
        driver.get(f"https://www.glowpick.com/categories/{i}?tab=review")
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//*[@id="default-layout"]/div/div[1]/span/div/div[2]/div[2]/button[2]').click()
        review = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div/div/div[2]/div/ul').find_elements_by_class_name('reviews__list__item')
        for i1 in review:
            items = {
                'Age' : str(i1.find_elements_by_class_name('property__wrapper__item')[0].text),
                'type' : str(i1.find_elements_by_class_name('property__wrapper__item')[1].text),
                'gender' : str(i1.find_elements_by_class_name('property__wrapper__item')[2].text),
                'brand' : str(i1.find_elements_by_tag_name('p')[1].text),
                'Name' : str(i1.find_elements_by_tag_name('p')[2].text),
                'rating' : int(i1.find_elements_by_class_name('stars__rating')[0].text)
             }
            products.append(items)
        
    df2 = pd.DataFrame(products)
    print(df2.head())
    df2.to_csv("data2.csv")

Scrapping()
