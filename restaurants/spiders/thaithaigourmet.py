# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class ThaithaigourmetSpider(scrapy.Spider):
    name = 'thaithaigourmet'
    allowed_domains = ['www.thaithaigourmet.com/']
    start_urls = ['http://www.thaithaigourmet.com/']

    def parse(self, response):
        menu_url = response.css('.logo').xpath('@rel').get()
        print(menu_url)
        yield Request(menu_url, callback=self.parse_menu)
        pass  

    def parse_menu(self, response):
        menu_items = response.css('.items_wrapper').xpath('//h4/text()').extract()
        print(menu_items)
        yield {
            'menu_items': menu_items
        }
        pass