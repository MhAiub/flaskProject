from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time

update_link = 'https://www.bbc.com'
base_url = 'https://www.bbc.com/'
path = "/home/expo/.wdm/drivers/chromedriver/linux64/96.0.4664.45/chromedriver"

driver = webdriver.Chrome(executable_path=path)

driver.get(base_url)
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

links_1 = [data['href'] for data in soup.find_all('a', {'class': "block-link__overlay-link"})]
links_2 = [data['href'] for data in soup.find_all('a', {'class': "media__link"})]
delay = 1 # seconds

links_1.extend(links_2)
head_li = []
desc_li = []
lin_li = []

for link in links_1:
    try:
        if "https://www.bbc.com" in link:
            links = link
        else:
            links = update_link + link
        time.sleep(3)
        print('i am sleeping')
        driver.get(links)
        html_source = driver.page_source
        soup_data = BeautifulSoup(html_source, 'html.parser')
        header_data = soup_data.find('h1')
        description_data = soup_data.find('p')

        if header_data and description_data:
            header = header_data.get_text()
            description = description_data.get_text()

            if header:
                header = header
            else:
                header = 'Not found'

            if description:
                description = description
            else:
                description = 'Not found'

            head_li.append(header)
            desc_li.append(description)
            lin_li.append(links)

        excel_data = {'Link': lin_li, 'title': head_li, 'description': desc_li}
        df = pd.DataFrame(excel_data, columns=['Link', 'title', 'description'])
        df.transpose()
        df.to_excel(r'test_data.xlsx', index=False, header=True)

    except Exception as e:
        print(e)