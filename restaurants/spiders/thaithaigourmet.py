# -*- coding: utf-8 -*-
import scrapy, subprocess
from scrapy import Request

class ThaithaigourmetSpider(scrapy.Spider):
    name = 'thaithaigourmet'
    allowed_domains = ['thaithaigourmet.com', 'beyondmenu.com']
    start_urls = ['http://www.thaithaigourmet.com/']

    def parse(self, response):
        menu_url = response.css('.logo').xpath('@rel').get()
        print('\n\n\nRedirecting to ' + menu_url + '\n\n\n')
        yield Request(menu_url, callback=self.parse_menu)
        pass

    def parse_menu(self, response):
        items_wrapper_array = response.css('.items_wrapper')
        for items_wrapper in  items_wrapper_array:
            items = items_wrapper.xpath('a')
            for item in items:
                name = item.xpath('//h4/text()').extract_first()
                description = item.xpath('//p/text()').extract_first()
                price = item.xpath('//td[@class="price"]/text()').extract_first()
                yield {
                    'name': name,
                    'description': description,
                    'price': price
                }       
        pass