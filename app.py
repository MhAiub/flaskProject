from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


path = "C:\\Users\\AYSHA\\.wdm\\drivers\\chromedriver\\win32\\98.0.4758.102\\chromedriver"

# data = soup.find('a', {'class':"block-link__overlay-link"})

link_url = 'https://www.bbc.com'
driver = webdriver.Chrome(path)

base_url = 'https://www.bbc.com/'
driver.get(base_url)
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

links_1 = [data['href'] for data in soup.find_all('a', {'class': "block-link__overlay-link"})]
links_2 = [data['href'] for data in soup.find_all('a', {'class': "media__link"})]



print('_____________________ Entering for loap -------------------')
for link in links_1:
    try:
        if "https://www.bbc.com" in link:
            query = link
        else:
            query = link_url+link
        
        driver.get(query)
        html_source = driver.page_source
        soup_data = BeautifulSoup(html_source, 'html.parser')

    except Exception as e:
        print(e)
            

      
for link_t in links_2:
    try:
        if "https://www.bbc.com" in link_t:
            query = link_t
        else:
            query = link_url+link_t
        print('_____________________ Entering for data -------------------')
        driver.get(query)
        html_source = driver.page_source
        soup_data = BeautifulSoup(html_source, 'html.parser')
    except Exception as e:
        print(e)
    
    
headers = soup_data.find_all('h1', {'class': "ssrcss-gcq6xq-StyledHeading e1fj1fc10"})
descriptions = soup_data.find_all('p', {'class': "ssrcss-1q0x1qg-Paragraph eq5iqo00"})

if headers:
    header = headers
else:
    header = 'no data found'

if descriptions:
    description = descriptions
else:
    descriptions = 'no data found'





header = [data for data in soup_data.find_all('h1', {'class': "ssrcss-gcq6xq-StyledHeading e1fj1fc10"})] # Getting all the header 

description = [data for data in soup_data.find_all('p', {'class': "ssrcss-1q0x1qg-Paragraph eq5iqo00"})]



excel_data = {'Link': links_1, 'link_2': links_2, 'title':header,'description': description  }
df = pd.DataFrame(excel_data, columns=['Link', 'link_2', 'title', 'description' ])
df.to_excel(r'test_data.xlsx', index=False, header=True)
