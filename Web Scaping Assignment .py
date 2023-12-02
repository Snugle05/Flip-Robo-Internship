#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# #### 1) Write a python program to display all the header tags from wikipedia.org and make data frame.

# In[4]:


url = "https://en.wikipedia.org/wiki/Main_Page"
r = requests.get(url)
print(r)


# In[5]:


Soup = BeautifulSoup(r.text,"lxml")
Soup


# In[6]:


Headers = []
for i in Soup.find_all("h2",class_="mp-h2"):
    Headers.append(i.text)
Headers


# In[7]:


df = pd.DataFrame({'Headers': Headers})
print(df)


# #### 2) Write s python program to display list of respected former presidents of India(i.e. Name , Term ofoffice)
# from https://presidentofindia.nic.in/former-presidents.htm and make data frame.

# In[8]:


url = "https://presidentofindia.nic.in/former-presidents"
r = requests.get(url)
print(r)


# In[10]:


soup = BeautifulSoup(r.text,'lxml')
soup


# In[12]:


Name_Term = []
for i in soup.find_all('div',class_="desc-sec"):
    Name_Term.append(i.text.replace("\n",""))
    
Name_Term


# In[13]:


df = pd.DataFrame({'Name_Term':Name_Term})
df


# #### 3) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# b) Top 10 ODI Batsmen along with the records of their team andrating.
# c) Top 10 ODI bowlers along with the records of their team andrating.

# In[20]:


# a) Top 10 ODI Teams in men's cricket

url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
r = requests.get(url)
print(r)


# In[21]:


Soup = BeautifulSoup(r.text,"lxml")
print(Soup)


# In[23]:


table = Soup.find('table', class_='table')
table


# In[24]:


# Initialize lists to store the data
teams = []
matches = []
points = []
ratings = []

for row in table.find_all('tr')[1:11]:  # Skip the header row and limit to the top 10 teams
    columns = row.find_all('td')
    if len(columns) == 5:
        team = columns[1].get_text(strip=True)
        match = columns[2].get_text(strip=True)
        point = columns[3].get_text(strip=True)
        rating = columns[4].get_text(strip=True)
        teams.append(team)
        matches.append(match)
        points.append(point)
        ratings.append(rating)


# In[25]:


df = pd.DataFrame({'Team': teams, 'Matches': matches, 'Points': points, 'Rating': ratings})
print(df)


# In[67]:


# b) Top 10 ODI Batsmen along with the records of their team and rating.

url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting"
r = requests.get(url)
print(r)


# In[68]:


soup = BeautifulSoup(r.text, 'lxml')
soup


# In[75]:


Positions = []
for i in soup.find_all('span',class_="rankings-table__pos-number")[:10]:
    Positions.append(i.text.replace("\n",""))
    
Positions


# In[77]:


Players = []
for i in soup.find_all('td',class_="table-body__cell rankings-table__name name")[:10]:
    Players.append(i.text.replace("\n",""))
Players


# In[79]:


Team = []
for i in soup.find_all('span',class_="table-body__logo-text")[:10]:
    Team.append(i.text)
Team


# In[80]:


Ratings = []
for i in soup.find_all('td',class_="table-body__cell rating")[:10]:
    Ratings.append(i.text)
Ratings


# In[82]:


df = pd.DataFrame({'Positions': Positions, 'Players': Players, 'Team': Team, 'Ratings': Ratings})
print(df)


# In[83]:


# c) Top 10 ODI bowlers along with the records of their team andrating.

url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling"
r = requests.get(url)
print(r)


# In[85]:


soup = BeautifulSoup(r.text,'lxml')
soup


# In[87]:


Positions = []
for i in soup.find_all('span',class_="rankings-table__pos-number")[:10]:
    Positions.append(i.text.replace("\n",""))
    
Positions


# In[88]:


Players = []
for i in soup.find_all('td',class_="table-body__cell rankings-table__name name")[:10]:
    Players.append(i.text.replace("\n",""))
Players


# In[89]:


Team = []
for i in soup.find_all('span',class_="table-body__logo-text")[:10]:
    Team.append(i.text)
Team


# In[91]:


Ratings = []
for i in soup.find_all('td',class_="table-body__cell rating")[:10]:
    Ratings.append(i.text)
Ratings


