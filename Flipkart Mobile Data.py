# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 17:51:32 2022

@author: Thakral's
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

final = pd.DataFrame()

for j in range(1,11):
    
    url = 'https://www.flipkart.com/search?q=smartphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={}'.format(j)
    
    webpage = requests.get(url).text
    soup = BeautifulSoup(webpage,'lxml') 
    
    container = soup.find_all('div' , class_='_2kHMtA')
    
    title = []
    rating = []
    feature_1 = []
    price = []
    features = []
    
    for i in container:
        
        title.append(i.find('div' , class_='_4rR01T').text.strip())
        

    for i in container:
        
        feature_1.append(i.find('li', class_='rgWa7D').text.strip())
        
        
    for i in container:
        
        rating.append(i.find('div' , class_='gUuXy-').text.strip())
        
        
        
    for i in container:
        
        price.append(i.find('div' , class_='_30jeq3 _1_WHN1').text.strip())    
        
        
        
    for i in container:
        
        features.append(i.find('ul' , class_='_1xgFaf').text)
        
        
    d = {'Name':title , 'Rating':rating , 'Features':features , 'Price':price}

    df = pd.DataFrame(d)

    final = final.append(df,ignore_index=True)    