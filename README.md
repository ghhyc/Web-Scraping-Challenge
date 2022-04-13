# Mission to Mars

![mission_to_mars](Images/mission_to_mars.png)

This assignment aims to build a web application that scrapes four different websites for the Mission to Mars data and displays the information on a single HTML page.

The following steps is used in order to complete this objective:

## Scraping

### NASA Mars News

url=https://redplanetscience.com/ website was used to get the latest news on Mars mission using BeautifulSoup, splinter, pandas in a jupyter notebook.

### JPL Mars Space Images - Featured Image

https://www.spaceimages-mars.com was used to scrape the featured image of mars in full resolution.

### Mars Facts

https://space-facts.com/mars/ was used to obtain the table containing facts about the planet, including Diameter, Mass, etc.

### Mars Hemispheres

https://marshemispheres.com/ was used to obtain high-resolution images for each of Mar's hemispheres.

## Flask

- A python script to run all of the scraping code was designed ,and all of the scraped data was put into one Python dictionary.

- '/scrape' route, which will import the Python script and call the scrape function, was created.

## HTML file

Finally a HTML file called 'index.html' was created that displayed all of the data in HTML elements.

![final_app.png](Images/final_app.png)
