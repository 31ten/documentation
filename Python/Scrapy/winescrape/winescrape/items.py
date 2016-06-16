# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


#In the items.py file we define the items we want to collect from the specific website
#For each item we set it to Field()
#This helps keep our data well maintained and kept together

#Here We are scraping 5 different websites looking for specific information on each page
#We make a different item for each website we will scrape

class WinescrapeItem(scrapy.Item):
    title = Field()
    views = Field()
    posts = Field()
    user_post = Field()
    post_title = Field()
    date = Field()
    replies = Field()


class baiduWineItem(scrapy.Item):
    title = Field()
    answers = Field()
    date = Field()
    views = Field()
    likes = Field()
    dislikes = Field()
    url = Field()

class weixinItem(scrapy.Item):
    group_name = Field()
    group_id = Field()
    title = Field()
    views = Field()
    likes = Field()
    link = Field()


class doubanItem(scrapy.Item):
    name = Field()
    members = Field()
    title = Field()
    responses = Field()
    date = Field()


class zhihuItem(scrapy.Item):
    title = Field()
    members = Field()
    question_title = Field()
    concerned = Field()
    answers = Field()

