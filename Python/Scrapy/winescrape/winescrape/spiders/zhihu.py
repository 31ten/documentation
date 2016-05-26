# -*- coding: utf-8 -*-
import scrapy
from winescrape.items import zhihuItem
from scrapy.contrib.spiders import CrawlSpider, Rule

class ZhihuSpider(CrawlSpider):
    name = "zhihu"
    allowed_domains = ["zhihu.com"]
    start_urls = [
        'https://www.zhihu.com/topic/19555489/hot',
    ]

    def parse(self, response):
        for href in response.xpath('//div[@class="feed-content"]/a[@class="question_link"]/@href'):
            url = response.urljoin(href.extract())
            #responses = response.xpath('//td[@class="title"]/text()').extract()
            #meta = {'responses':responses}
            yield scrapy.Request(url, callback=self.parse_dir_contents)


    def parse_dir_contents(self, response):
        item = zhihuItem()
        item['title'] = '葡萄酒'
        item['members'] = '15838'
        item['question_title'] = response.xpath('//span[@class="color-green"]/text()').extract()
        item['concerned'] = '53943'
        item['answers'] = response.xpath('//div[@class="reply-doc content"]/p/text()').extract()
        next_comment = response.xpath('//span[@class="next"]/a/@href')
        if next_comment:
            comment_url = response.urljoin(next_comment[0].extract())
            yield scrapy.Request(comment_url, self.parse_dir_contents)
        else:
            yield item
