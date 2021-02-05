#!/usr/bin/env python
# coding: utf-8

# ### Data Scrapping Task

# #### 1.	Write a Python program to test if a given page is found or not on the server.

# In[101]:


import requests
def check_url(url):
    
    try:
        response=requests.get(url)
        #print(response.status_code)
        if response.status_code==200:
            return print('Connection Successful, Page Found')
        else:
            return False
    except Exception:
        return print('Connection Error, Page not Found')
            
check_url('https://www.bbc1.co.uk/news')
check_url('https://www.bbc.co.uk/news')


# #### 2.	Write a Python program to download and display the content of robot.txt for en.wikipedia.org

# In[30]:


import requests
url = 'https://en.wikipedia.org/robots.txt'
response = requests.get(url)
print(response.text)


# #### 3.	Write a Python program to get the number of datasets currently listed on data.gov
# 

# In[29]:


from requests_html import HTMLSession
session = HTMLSession()
r=session.get("http://www.data.gov")
links=r.html.find("a",containing="datasets")[0].text
print("Number of currnet dataset listed in data.gov are",links)


# #### 4.	Write a Python program to convert an address (like "1600 Amphitheatre Parkway, Mountain View, CA") into geographic coordinates (like latitude 37.423021 and longitude -122.083739).

# In[12]:


#pip install geopy
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="diwakarsharma238@gmail.com")

location = geolocator.geocode("1600 Amphitheatre Parkway, Mountain View, CA")
print('Given Address :')
print(location.address)
print("\nLatitude:{} \nLongitutude:{}".format(location.latitude, location.longitude))


# #### 6.	Write a Python program to extract h1 tag from example.com. 

# In[28]:


from requests_html import HTMLSession
session = HTMLSession()
r=session.get('http://www.example.com')
extract=r.html.find("h1")
extract[0].html


# #### 7.	Write a Python program to extract and display all the header tags from en.wikipedia.org/wiki/Main_Page.

# In[52]:


import requests
from bs4 import BeautifulSoup

response=requests.get('https://en.wikipedia.org/wiki/Main_Page')
html=response.content
soup = BeautifulSoup(html, "html.parser")
extract=soup.find_all(['h1','h2','h3','h4',',h5','h6'])
extract


# 
# #### 8.	Write a Python program to extract and display all the image links from en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer). 

# In[98]:


from requests_html import HTMLSession
session = HTMLSession()
r=session.get('https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)')
links=r.html.find("img")
image_links=[links[i].attrs['src'] for i in range(len(links))]
image_links


# #### 10	Write a Python program to that retrieves an arbitary Wikipedia page of "Python" and creates a list of links on that page.

# In[108]:


from requests_html import HTMLSession
session = HTMLSession()
r=session.get('https://en.wikipedia.org/wiki/Python')
links=r.html.absolute_links

print('Total link on webpage:',len(links))
links


# #### 11	Write a Python program to check whether a page contains a title or not. 

# In[79]:


def check_title(url):
    from requests_html import HTMLSession
    session = HTMLSession()
    r=session.get(url)
    link=r.html.find('title')
    
    #If link is a empty list then no title found
    if not link:
        return print('{} does not have a title'.format(url))
    else:    
        return print('{} has title: {}'.format(url, link[0].text))
    
check_title("http://www.data.gov")


# #### 12	Write a Python program to list all language names and number of related articles in the order they appear in wikipedia.org.

# In[ ]:





# In[169]:


from requests_html import HTMLSession
session = HTMLSession()
r=session.get('https://www.wikipedia.org/')
links=r.html.find('a.link-box')

lang_list=[links[i].text for i in range(len(links))]
for i in range(len(lang_list)):
    print(lang_list[i])


# #### 13	Write a Python program to get the number of people visiting a U.S. government website right now.
# ****Source: https://analytics.usa.gov/data/live/realtime.json
# 

# In[19]:


from requests_html import HTMLSession
session = HTMLSession()
url='https://analytics.usa.gov/data/live/realtime.json'
r=session.get(url)
j=r.json()
print('No of active users on webpage {} are {}'.format(url,j['data'][0]['active_visitors']))


# #### 14	Write a Python program get the number of security alerts issued by US-CERT in the current year. 
# Source: https://www.us-cert.gov/ncas/alerts
# 

# In[78]:


def alert_year(year):
    from requests_html import HTMLSession
    session = HTMLSession()
    total_alert=0
    
    #loop for all the pages for given year
    for Page in range(5):
        url=('https://us-cert.cisa.gov/ncas/alerts/{}?page={}'.format(year,Page))
        r=session.get(url)
        link=r.html.find('.view-content span')
        a=[link[i].text for i in range(len(link))]
        if len(a)==0:
            break
        total_alert =total_alert+len(a)
    return print('Total alert for year {} are {}'.format(year,total_alert))

alert_year(2021)


# #### 15	 Write a Python program to get the number of Pinterest accounts maintained by U.S. State Department embassies and missions. 
# ****Source: https://www.state.gov/r/pa/ode/socialmedia/
# 

# ********* Website not reachable  skipping question *************

# #### 16	Write a Python program to get the number of followers of a given twitter account.

# In[1]:



from requests_html import AsyncHTMLSession
session=AsyncHTMLSession()
account_name='BorisJohnson'
url=('https://twitter.com/{}'.format(account_name))
r = await session.get(url)
await r.html.arender(timeout=5,sleep=5)
links=r.html.find('[href*=follower]')
print('Number of follower for twitter account {} are {}'.format(account_name,links[0].text))


# In[198]:


import requests
from bs4 import BeautifulSoup
url='https://twitter.com/narendramodi'

response=requests.get(url)
html=response.content
soup = BeautifulSoup(html,'html.parser')
with open('twitter.html', 'wb') as file:
    file.write(soup.prettify('utf-8'))
a=soup.find_all('[dir]')
a


# #### 17	Write a Python program to get the number of following on Twitter.
# 

# In[2]:


from requests_html import AsyncHTMLSession
session=AsyncHTMLSession()
account_name='BorisJohnson'
url=('https://twitter.com/{}'.format(account_name))
r = await session.get(url)
await r.html.arender(timeout=5,sleep=5)
links=r.html.find('[href*=following]')
print('Number of following for twitter account {} are {}'.format(account_name,links[0].text))


# #### 18	 Write a Python program to get the number of post on Twitter liked by a given account. 

# #### 19	 Write a Python program to count number of tweets by a given Twitter account.

# In[3]:


from requests_html import AsyncHTMLSession
session=AsyncHTMLSession()
account_name='BorisJohnson'
url=('https://twitter.com/{}'.format(account_name))
r = await session.get(url)
await r.html.arender(timeout=5,sleep=5)
links=r.html.find('[dir=auto]')
links[11].text


# In[ ]:




