#!/usr/bin/env python
# coding: utf-8

# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd
from selenium import webdriver

# Convert Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

def scrape():
    
  # NASA Mars News (1 of 5)
    
    NASA_mars_news_url = 'https://mars.nasa.gov/news/'
    mars_response = requests.get(NASA_mars_news_url)
    martian_soup = BeautifulSoup(mars_response.text, 'html.parser')
    news_title = martian_soup.find('div', 'a', class_="content_title").text
    news_p = martian_soup.find('div', class_="rollover_description_inner").text
    
  # JPL Mars Space Images - Featured Image (2 of 5)
    
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    mars_img_browser = Browser('chrome', **executable_path, headless=False)
    mars_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    mars_img_browser.visit(mars_image_url)
    mars_html = mars_img_browser.html
    mars_img_soup = BeautifulSoup(mars_html, 'html.parser')
    base_img_url = "https://www.jpl.nasa.gov"
    img_url = mars_img_soup.find("a", class_="button fancybox")["data-fancybox-href"]
    featured_image_url = (base_img_url + img_url)
    print (featured_image_url)

  # Mars Weather (3 of 5)

    mars_weather_url = "https://twitter.com/marswxreport?lang=en)"
    mars_weather_request = requests.get(mars_weather_url)
    mars_weather_soup = BeautifulSoup(mars_weather_request.text, 'html.parser')
    mars_weather_readings = mars_weather_soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    
  # Mars Facts (4 of 5)

    mars_facts_url = "https://space-facts.com/mars/"
    mars_facts_table = pd.read_html(mars_facts_url)
    mars_facts_df = mars_facts_table[0]
    mars_facts_df.columns = ["Query", "Fax"]
    mars_facts_html_table = mars_facts_df.to_html() # 'Table/mars_html_table.html' -- to create previewable html
    mars_facts_html_table = mars_facts_html_table.replace("\n", "")
    print(mars_facts_html_table)


  # Mars Hemispheres (5 of 5)

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    mars_hemispheres_base_img_browser = Browser('chrome', **executable_path, headless=False)
    mars_hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    mars_hemispheres_base_img_browser.visit(mars_hemisphere_url)
    mars_hemisphere_html = mars_hemispheres_base_img_browser.html
    mars_hemisphere_html_soup = BeautifulSoup(mars_hemisphere_html, 'html.parser')
    hemispheres_imgs = mars_hemisphere_html_soup.find_all("div", class_="item")
    hemispheres_base_img_url = "https://astrogeology.usgs.gov"

    hemispheres_imgs_urls = []

    for img in hemispheres_imgs:
        img_title = img.find("h3").text
        img_url = img.find("a")["href"]
        full_img_link = hemispheres_base_img_url + img_url 

        mars_hemispheres_base_img_browser.visit(full_img_link)
        hemispheres_base_img_html = mars_hemispheres_base_img_browser.html
        hemispheres_full_img_soup = BeautifulSoup(hemispheres_base_img_html, "html.parser")
        hemispheres_downloads = hemispheres_full_img_soup.find("div", class_="downloads")
        hemispheres_image_download_url = hemispheres_downloads.find("a")["href"]
        hemispheres_imgs_urls.append({"title": img_title, "img_url": img_url})

    mars_dashboard = {
        "News Title": news_title,
        "News Paragraph": news_p,
        "Featured Image": featured_image_url,
        "Weather": mars_weather_readings,
        "Hemisphere Images": hemispheres_imgs_urls
        }
        
  # Close the browser after scraping

    mars_img_browser.quit()
    mars_hemispheres_base_img_browser.quit()

  # Return results

    return mars_dashboard