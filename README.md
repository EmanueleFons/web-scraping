# web-scraping
Web Scraping Projects
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep

url ='https://www.coronatracker.com/pt-br'

driver = webdriver.Chrome()
driver.get(url)
sleep(5)
cases = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span')
casestext = cases.text

cure = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span')
curetext = cure.text

death=driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/span')
deathtext= death.text

print(f'Casos confirmados: {casestext}')
print (f'Curados: {curetext}')
print(f'Mortes confimadas: {deathtext}')
