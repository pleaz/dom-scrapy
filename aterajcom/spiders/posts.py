# -*- coding: utf-8 -*-
from aterajcom.items import AterajcomItem
import scrapy
import json


class AterajcomSpider(scrapy.Spider):
    name = 'comments'
    allowed_domains = ['ateranetworks.zendesk.com']
    start_urls = ['https://ateranetworks.zendesk.com/api/v2/community/topics/115000398047/posts.json']

    def parse(self, response):
        doc = json.loads(response.body_as_unicode())
        for post in doc['posts']:
            yield scrapy.Request(
                response.urljoin(
                    'https://ateranetworks.zendesk.com/api/v2/community/posts/'+str(post['id'])+'/comments.json'),
                callback=self.parse_url
            )
        if doc['next_page'] is not None:
            yield scrapy.Request(response.urljoin(doc['next_page']))

    @staticmethod
    def parse_url(response):
        comments = json.loads(response.body_as_unicode())
        for comment in comments['comments']:
            item = AterajcomItem()
            for key, value in comment.items():
                item[key] = value
            yield item
