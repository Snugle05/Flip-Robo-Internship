#!/usr/bin/env python
# coding: utf-8

#  1. Write a python program which searches all the product under a particular product from www.amazon.in. The
# product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search for
# guitars. 

# In[80]:


import time
from selenium import webdriver
import selenium
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


# In[81]:


driver = webdriver.Chrome()


# In[82]:


val=input("enter your item: ")


# 2. In the above question, now scrape the following details of each product listed in first 3 pages of your search
# results and save it in a data frame and csv. In case if any product has less than 3 pages in search results then
# scrape all the products available under that product name. Details to be scraped are: "Brand
# Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and
# “Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“. 

# In[83]:


driver.get("https://www.amazon.in/")
time.sleep(3)


# In[84]:


Input=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
Input.send_keys("guitars")


# In[85]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
search.click()


# In[89]:


# Scrap all product url's

product_urls=[]
start=0
end=3
for page in range(start,end):
    url=driver.find_elements(By.XPATH,'//a[@class= "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in url:
        product_urls.append(i.get_attribute("href"))
    nxt_button=driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
    nxt_button.click()
    time.sleep(2)


# In[90]:


len(product_urls)


# In[ ]:


for url in product_urls:
    driver.get(url)
    time.sleep(2)
    
    try:
        brand= driver.find_element(By.XPATH,'//*[@id="productOverview_feature_div"]/div/table/tbody/tr[1]/td[2]/span')
        Brand.append(brand.text)
    except NoSuchElementException:
        Brand.append('-')
    


# 3. Write a python program to access the search bar and search button on images.google.com and scrape 10
# images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’. 

# In[94]:


driver = webdriver.Chrome()


# In[95]:


driver.get("https://images.google.com/")
time.sleep(3)


# In[96]:


Input=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
Input.send_keys("cake")


# In[99]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button/div/span")
search.click()


# In[100]:


for _ in range(20):
    driver.execute_script("window.scrollBy(0,700)")
    
images = driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')

img_urls=[]
for image in images:
    source= image.get_attribute('src')
    if source is not None:
        if (source[0:4] == 'http'):
            img_urls.append(source)
                           


# In[ ]:


for i in range(len(img_urls)):
    if i > 10:
        breakBy.XPATH,
    print("Downloading {0} of {1} images" .format(i, 10))
    response=requests.get(img_urls[i])
    file = open(r"/Users/adityasharma/Downloads"+str(i)+".jpg","wb")
    file.write(response.content)


# 4. Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com
# and scrape following details for all the search results displayed on 1st page. Details to be scraped: “Brand
# Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”,
# “Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the
# details is missing then replace it by “- “. Save your results in a dataframe and CSV. 

# In[108]:


driver = webdriver.Chrome()


# In[109]:


driver.get("https://www.flipkart.com/")
time.sleep(3)


# In[110]:


Input=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[1]/div[2]/form/div/div/input")
Input.send_keys("smart phone")


# In[112]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[1]/div[2]/form/div/button")
search.click()


# In[113]:


# Scrap all product url's

product_urls=[]
start=0
end=3
for page in range(start,end):
    url=driver.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
    for i in url:
        product_urls.append(i.get_attribute("href"))
    nxt_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    nxt_button.click()
    time.sleep(2)


# In[114]:


len(product_urls)


# In[115]:


open_link=driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]")
open_link.click()


# In[118]:


Brand=[]
for url in product_urls:
    driver.get(url)
    time.sleep(2)
    
    try:
        brand= driver.find_element(By.XPATH,'//*[@id="B_NuCI"]/div/table/tbody/tr[1]/td[2]/span')
        Brand.append(brand.text)
    except NoSuchElementException:
        Brand.append('-')
    


# In[119]:


Colour=[]
for url in product_urls:
    driver.get(url)
    time.sleep(2)
    
    try:
        colour= driver.find_element(By.XPATH,'//*[@id="_21lJbe"]/div/table/tbody/tr[1]/td[2]/span')
        Colour.append(colour.text)
    except NoSuchElementException:
        Colour.append('-')
    


# In[120]:


Ram=[]
Storage=[]
Primary_camera=[]
Secondary_camera=[]
Display_size=[]
Battery_capacity=[]

for url in product_urls:
    driver.get(url)
    time.sleep(2)
    
    try:
        ram= driver.find_element(By.XPATH,'//*[@id="_1q8vHb"]/div/table/tbody/tr[1]/td[2]/span')
        Ram.append(ram.text)
    except NoSuchElementException:
        Ram.append('-')
    try:
        storage= driver.find_element(By.XPATH,'//*[@id="_1q8vHb"]/div/table/tbody/tr[1]/td[2]/span')
        Storage.append(storage.text)
    except NoSuchElementException:
        Storage.append('-')
    try:
        primary_camera= driver.find_element(By.XPATH,'//*[@id="_21Ahn-"]/div/table/tbody/tr[1]/td[2]/span')
        Primary_camera.append(primary_camera.text)
    except NoSuchElementException:
        Primary_camera.append('-')
    try:
        secondary_camera= driver.find_element(By.XPATH,'//*[@id="_21Ahn-"]/div/table/tbody/tr[1]/td[2]/span')
        Secondary_camera.append(secondary_camera.text)
    except NoSuchElementException:
        Secondary_camera.append('-')
    try:
        display_size= driver.find_element(By.XPATH,'//*[@id="_21Ahn-"]/div/table/tbody/tr[1]/td[2]/span')
        Display_size.append(display_size.text)
    except NoSuchElementException:
        Display_size.append('-')
    try:
        battery_capacity= driver.find_element(By.XPATH,'//*[@id="_21Ahn-"]/div/table/tbody/tr[1]/td[2]/span')
        Battery_capacity.append(battery_capacity.text)
    except NoSuchElementException:
        Battery_capacity.append('-')


