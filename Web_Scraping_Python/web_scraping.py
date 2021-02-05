#!/usr/bin/env python
# coding: utf-8

# ## Web Scrapping

# #### 1. Write a Python program of your Top Ten favorite movies, the year of the movie and the synopsis. 

# In[8]:


from requests_html import HTMLSession
session = HTMLSession()
url='https://www.imdb.com/chart/top/'
r=session.get(url)

link=r.html.find('td.titleColumn a[href]')
movie_name =[link[i].text for i in range(len(link))]
url =[list(link[i].absolute_links) for i in range(len(link))]

year =r.html.find('td.titleColumn span')
year =[int(year[i].text.strip('()')) for i in range(len(year))]


from requests_html import AsyncHTMLSession
session=AsyncHTMLSession()
synopse=[]
for i in range(10):
    url_movie=url[i][0]
    r = await session.get(url_movie)
    await r.html.arender(timeout=10,sleep=10)

    syn=r.html.find('div.summary_text')
    synopse.append(syn[0].text)
    
import pandas as pd

movie_top10=pd.DataFrame()
movie_top10["Movie Name"] = movie_name[0:10]
movie_top10["Year"]=year[0:10]
movie_top10["Synopse"]=synopse

pd.set_option('display.max_colwidth',-1)
movie_top10


# #### 2.Write a Python program to find the live weather report (Temperature) in Tokyo, Osaka and Sapporo. 

# In[33]:


import requests
import json
API_key='1e1f1b7d456fc67d53e3a50216d65374'
city_list=list(input('list of city names:').split())
for city_name in city_list:
    url =('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city_name,API_key))

    response=requests.get(url)
    
    print("\nCity: {}".format(city_name))
    print("Temp:{} degC".format(response.json()['main']['temp']))
    print("Wind Speed:{} m/s".format(response.json()['wind']['speed']))
    print("Description:{}".format(response.json()['weather'][0]['description']))


# #### 3.Write a Python program to get the number of magnitude 5+ earthquakes detected worldwide by BGS.
# modified: 
# write a prog to get the data for recent earthquake world wide

# In[41]:


import pandas as pd

url='https://earthquakes.bgs.ac.uk/earthquakes/recent_world_events.html'
table = pd.read_html(url)
pd.set_option('display.max_colwidth',-1)
table[0]


# In[ ]:




