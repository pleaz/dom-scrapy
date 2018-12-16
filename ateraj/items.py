# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AterajItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    details = scrapy.Field()
    author_id = scrapy.Field()
    vote_sum = scrapy.Field()
    vote_count = scrapy.Field()
    comment_count = scrapy.Field()
    follower_count = scrapy.Field()
    topic_id = scrapy.Field()
    html_url = scrapy.Field()
    created_at = scrapy.Field()
    updated_at = scrapy.Field()
    url = scrapy.Field()
    featured = scrapy.Field()
    pinned = scrapy.Field()
    closed = scrapy.Field()
    status = scrapy.Field()
