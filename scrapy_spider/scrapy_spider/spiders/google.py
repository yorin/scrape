# -*- coding: utf-8 -*-
import scrapy


class GoogleSpider(scrapy.Spider):
    name = 'google_spider'
    allowed_domains = ['google.com']
    start_urls = ['https://google.com/']

    def parse(self, response):
        pass
