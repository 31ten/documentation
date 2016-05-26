# -*- coding: utf-8 -*-
from winescrape.items import baiduWineItem
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from selenium import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys



class BaiduSpider(CrawlSpider):
    name = "baidu"
    allowed_domains = ["zhidao.baidu.com"]
    start_urls = [
        'http://zhidao.baidu.com/search?word=%C6%CF%CC%D1%BE%C6%CA%B2%FCN%C5%C6%D7%D3%BA%C3',
    ]


    def parse(self, response):
        for href in response.xpath('//a[@class="ti"]/@href'):
            answers = response.xpath('//span[@class="mr-8"]/a[contains(@data-log,"pos:ans")]/text()').extract()
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, meta={'answers':answers}, callback=self.parse_dir_contents)
        next_page = response.xpath('//a[@class="pager-next"]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

    def parse_dir_contents(self, response):
        item = baiduWineItem()
        item['title'] = response.xpath('//span[@class="ask-title "]/text()').extract()
        item['date'] = response.xpath('//span[@class="grid-r ask-time"]/text()').extract()
        item['views'] = response.xpath('//div[@id="ask-info"]/span/span/text()').extract()
        item['likes'] = response.xpath('//span[@class="evaluate evaluate-32"]/b[contains(@class, "evaluate-num")]/text()').extract()
        item['dislikes'] = response.xpath('//b[@class="evaluate evaluate-bad evaluate-32"]/text()').extract()
        item['answers'] = response.meta['answers']
        item['url'] = response.url
        yield item


