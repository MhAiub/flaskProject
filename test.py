import os
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException


driver = webdriver.Chrome("/home/expo/.wdm/drivers/chromedriver/linux64/96.0.4664.45/chromedriver")

search_url='https://www.bbc.com/'
html_source = driver.page_source
driver.get(search_url)
import pdb;pdb.set_trace()


#Scroll to the end of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)#sleep_between_interactions
imgResults = driver.find_elements_by_xpath("/block-link__overlay-link")
totalResults=len(imgResults)
print(driver)
print(len(imgResults))



