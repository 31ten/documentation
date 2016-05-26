# -*- coding: utf-8 -*-
import scrapy
from winescrape.items import weixinItem

class WeixinSpider(scrapy.Spider):
    name = "weixin"
    allowed_domains = ["mp.weixin.qq.com"]
    start_urls = (
        'http://mp.weixin.qq.com/profile?src=3&timestamp=1463465936&ver=1&signature=otszrQ0wOy5QyIefK7CczdOZXDfKE*TSSTlDchmhX453gcvjeO4Ps5VekM8TzJ4ECMsUDKG0gQV6qJGL8KROOA==',
    )

    def parse(self, response):
        item = weixinItem()
        item['group_name'] = response.xpath('//h4[@class="weui_media_title"]/text()').extract()
        yield item
        #for href in response.xpath('//h4[@class="weui_media_title"]/@href'):
            #url = response.urljoin(href.extract())
            #yield scrapy.Request(url, callback=self.parse_dir_contents)
        #next_page = response.xpath('//a[@class="next pagination-item"]/@href')
        #if next_page:
        #    url = response.urljoin(next_page[0].extract())
        #    yield scrapy.Request(url, self.parse)

    #def parse_dir_contents(self, response):

