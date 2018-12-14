# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AteracomItem(scrapy.Item):
    id = scrapy.Field()
    comment_url = scrapy.Field()
    related_post = scrapy.Field()
    comment_text = scrapy.Field()
    comment_datetime = scrapy.Field()
    comment_author = scrapy.Field()
    comment_votes = scrapy.Field()
    comment_official = scrapy.Field()