# In[93]:


df = pd.DataFrame({'Positions': Positions, 'Players': Players, 'Team': Team, 'Ratings': Ratings})
print(df)


# #### 4) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[36]:


# a) 

url = "https://www.icc-cricket.com/rankings/womens/team-rankings/odi"
r = requests.get(url)
print(r)


# In[37]:


soup = BeautifulSoup(r.text, 'lxml')
soup


# In[38]:


table = soup.find('table', class_='table')
table


# In[39]:


# Initialize lists to store the data
teams = []
matches = []
points = []
ratings = []

for row in table.find_all('tr')[1:11]:  # Skip the header row and limit to the top 10 teams
    columns = row.find_all('td')
    if len(columns) == 5:
        team = columns[1].get_text(strip=True)
        match = columns[2].get_text(strip=True)
        point = columns[3].get_text(strip=True)
        rating = columns[4].get_text(strip=True)
        teams.append(team)
        matches.append(match)
        points.append(point)
        ratings.append(rating)


# In[40]:


df = pd.DataFrame({'Team': teams, 'Matches': matches, 'Points': points, 'Rating': ratings})
print(df)


# #### 5) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and
# make data frame
# i) Headline
# ii) Time
# iii) News Link

# In[41]:


url = "https://www.cnbc.com/world/?region=world"
r = requests.get(url)
print(r)


# In[42]:


soup = BeautifulSoup(r.text,"lxml")
soup


# In[43]:


# i) Heading

Headings = []
for i in soup.find_all('div',class_="RiverHeadline-headline RiverHeadline-hasThumbnail"):
    Headings.append(i.text)
Headings


# In[44]:


df = pd.DataFrame({'Headings':Headings})
df


# In[65]:


# ii) Time

Time = []
for i in soup.find_all('span',class_="RiverByline-datePublished"):
    Time.append(i.text)
    
Time


# In[ ]:


# iii) News Link

News_link = []
for i in soup.find_all():
    News_link
News_link


# #### 6) Write a python program to scrape the details of most downloaded articles from AI in last 90
# days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
# Scrape below mentioned details and make data frame
# 
# i) Paper Title
# ii) Authors
# iii) Published Date
# iv) Paper URL

# In[49]:


url = "https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"
r = requests.get(url)
r


# In[50]:


soup = BeautifulSoup(r.text,"lxml")
soup


# In[51]:


# i) Paper Title 

Title = []
for i in soup.find_all('h2',class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    Title.append(i.text)
Title


# In[52]:


# ii) Author 

Author = []
for i in soup.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    Author.append(i.text)
Author


# In[53]:


# iii) Published Date 

Date = []
for i in soup.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    Date.append(i.text)
Date


# In[64]:


# iv) Paper URL

URL = []
for i in soup.find_all('a', class_='c-article-title-link'):
    URL.append(i[data-SRC])
URL


# In[55]:


df = pd.DataFrame({'Title':Title,'Author':Author,'Date':Date})
df


# #### 7) Write a python program to scrape mentioned details from dineout.co.inand make data frame
# 
# i) Restaurant name
# ii) Cuisine
# iii) Location
# iv) Ratings
# v) Image URL

# In[56]:


url = "https://www.dineout.co.in/delhi-restaurants/buffet-special"
r = requests.get(url)
r


# In[57]:


soup = BeautifulSoup(r.text,"lxml")
soup


# In[58]:


# i) Restaurant Name

Name = []
for i in soup.find_all('a',class_="restnt-name ellipsis"):
    Name.append(i.text)
Name


# In[59]:


# ii) Cuisine

Cuisine = []
for i in soup.find_all('span',class_="double-line-ellipsis"):
    Cuisine.append(i.text)
Cuisine


# In[60]:


# iii) Location

Location = []
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    Location.append(i.text)
Location


# In[61]:


# iv) Ratings

Ratings = []
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    Ratings.append(i.text)
Ratings


# In[62]:


# v) Image URL

Image_url = []
for i in soup.find_all('img',class_="no-img"):
    Image_url.append(i['data-src'])
    
Image_url


# In[63]:


df = pd.DataFrame({'Name':Name,'Cuisine':Cuisine,'Location':Location,'Ratings':Ratings,'Image_url':Image_url})
df


# In[ ]:




