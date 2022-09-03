# MISSION TO MARS

### SUBJECT: Robin, who loves astronomy and wants to work for NASA one day, has decided to use the web scraping method of gathering current Mission to Mars news and then present the collected data in a central location: a webpage.

### TOOLS Robin will use to build her webpage:
#### * Data gathering with Python, & 2 python libraries - html5lib and lxml
#### * Splinter: will automate her web browser as she begins scraping
#### * Web-Driver Manager: will allow her to easily use a driver that to scrape websites without having to go through the complicated process of installing the stand alone ChromeDriver
#### * Flask-PyMongo: a small and lightweight Python web framework
#### * BeautifulSoup: for parsing HTML and XML documents
#### * MongoDB: a flexible document database that can store non-uniform data such as images, tables, etc.

### WEB PAGE, DATA AND LAYOUT:
#### Header with Title and scraping button
![Header_ScrapeButton](https://user-images.githubusercontent.com/107228424/188285947-769af1e3-1b5f-4320-a22d-f26a4d10a21d.jpg)

#### Latest Mars News: Title and news detail
![Latest_Mars_News](https://user-images.githubusercontent.com/107228424/188285965-41262d4e-e916-4edd-8ef8-41a74f71a6cd.jpg)

#### Featured Mars Image alongside Mars Facts table
![Latest_Mars_News](https://user-images.githubusercontent.com/107228424/188285974-4c386c74-f07c-400c-86ca-f72423470e37.jpg)

### CHALLENGE: adjust the web app to include all Four Hemispheres of Mars images and titles. To do this, use:
  #### * BeautifulSoup and Splinter to scrape full-resolution images of Mars’s hemispheres and the titles of those images
  #### * Store the scraped data on a Mongo database
  #### * Use a web application to display the data
  #### * Add Bootstrap 3 components to alter the design of the web app to accommodate these images.

### DELIVERABLES:
  #### 1) Using BeautifulSoup and Splinter, you’ll scrape full-resolution images of Mars’s hemispheres and the titles of those images. (40 points)
  ####    a. Code is written that retrieves the full-resolution image and title for each hemisphere image (10 pt)
  ####    b. The full-resolution images of the hemispheres are added to the dictionary. (10 pt)
  ####    c. The titles for the hemisphere images are added to the dictionary. (10 pt)
  ####    d. The list contains the dictionary of the full-resolution image URL string and title for each hemisphere image. (10 pt)

  #### 2) Using your Python and HTML skills, you’ll add the code you created in Deliverable 1 to your scraping.py file, update your Mongo database, and modify your index.html file so the webpage contains all the information you collected in this module as well as the full-resolution image and title for each hemisphere image.
  ####  a. The scraping.py file contains code that retrieves the full-resolution image URL and title for each hemisphere image (10 pt)
  ####  b. The Mongo database is updated to contain the full-resolution image URL and title for each hemisphere image (10 pt)
  ####  c. The index.html file contains code that will display the full-resolution image URL and title for each hemisphere image (10 pt)
  ####  d. After the scraping has been completed, the web app contains all the information from this module and the full-resolution images and titles for the four hemisphere images (10 pt)
![4HemispheresMars](https://user-images.githubusercontent.com/107228424/188285986-46b49bd5-6aac-4641-bed2-cdcd7e4f0cc4.jpg)

#### 3) Update your web app to make it mobile-responsive, and add two additional Bootstrap 3 components to make it stand out.
  ####  a. The webpage is mobile-responsive (10 pt)
  ####  b. Two additional Bootstrap 3 components are used to style the webpage (10 pt)
![MissionToMars_Webpage](https://user-images.githubusercontent.com/107228424/188285991-9e90c8c1-6558-4e13-866e-fb64308f543c.jpg)


