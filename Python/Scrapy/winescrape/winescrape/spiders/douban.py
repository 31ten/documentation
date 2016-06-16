# -*- coding: utf-8 -*-
import scrapy
from winescrape.items import doubanItem
from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
#from scrapy.linkextractors import LinkExtractor


class DoubanSpider(CrawlSpider):
    #this names our spider, when we crawl we use this to tell scrapy which spider to use
    name = "douban"
    #this tells scrapy what websites it can scrape from
    allowed_domains = ["douban.com"]
    #this is where we set all the urls we want scrapy to start at
    start_urls = [
        #'https://www.douban.com/group/wineshanghai/discussion?start=0',
        #'https://www.douban.com/group/wineroom/discussion?start=0',
        #'https://www.douban.com/group/202012/discussion?start=0',
        #'https://www.douban.com/group/337374/discussion?start=0',
        #'https://www.douban.com/group/243233/discussion?start=0',
        #'https://www.douban.com/group/107856/discussion?start=0',
        #'https://www.douban.com/group/213279/discussion?start=0',
        #'https://www.douban.com/group/red-wine/discussion?start=0',
        #'https://www.douban.com/group/301813/discussion?start=0',
    ]


    #Since what we need to scrape has essentially two pages we need to obtain information from
    #the first page is a list of links that we want to go inside
    #here we tell scrapy to go through all the articles on the page and find the urls associated with a specific xpath selector
    #once you find that link extract the url and then go inside that page to collect our data
    def parse(self, response):
    #for ever url link with this class
        for href in response.xpath('//td[@class="title"]/a/@href'):
            #extract the link so we can go inside it
            url = response.urljoin(href.extract())
            #once collected, for that specific url, go inside and run the method parse_dir_contents to collect our items
            yield scrapy.Request(url, callback=self.parse_dir_contents)
        #once all the links on that page has been collected we need to see if there is a next page we can go to
        #we know there is so we set the next page xpath selector
        next_page = response.xpath('//span[@class="next"]/a/@href')
        if next_page:
            #if there is a next page, we join the url and jump to the next page
            url = response.urljoin(next_page[0].extract())
            #once on the new page we go back to the parse function and begin looking for links again
            yield scrapy.Request(url, self.parse)


    def parse_dir_contents(self, response):
        #on the data page we instantiate our item class
        item = doubanItem()
        #since scrapy is not effecient at handling javascript we must set the name for this page
        #this limits us from allowing our start_urls to only attack one specific start_url at a time
        item['name'] = '大爱红酒'
        #we must also do the same for memebers, since the data is being hidden by JS
        item['members'] = '1612'
        #we set the xpath selectors for all the items we would like to extract and scrape
        item['date'] = response.xpath('//span[@class="color-green"]/text()').extract()
        item['title'] = response.xpath('//div[@id="wrapper"]/div/h1/text()').extract()
        item['responses'] = response.xpath('//div[@class="reply-doc content"]/p/text()').extract()
        #on some pages the comments paginate to another page, so we look for another page
        next_comment = response.xpath('//span[@class="next"]/a/@href')
        #if there is another page of comments
        if next_comment:
            #we extract the link so we can move to the next page
            comment_url = response.urljoin(next_comment[0].extract())
            #then we call back the parse_dir contents and extract more comments
            yield scrapy.Request(comment_url, self.parse_dir_contents)
        else:
            #if there is no next comment then we just yield the item
            yield item

