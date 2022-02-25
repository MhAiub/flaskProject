import os
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import xlwt

# data = soup.find('a', {'class':"block-link__overlay-link"})

driver = webdriver.Chrome("/home/expo/.wdm/drivers/chromedriver/linux64/96.0.4664.45/chromedriver")

base_url = 'https://www.bbc.com/'
driver.get(base_url)
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

all_data = [data['href'] for data in soup.find_all('a', {'class': "block-link__overlay-link"})]

for link in all_data:
    link_url = 'https://www.bbc.com'
    query = link_url+link
    driver.get("https://www.bbc.com/future/article/20220223-the-chemical-that-sharpens-our-social-skills")
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    data = soup.find_all('p', {'class': "Normal1"})
    print(data)

# excel_data = {'Link': all_data, 'Name': 'BBC WEB LINKS'}
# df = pd.DataFrame(excel_data, columns=['Link', 'Name'])
# df.to_excel(r'/home/expo/Documents/bbc_wesite_links.xls', index=False, header=True)

