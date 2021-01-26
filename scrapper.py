from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome('C:/Users/User/Desktop/dokument/class/127/chromedriver')
browser.get(start_url)

time.sleep(10)

def scrape():
    headers = ['name', 'light_years_from_earth', 'planet_mass', 'stellar_magnitude', 'discovery_data']
    planet_data = []
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        for ul_tag in soup.find_all('ul', attrs = {'class', 'exoplanet'}):
            li_tag = ul_tag.find_all('li')
            temp_list = []

            for index, li_tag in enumerate(li_tag):
                if index == 0:
                    temp_list.append(li_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append('')
        
            planet_data.append(temp_list)
        
        browser.find_element_by_xpath('//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()
    
    with open('data.csv', 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(planet_data)
        

scrape()

