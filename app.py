import os
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import xlwt


# data = soup.find('a', {'class':"block-link__overlay-link"})

link_url = 'https://www.bbc.com'
driver = webdriver.Chrome(ChromeDriverManager().install())

base_url = 'https://www.bbc.com/'
driver.get(base_url)
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

links_1 = [data['href'] for data in soup.find_all('a', {'class': "block-link__overlay-link"})]
links_2 = [data['href'] for data in soup.find_all('a', {'class': "media__link"})]

for link in links_1:
    if "https://www.bbc.com" in link:
        query = link_url
    else:
        
        query = link_url+link

    driver.get(query)
    html_source = driver.page_source
    soup_data = BeautifulSoup(html_source, 'html.parser')
    

for link_ in links_2:
    
    if "https://www.bbc.com" in link:
        query = link_url
    else:
        query = link_url+link
        
    driver.get(query)
    html_source = driver.page_source
    soup_data = BeautifulSoup(html_source, 'html.parser')
    
#header = soup_data.find_all('h1', {'class': "ssrcss-gcq6xq-StyledHeading e1fj1fc10"})
#description = soup_data.find_all('p', {'class': "ssrcss-1q0x1qg-Paragraph eq5iqo00"}) if description else 'no data found'


header = [data for data in soup_data.find_all('h1', {'class': "ssrcss-gcq6xq-StyledHeading e1fj1fc10"})] # Getting all the header 

description = [data for data in soup_data.find_all('p', {'class': "ssrcss-1q0x1qg-Paragraph eq5iqo00"})]



excel_data = {'Link': link_1, 'link_2': link_2, 'title':header, 'description':description,  }
df = pd.DataFrame(excel_data, columns=['Link', 'link_2', 'title', 'description' ])
df.to_excel(r'test_data.xlsx', index=False, header=True)

