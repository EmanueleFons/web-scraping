from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
import smtplib #this one is to send a email alert

url = 'https://br.tradingview.com/symbols/BTCUSD/'

driver = webdriver.Chrome()
driver.get(url)
sleep (8)

price = driver.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[3]/div[1]/div/div/div/div[1]/div[1]')
pricetext = price.text

print (f'Sua cotação do bitcoin é: {pricetext}')

#send email 
def sendemail():
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('smtpbtc@gmail.com', )

    subject = 'O Bitcoin atigiu os 50k!'
    body = f'O bitcoin abou de atingir a cotação: {pricetext}'
    server.sendmail(
        'smtpbtc@gmail.com',
        subject,
        body
    )
    print('Email enviado')
    server.quit()

    if pricetext >= '50000.00':
        sendemail()
