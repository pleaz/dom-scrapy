# -*- coding: utf-8 -*-
from atera.items import AteraItem
import scrapy
import re


class VillaSpider(scrapy.Spider):
    name = 'posts'
    allowed_domains = ['support.atera.com']
    start_urls = ['https://support.atera.com/hc/en-us/community/topics/115000398047-Atera-Ideas']

    def parse(self, response):
        divs = response.xpath('//div[contains(@class, "post-overview")]')
        for div in divs:
            url = div.xpath('.//span[@class="post-overview-info"]/a/@href').extract_first().strip()
            yield scrapy.Request(response.urljoin(url), callback=self.parse_url)

        next_page_url = response.xpath('//li[@class="pagination-next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

    @staticmethod
    def parse_url(response):
        item = AteraItem()
        item['id'] = re.findall(r'/posts/([0-9]+)-', response.url)[0]
        item['post_url'] = response.url
        item['post_title'] = response.xpath('//div[@class="post-header"]/h1/text()').extract_first().strip()
        date = response.xpath('//div[contains(@class, "post-published")]')
        item['post_text'] = response.xpath('//div[contains(@class, "post-body")]'
                                           ).extract_first().strip().replace(date.extract_first(), '')
        formatted = date.xpath('./time/@datetime').extract_first().strip().replace('T', ' ').replace('-', '/')
        item['post_datetime'] = re.sub(r':([0-9]{2})Z', '', formatted)
        item['post_author'] = response.xpath('//strong[@class="post-author"]/text()').extract_first().strip()
        item['post_votes'] = response.xpath(
            '//div[contains(@class, "post-vote")]/span[@class="vote-sum"]/text()').extract_first().strip()
        post_status = response.xpath('//div[@class="post-status"]/span/text()').extract_first()
        if post_status != 'None':
            item['post_status'] = post_status.strip()

        yield item
