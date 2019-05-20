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
    mwr = mars_weather_readings.split("pic.")

    
  # Mars Facts (4 of 5)

    mars_facts_url = "https://space-facts.com/mars/"
    mars_facts_table = pd.read_html(mars_facts_url)
    mars_facts_df = mars_facts_table[0]
    mars_facts_df.columns = ["Query", "Fax"]
    eq_diam = mars_facts_df["Query"][0]
    pl_diam = mars_facts_df["Query"][1]
    mass = mars_facts_df["Query"][2]
    moons = mars_facts_df["Query"][3]
    o_dist = mars_facts_df["Query"][4]
    o_period = mars_facts_df["Query"][5]
    temp = mars_facts_df["Query"][6]
    first_rec = mars_facts_df["Query"][7]
    rec_by = mars_facts_df["Query"][8]
    eq_diam_faq = mars_facts_df["Fax"][0]
    pl_diam_faq = mars_facts_df["Fax"][1]
    mass_faq = mars_facts_df["Fax"][2]
    moons_faq = mars_facts_df["Fax"][3]
    o_dist_faq = mars_facts_df["Fax"][4]
    o_period_faq = mars_facts_df["Fax"][5]
    temp_faq = mars_facts_df["Fax"][6]
    first_rec_faq = mars_facts_df["Fax"][7]
    rec_by_faq = mars_facts_df["Fax"][8]
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
    hemispheres_image_download_url = []
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
        hidu = hemispheres_image_download_url.split("\n")
    
    
        
    mars_dashboard = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather_readings": mwr[0],
        "mars_table": mars_facts_html_table,
        "hemispheres_imgs_one": hemispheres_image_download_url,
        "eq_diam": eq_diam,
        "pl_diam": pl_diam,
        "mass": mass,
        "moons": moons,
        "o_dist": o_dist,
        "o_period": o_period,
        "temp": temp,
        "first_rec": first_rec,
        "rec_by": rec_by,
        "eq_diam_faq": eq_diam_faq,
        "pl_diam_faq": pl_diam_faq,
        "mass_faq": mass_faq,
        "moons_faq": moons_faq,
        "o_dist_faq": o_dist_faq,
        "o_period_faq": o_period_faq,
        "temp_faq": temp_faq,
        "first_rec_faq": first_rec_faq,
        "rec_by_faq": rec_by_faq
        }
        
  # Close the browser after scraping

    mars_img_browser.quit()
    mars_hemispheres_base_img_browser.quit()

  # Return results

    return mars_dashboard