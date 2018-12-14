# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AteraItem(scrapy.Item):
    id = scrapy.Field()
    post_url = scrapy.Field()
    post_title = scrapy.Field()
    post_text = scrapy.Field()
    post_datetime = scrapy.Field()
    post_author = scrapy.Field()
    post_votes = scrapy.Field()
    post_status = scrapy.Field()
