#!/usr/bin/env python
# coding: utf-8

# # Web Scraping Homework - Mission to Mars
# 
# ![mission_to_mars](Images/mission_to_mars.png)

# In[23]:


from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests, pymongo, time, os


# In[24]:



#Setup configuration variables to enable Splinter to interact with browser 
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)


# ## Step 1 - Scraping
# 
# Complete your initial scraping
# Pandas, and Requests/Splinter.

# ### NASA Mars News
# * Scrape the [Mars News Site](https://redplanetscience.com/) and 
# collect the latest News Title and Paragraph Text. 
# 
# 

# In[25]:


def scrape_news(bro):
    
    # Visit the mars nasa news site
    # URL of page to be scraped
    url='https://redplanetscience.com/'

    # Use the browser to visit the url

    bro.visit(url)

    # Wait for 5 seconds for error purpouses
    time.sleep(5)

    # Return the rendered page by the browser
    html_nasa = bro.html

    # Use beatifulsoup to scrap the page rendered by the browser
    soup = BeautifulSoup(html_nasa, 'html.parser')

    # Search for the div where the title is located
    # Retrieve the news title
    results = soup.find_all('div', class_="content_title")
    news_title = results[0].text
    #?
    news_p = results[1].text
    #?    

    # Search for the div where the paragraph news is located
    results = soup.find_all('div', class_="article_teaser_body")
    news_p = results[0].text
    #print(f"Paragraph: {new_p}")

    # Step 1 - Scraping
    # Create a empty dictionary to store the data
    scraped_data = {
        'news_title':news_title,
        'news_p':news_p    

    }
    print(scraped_data)
    return scraped_data


scrape_news(browser)


# 
# ### JPL Mars Space Images - Featured Image
# 
# * Visit the url for the Featured Space Image site [here](https://spaceimages
# 
# * Use splinter to navigate the site and find the image url for the current F
# Image and assign the url string to a variable called `featured_image_url`.
# 
# * Make sure to find the image url to the full size `.jpg` image.
# 
# * Make sure to save a complete url string for this image.
# 
# ```python
# # Example:
# featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'
# 

# In[27]:


def scrape_feature(brow):
    
    # URL for JPL Nasa websit-visit
    url_jpl = "https://www.spaceimages-mars.com"
    # Use the browser to visit the url
    brow.visit(url_jpl) 

    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    html_jpl = brow.html
    soup = BeautifulSoup(html_jpl, 'html.parser')

    # Featured image is in the div class="???"
    space_images = soup.find('img', class_="fancybox-image").get("src")
    
    # The url for JPL Featured Space Image - at end

    # Full url
    feature_image_url = f"{url_jpl}{space_images}"
    print(feature_image_url)
    return feature_image_url

scrape_feature(browser)


# ### Mars Facts
# 
# * Visit the Mars Facts webpage [here](https://galaxyfact
# the table containing facts about the planet including Di
# 
# * Use Pandas to convert the data to a HTML table string.
# 
# 

# In[28]:


def scrape_mars_facts(brows):
    # URL
    url_mars_facts = "https://space-facts.com/mars/"

    # Use Pandas to automatically scrape any tabular data from a page.
    mars_facts = pd.read_html(url_mars_facts)
    mars_df = mars_facts[1]
    #(mars_df)
    #How many tables are available
    #len(mars_facts)


    mars_df.columns=['Mars - Earth Comparison','Mars','Earth']
    
    mars_df.set_index('Mars - Earth Comparison',inplace=True)
    print (mars_df)
    #mars_df
    
    
    return mars_df

scrape_mars_facts(browser)

#    mars_df.to_html()


# ### Mars Hemispheres
# 
# * Visit the astrogeology site [here](https://marshemispheres.com/) to 
# obtain high resolution images for each of Mar's hemispheres.
# 
# * You will need to click each of the links to the hemispheres in order 
# to find the image url to the full resolution image.
# 
# * Save both the image url string for the full resolution hemisphere 
# image, and the Hemisphere title containing the hemisphere name. Use a 
# Python dictionary to store the data using the keys `img_url` and 
# `title`.
# 
# * Append the dictionary with the image url string and the hemisphere 
# title to a list. This list will contain one dictionary for each 
# hemisphere.
# 

# In[29]:


def scrape_hemis(brows):
    # URL of page to be scraped
    url_mars_hemispheres='https://marshemispheres.com/'

    # Use the browser to visit the url
    brows.visit(url_mars_hemispheres)

    # Create a list with the name of the hemispheres
    list_hemispheres = []

    links=brows.find_by_css('a.product-item img')

    for i in range(len(links)):
        hemis={}
        brows.find_by_css('a.product-item img')[i].click()
        sample=brows.links.find_by_text('Sample').first
        hemis['url']=sample['href']
        hemis['title']=brows.find_by_css('h2.title').text

        list_hemispheres.append(hemis)
        brows.back() 
        
       # mars_hemis_url = f"{url_mars_hemispheres}{hemis}"   
  
    return list_hemispheres

scrape_hemis(browser)


# In[30]:



def scrape_all(browser):
    this=scrape_news(browser)
    this_dict = {
        "news_title" : this['news_title'],
        "news_p" : this['news_p'],
        "feature_image_url" : scrape_feature(browser),
        "hemispheres" : scrape_hemis(browser),
        "table_html" : scrape_mars_facts(browser)
            }
    print(this_dict)
    return this_dict

scrape_all(browser)



# In[20]:



def scrape_all(browser):
    this=scrape_news(browser)
    this_dict = {
        "news_title" : this['news_title'],
        "news_p" : this['news_p'],
        "feature_image_url" : scrape_feature(browser),
        "hemispheres" : scrape_hemis(browser),
        "table_html" : scrape_mars_facts(browser)
            }
    print(this_dict)
    return this_dict

 scrape_all(browser)


# In[31]:


#calling the function -- pass browser to the function
print(scrape_all(browser))


# In[32]:


# When you’ve finished testing, close your browser using browser.quit:
browser.quit()


# In[ ]:




