from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options # add Options

from bs4 import BeautifulSoup as bs
import json
import time



profile_path = '/home/tester' # add path to Firefox 

options = Options() # create options object 

# add_argumenrs to the options 
options.add_argument('--no-sandbox') 
options.add_argument(f'--profile {profile_path}')
options.add_argument('--disable-dev-shm-usage')

service = Service('~/snap/firefox/2311') # change the path to match with yours 
driver = webdriver.Firefox(options=options ,service =service) # add options objects 

def scrap(url,class_element_name,class_element_color,class_element_price,class_element_size):
    driver.get(url)
    time.sleep(5)
    
    data = {}
    
    the_name = ''
    the_color = ''
    the_price = ''
    the_size = []

    content = driver.page_source

    soup = bs(content,features='lxml')

    for div in soup.findAll(class_=class_element_name):
        name = div.find("h1")
        for word in name:
            the_name += word
            
    for div in soup.findAll(class_=class_element_color):
        color = div.find('span')
        for col in color:
            the_color += col

    for div in soup.findAll(class_=class_element_price):
        price = div.find('span')
        for pri in price:
            for i in pri:
                if i != '£' and i != ' ':
                    the_price += i                    
            break
        break    
    the_price=float(the_price)    
    for div in soup.findAll(class_=class_element_size):
        size = div.find('span')
        for x in size:
            the_size.append(x)
    
    
    data['name'] = the_name
    data['price'] = the_price
    data['color'] = the_color
    data['size'] = the_size  
    
    with open('14-02-2023.json', mode='w') as f:
        json.dump(data,f)

scrap('https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99','product-features','product-colors','S5XGZ MZfYt','PL1La X4g20')



