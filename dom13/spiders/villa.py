# -*- coding: utf-8 -*-
from dom13.items import Dom13Item
import scrapy


class VillaSpider(scrapy.Spider):
    name = 'villa'
    allowed_domains = ['villaexpert.ru']
    start_urls = ['https://villaexpert.ru/proekti']

    def parse(self, response):
        divs = response.xpath('//div[contains(@class, "views-row")]')
        for div in divs:
            url = div.xpath('.//a/@href').extract_first().strip()
            yield scrapy.Request(response.urljoin(url), callback=self.parse_url)

    @staticmethod
    def parse_url(response):
        item = Dom13Item()
        chars = response.xpath('//table[@class="prj-tab"]//tr')
        item['props'] = {}
        for i, char in enumerate(chars):
            item['props'][str(i)] = {}
            char_xs = char.xpath('./td/text()').extract()
            for iz, char_x in enumerate(char_xs):
                if iz == 0:
                    n = 'name'
                else:
                    n = 'value'
                item['props'][str(i)][n] = char_x.strip()

        prices = response.xpath('//table[@class="prj-tab price-tab"]//tr')
        item['price'] = {}
        for i, price in enumerate(prices):
            item['price'][str(i)] = {}
            price_x = price.xpath('./td')
            item['price'][str(i)]['name'] = price_x[0].xpath('text()').extract_first().strip()
            item['price'][str(i)]['value'] = price_x[1].xpath('./span/text()').extract_first().strip()

        item['images'] = response.xpath('//div[@class="slider slider-for"]//img/@src').extract()
        item['name'] = response.xpath('//h1/text()').extract_first().strip()
        item['id'] = response.url.replace('https://villaexpert.ru/project/', '')

        yield item
