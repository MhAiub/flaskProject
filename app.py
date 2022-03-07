from bs4 import BeautifulSoup
from selenium import webdriver

# from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

update_link = 'https://www.bbc.com'
base_url = 'https://www.bbc.com/'
path = "/home/expo/.wdm/drivers/chromedriver/linux64/96.0.4664.45/chromedriver"

driver = webdriver.Chrome(executable_path=path)

driver.get(base_url)
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

links_1 = [data['href'] for data in soup.find_all('a', {'class': "block-link__overlay-link"})]
links_2 = [data['href'] for data in soup.find_all('a', {'class': "media__link"})]

links_1.extend(links_2)
head_li = []
desc_li = []

for link in links_1:
    try:
        if "https://www.bbc.com" in link:
            links = link
        else:
            links = update_link + link

        driver.get(links)
        html_source = driver.page_source
        soup_data = BeautifulSoup(html_source, 'html.parser')
        header_data = soup_data.find('h1')
        description_data = soup_data.find('p')

        if header_data and description_data:
            header = header_data.get_text()
            description = description_data.get_text()
            print(link)

            if header:
                header = header
                print('hhhh__',header)
            else:
                header = 'Not found'

            if description:
                description = description
                print('desc_________',description)
            else:
                description = 'Not found'

            head_li.append(header)
            desc_li.append(description)

            excel_data = {'Link': links_1, 'title': head_li, 'description': desc_li}
            df = pd.DataFrame(excel_data, columns=['Link', 'title', 'description'])
            import pdb;pdb.set_trace()
            df.transpose()
            df.to_excel(r'test_data.xlsx', index=False, header=True)

    except Exception as e:
        print(e)