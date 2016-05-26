# -*- coding: utf-8 -*-
import scrapy
from winescrape.items import WinescrapeItem

class WineSpider(scrapy.Spider):
    name = "wine"
    allowed_domains = ["tieba.baidu.com"]
    start_urls = [
        'http://tieba.baidu.com/f?kw=%E7%BA%A2%E9%85%92&ie=utf-8&pn=0',
        'http://tieba.baidu.com/f?kw=%E8%91%A1%E8%90%84%E9%85%92&ie=utf-8',
        'http://tieba.baidu.com/f?kw=%B7%A8%B9%FA%BA%EC%BE%C6',
        'http://tieba.baidu.com/f?kw=%B9%BA%BE%C6%CD%F8',
        'http://tieba.baidu.com/f?kw=%D1%F3%BE%C6%D7%A8%BC%D2',
        'http://tieba.baidu.com/f?kw=%B2%CD%BE%C6',
        'http://tieba.baidu.com/f?kw=%BD%F8%BF%DA%BA%EC%BE%C6',
        'http://tieba.baidu.com/f?kw=%B7%A8%B9%FA%C6%CF%CC%D1%BE%C6',
        'http://tieba.baidu.com/f?kw=%BA%EC%BE%C6%BD%BB%D2%D7',
    ]

    def parse(self, response):
        for href in response.xpath('//a[contains(@class, "j_th_tit")]/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)
        next_page = response.xpath('//a[@class="next pagination-item"]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)



    def parse_dir_contents(self, response):
        item = WinescrapeItem()
        item['title'] = response.xpath('//a[@class="card_title_fname"]/text()').extract()
        item['views'] = response.xpath('//span[@class="card_menNum"]/text()').extract()
        item['posts'] = response.xpath('//span[@class="card_infoNum"]/text()').extract()
        item['user_post'] = response.xpath('//*[@id="j_p_postlist"]/div[1]/div[2]/ul/li[3]/a/text()').extract()
        item['post_title'] = response.xpath('//div[@class="core_title core_title_theme_bright"]/h1/text()').extract()
        item['date'] = response.xpath('//*[@id="j_p_postlist"]/div[1]/div[3]/div[3]/div[1]/ul[2]/li[2]/span/text()').extract()
        item['replies'] = response.xpath('//li[@class="l_reply_num"]/span/text()').extract()
        yield item
