# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AterajcomItem(scrapy.Item):
    id = scrapy.Field()
    body = scrapy.Field()
    author_id = scrapy.Field()
    vote_sum = scrapy.Field()
    vote_count = scrapy.Field()
    official = scrapy.Field()
    html_url = scrapy.Field()
    created_at = scrapy.Field()
    updated_at = scrapy.Field()
    url = scrapy.Field()
    post_id = scrapy.Field()
