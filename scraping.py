# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# set executable path, then set up the URL (NASA Mars News (Links to an external site.)) for scraping
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# assign the url & instruct the browser to Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page (a specific combination of tag (div) 
  # and attribute (list_text). example: ul.item_list would be found in HTML as <ul class="item_list">)
browser.is_element_present_by_css('div.list_text', wait_time=1)

# set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# begin scraping: assign the title and summary text to variables 
  # we'll reference later
slide_elem.find('div', class_='content_title')

# Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image.  
# #(use markdown to separate the article scraping from the image scraping.  Select drop down in toolbar & select markdown.)

# set up the URL we are getting the images from
url = 'https://spaceimages-mars.com'
browser.visit(url)

# we want to click the "Full Image" button. use the HTML tag in our code
# Find and click the full image button ([1] indicates we want to click the second 'button')
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# need to click the More Info button to get to the next page.
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Pull the most recent image each time the code is executed
# Find the relative image url (by inspecting the website code & using dev tools
    # we know it's in img class="fancybox-image" & src="image/featured/ . . .")
# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL (add base URL to pull up image in browser)
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# MARK UP FACTS TABLE

# scrape (grab) the entire table with Pandas' .read_html() function (at top import pandas)
  #create a new DataFrame from the HTML table. The Pandas function read_html() & [0] specifically 
  #searches for and returns the first list of tables found in the HTML
df = pd.read_html('https://galaxyfacts-mars.com')[0]
  # assign columns to the new DataFrame for additional clarity
df.columns=['description', 'Mars', 'Earth']
  # turning the Description column into the DataFrame's index. inplace=True means that the updated 
  # index will remain in place, without having to reassign the DataFrame to a new variable
df.set_index('description', inplace=True)
df

# Use Pandas to easily convert our DataFrame back into HTML-ready code 
# using the .to_html() function for live web-site use
df.to_html()

# end the automated browsing session
browser.quit()
