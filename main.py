from cgi import FieldStorage
from xml.etree.ElementPath import xpath_tokenizer
import config as cf
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv

Path='/Users/prafu/OneDrive/Desktop/data analytics/Internship_datam/chromedriver_win32/chromedriver'

url='https://edalnice.cz/en/bulk-purchase/index.html#/multi_eshop/batch'
op = Options()

op.add_argument("--start-maximized") #open Browser in maximized mode
#op.add_argument("--no-sandbox") #bypass OS security model
op.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
op.add_experimental_option("excludeSwitches", ["enable-automation"])
op.add_experimental_option("excludeSwitches", ["enable-logging"])
op.add_experimental_option('useAutomationExtension', False)
op.headless = False

with  webdriver.Chrome(executable_path=Path, options=op) as d:
    d.get(url)
    time.sleep(5)
    d.find_element(by=By.CSS_SELECTOR,value=".refuseCookies").click()
    with open('sample.csv','r') as csv:
        lines=csv.readlines()
        #print(lines[0])
        a=[]
        for i in lines:
            a.append(i[:-1].split(','))
    for i in range(1,len(a)):
        ele=d.find_element(by=By.CSS_SELECTOR,value=".multi-eshop.jumbotron:last-child h3")
        d.execute_script('arguments[0].scrollIntoView()',ele)

        d.find_element(by=By.CSS_SELECTOR,value=".multi-eshop.jumbotron:last-child .react-select__input").send_keys(a[i][0])
        time.sleep(10)
        d.find_element(by=By.CSS_SELECTOR,value=".multi-eshop.jumbotron:last-child .react-select__option--is-focused").click()
        time.sleep(3)
        date=a[i][1]
        date=date[:6]+'20'+date[6:]
        d.find_element(by=By.CSS_SELECTOR,value=".multi-eshop.jumbotron:last-child .kit__input_datepicker").send_keys(date)
        time.sleep(3)
        d.find_element(by=By.CSS_SELECTOR,value=".multi-eshop.jumbotron:last-child .order-0").send_keys(a[i][2])
        time.sleep(3)
        if a[i][3]!='':
            d.find_element(by=By.CSS_SELECTOR,value=".multi-eshop.jumbotron:last-child .custom-control-input").click()
            time.sleep(3)
            if a[i][3] =="Natural Gas":
                d.find_element(by=By.CSS_SELECTOR,value=".multi-eshop.jumbotron:last-child .col-auto:nth-child(1)").click()
            elif a[i][3]=='Biomethane':
                d.find_element(by=By.CSS_SELECTOR,value=".multi-eshop.jumbotron:last-child .col-auto:nth-child(2)").click()
            time.sleep(3)
        if a[i][4]=="Annual":
            d.find_element(by=By.CSS_SELECTOR,value=".multi-eshop.jumbotron:last-child .form-group:nth-child(1) > .charge-view").click()
        elif a[i][4]=='30-day':
            d.find_element(by=By.CSS_SELECTOR,value=".multi-eshop.jumbotron:last-child .form-group:nth-child(2) > .charge-view").click()
        elif a[i][4]=='10-day':
            d.find_element(by=By.CSS_SELECTOR,value=".multi-eshop.jumbotron:last-child .form-group:nth-child(3) > .charge-view").click()
        time.sleep(3)
        if(i!=len(a)-1):
            d.find_element(by=By.CSS_SELECTOR,value=".multi-eshop.jumbotron:last-child .text-center .kit__button:last-child").click()
            time.sleep(5)
    ele=d.find_element(by=By.CSS_SELECTOR,value=".col-12 h3")
    d.execute_script('arguments[0].scrollIntoView()',ele)      
    d.find_element(by=By.CSS_SELECTOR,value=".kit__button.w-100").click()
    time.sleep(3)
    d.find_element(by=By.CSS_SELECTOR,value=".kit__button.w-100").click()
    time.sleep(3)
    ele=d.find_element(by=By.CSS_SELECTOR,value=".jumbotron .h3")
    d.execute_script('arguments[0].scrollIntoView()',ele)
    d.find_element(by=By.ID,value='email-input').send_keys(cf.EMAIL)
    time.sleep(3)
    d.find_element(by=By.ID,value='email-confirmation-input').send_keys(cf.EMAIL)
    time.sleep(3)
    d.find_element(by=By.ID,value='card_payment_radio_array_option').click()
    time.sleep(3)
    d.find_element(by=By.ID,value='_termsAgreement-true').click()
    time.sleep(3)
    d.find_element(by=By.CSS_SELECTOR,value=".kit__button.w-100").click()
    time.sleep(15)
    d.find_element(by=By.ID,value='cardnumber').send_keys(cf.CARD_NUMBER)
    time.sleep(3)
    d.find_element(by=By.ID,value='expiry').send_keys(cf.CARD_VALIDITY)
    time.sleep(3)
    d.find_element(by=By.ID,value='cvc').send_keys(cf.CARD_CVV)
    time.sleep(3)
