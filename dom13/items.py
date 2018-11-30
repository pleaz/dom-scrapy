# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Dom13Item(scrapy.Item):
    id = scrapy.Field()
    props = scrapy.Field()
    price = scrapy.Field()
    images = scrapy.Field()
    name = scrapy.Field()
