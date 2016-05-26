## How to Setup and Install Scrapy

To first setup and install Scrapy we must make sure we are using Python2.7 or Python3.
Since we are scraping data from Chinese websites, it's best if we use Python3 since it handles utf-8 data out of the box.

I prefer using vitualenv to structure my Python Projects, but virtualenv is out of the scope of this project.

When installing packages with python we use pip.
Make the project directory and inside run this command:

    pip install Scrapy


Scrapy is now installed on your computer and is ready to be used.
Inside the project folder run this command to start your project.

    scrapy startproject name_of_project


This will create the working template for our project, it creates all the neccessary files we will be using.

We can test the website and see what we can grab before we begin coding by running this command:

    scrapy shell full_name_of_url_you_want_to_scrape

This opens an interactive shell in the terminal, here we can test what we can grab using xpath selectors, this is a good first way to begin testing the website

To create the spider that will crawl the pages we want, we run this command to create the files:

    scrapy genspider name_of_spider name_of_url_to_scrape

Now we have all the neccessary files to begin crawling web pages

Once we have finished writing our code we run the spider with:

    scrapy crawl spider_name

If we want it to automatically import to json or CSV we can run this command

    scrapy crawl spider_name -o name_of_json.json

 or

     scrapy crawl spider_name -o name_of_csv.csv

For more information about Scrapy check out their documentation at https://scrapy.readthedocs.io/en/latest/index.html



