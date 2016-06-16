# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import csv


#In order for JSON to encode Chinese Characters we make a class that will be set in the item_pipeline settings
class WineprojectPipeline(object):
    #here we set the name of our file , we set it to append, and we make sure the encoding is utf-8
    def __init__(self):
        self.file = codecs.open('douban_nine.json', 'a', encoding='utf-8')

    ##this loads the data from our item class that we are using for the specific bot
    #This makes sure that each line is properly encoded, if the line break is removed only the first line will be encoded
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    #once the data is finished being dumped into the JSON file we close the spider
    def spider_closed(self, spider):
        self.file.close()



#sometimes a client needs a CSV to make it easier for them to read
#here we create another item_pipeline for out CSV file
class csvPipeline(object):
    #this opens the csv file, we name the file, and set it to write
    def __init__(self):
        self.brandCategoryCsv = csv.writer(open('tieba_wine.csv', 'wb'))

    #this sets our rows in the csv file, we want each row to include an item from our items.py class
    #due to various spiders collecting different items, we will need to make sure we change the items accrodingly
    def process_item(self, item, spider):
        self.brandCategoryCsv.writerow([item['date'].encode('utf-8'),
                                        item['title'].encode('utf-8'),
                                        item['user_post'].encode('utf-8'),
                                        item['views'].encode('utf-8'),
                                        item['post_title'].encode('utf-8'),
                                        item['posts'].encode('utf-8'),
                                        item['replies'].encode('utf-8')])
        return item