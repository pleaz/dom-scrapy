# -*- coding: utf-8 -*-
from ateraj.items import AterajItem
import scrapy
import json


class AterajSpider(scrapy.Spider):
    name = 'posts'
    allowed_domains = ['ateranetworks.zendesk.com']
    start_urls = ['https://ateranetworks.zendesk.com/api/v2/community/topics/115000398047/posts.json']

    def parse(self, response):
        doc = json.loads(response.body_as_unicode())
        for post in doc['posts']:
            item = AterajItem()
            for key, value in post.items():
                item[key] = value
            yield item
        if doc['next_page'] is not None:
            yield scrapy.Request(response.urljoin(doc['next_page']))