# In[121]:


df = pd.DataFrame({"Brand":Brand,"Colour":Colour,"Ram":Ram,"Storage":Storage,"Primary_camera":Primary_camera,"Secondary_camera":Secondary_camera,"Display_size":Display_size,"Battery_capacity":Battery_capacity})
df


# In[122]:


df.to_csv("flipkart_product_data.csv", index=False)


# In[123]:


driver.quit()


# 5. Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps. 

# In[124]:


driver = webdriver.Chrome()


# In[125]:


driver.get("https://www.google.com/maps/")
time.sleep(3)


# In[126]:


Input=driver.find_element(By.XPATH,"/html/body/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/form/input")
Input.send_keys("delhi")


# In[127]:


search=driver.find_element(By.XPATH,"/html/body/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/div[1]/button")
search.click()


# In[128]:


try:
    url = driver.current_url
    parts = url.split('@')[1].split(',')
    latitude = parts[0]
    longitude = parts[1]
    print(f"Latitude: {latitude}, Longitude: {longitude}")
except Exception as e:
    print("Error: Unable to extract coordinates.")
    print(e)


# In[129]:


driver.quit()


# 6. Write a program to scrap all the available details of best gaming laptops from digit.in. 

# In[135]:


driver = webdriver.Chrome()


# In[136]:


driver.get("https://www.digit.in/top-products/top-10-laptops-5.html")
time.sleep(3)


# In[137]:


Laptop_name=[]
laptop_name=driver.find_elements(By.XPATH,'//h3[@class="font130 mt0 mb10 mobilesblockdisplay "]')
for i in laptop_name:
    name=i.text
    Laptop_name.append(name)


# In[144]:


df=pd.DataFrame({"Laptop_name":Laptop_name})
df


# In[154]:


driver.quit()


# 7. Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped:
# “Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”. 

# In[155]:


driver = webdriver.Chrome()


# In[156]:


driver.get("https://www.forbes.com/billionaires/")
time.sleep(3)


# In[169]:


ranks = []
names = []
net_worths = []
ages = []
citizenships = []
sources = []
industries = []


# In[174]:


billionaire_elements = driver.find_elements(By.XPATH,'//div[@class="Table_rank___YBhk Table_dataCell__2QCve"]')
for element in billionaire_elements:
    rank = element.text
    ranks.append(rank)

name_elements = driver.find_elements(By.XPATH,'//div[@class="Table_dataCell__2QCve"]')
for element in name_elements:
    name = element.text
    names.append(name)

net_worth_elements = driver.find_elements(By.XPATH,'//div[@class="Table_netWorth___L4R5 Table_dataCell__2QCve"]')
for element in net_worth_elements:
    net_worth = element.text
    net_worths.append(net_worth)

age_elements = driver.find_elements(By.XPATH,'//div[@class="Table_dataCell__2QCve"]')
for element in age_elements:
    age = element.text
    ages.append(age)

citizenship_elements = driver.find_elements(By.XPATH,'//div[@class="TableRow_cell__db-hv Table_cell__houv9"]')
for element in citizenship_elements:
    citizenship = element.text
    citizenships.append(citizenship)

source_elements = driver.find_elements(By.XPATH,'//div[@class="TableRow_cell__db-hv Table_cell__houv9"]')
for element in source_elements:
    source = element.text
    sources.append(source)

industry_elements = driver.find_elements(By.XPATH,'//div[@class="Table_dataCell__2QCve"]')
for element in industry_elements:
    industry = element.text
    industries.append(industry)


# In[176]:


df=pd.DataFrame({"Rank": ranks[:150],"Name": names[:150],"Net worth": net_worths[:150],"Age": ages[:150],"Citizenship": citizenships[:150],"Source": sources[:150],"Industry": industries[:150]})
df


# In[177]:


driver.quit()


# 8. Write a program to extract at least 500 Comments, Comment upvote and time when comment was posted
# from any YouTube Video.

# In[178]:


driver = webdriver.Chrome()


# In[179]:


driver.get("https://www.youtube.com/watch?v=hlGoQC332VM")
time.sleep(3)


# In[182]:


for _ in range (500):
    driver.execute_script("window.scrollBy(0,500)")
    
comment_elements = driver.find_elements(By.XPATH, '//yt-formatted-string[@id="content-text"]')


# In[183]:


comments = []
upvotes = []
timestamps = []

for element in comment_elements:
    comment = element.text
    comments.append(comment)

upvote_elements = driver.find_elements(By.XPATH, '//span[@id="vote-count-middle"]')
for element in upvote_elements:
    upvote = element.text
    upvotes.append(upvote)

timestamp_elements = driver.find_elements(By.XPATH, '//yt-formatted-string[@class="published-time-text above-comment style-scope ytd-comment-renderer"]')
for element in timestamp_elements:
    timestamp = element.text
    timestamps.append(timestamp)


# In[187]:


df=pd.DataFrame({"Comments":comments,"upvotes":upvotes})
df


# In[189]:


driver.quit()


# 9. Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in
# “London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall
# reviews, privates from price, dorms from price, facilities and property description. 

# In[190]:


driver = webdriver.Chrome()


# In[192]:


driver.get("https://www.hostelworld.com/")


# In[195]:


Input=driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[2]/input")
Input.send_keys("London")


# In[196]:


search=driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[5]/button[1]/div")
search.click()


# In[ ]:


for url in product_urls:
    driver.get(url)
    time.sleep(2)
    
Doms_url=[]
Doms_url=driver.find_elements(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div[5]/div[1]/a/a/div[2]/div[1]")
Doms_url.click()


# In[ ]:




