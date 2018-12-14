# -*- coding: utf-8 -*-
from ateracom.items import AteracomItem
import scrapy
import re


class VillaSpider(scrapy.Spider):
    name = 'comments'
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
        comments = response.xpath('//ul[@class="comment-list"]/li')
        if comments:
            for comment in comments:
                item = AteracomItem()
                item['comment_text'] = comment.xpath('.//div[contains(@class, "comment-body")]').extract_first().strip()
                date = comment.xpath('.//time[@class="comment-published"]/@datetime'
                                      ).extract_first().strip().replace('T', ' ').replace('-', '/')
                item['comment_datetime'] = re.sub(r':([0-9]{2})Z', '', date)
                item['comment_author'] = comment.xpath('.//strong[@class="comment-author"]/text()'
                                                       ).extract_first().strip()
                votes = comment.xpath('.//div[contains(@class, "comment-vote")]/span[@class="vote-sum"]/text()'
                                      ).extract_first()
                if votes:
                    item['comment_votes'] = votes.strip()

                official = comment.xpath('.//div[contains(@class, "comment-avatar-agent")]').extract_first()
                if official:
                    item['comment_official'] = 'Official Comment'

                item['related_post'] = response.xpath('//div[@class="post-header"]/h1/text()').extract_first().strip()
                url = comment.xpath('.//a[@data-action="show-permalink"]/@href').extract_first()
                item['comment_url'] = url.strip()
                item['id'] = re.findall(r'/comments/([0-9]+)', url)[0]

                yield item
