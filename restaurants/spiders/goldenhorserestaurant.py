# -*- coding: utf-8 -*-
import scrapy


class GoldenhorserestaurantSpider(scrapy.Spider):
    name = 'goldenhorserestaurant'
    allowed_domains = ['https://goldenhorseca.com/']
    start_urls = ['http://https://goldenhorseca.com//']

    def parse(self, response):
        pass
