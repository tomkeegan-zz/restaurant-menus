# -*- coding: utf-8 -*-
import scrapy, subprocess
from scrapy import Request
from scrapy.selector import Selector

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
            print(items)
            for item in items:
                name = item.xpath('//h4/text()').get()
                description = item.xpath('//td[@style="width: 80%"]/p/text()').get()
                price = item.xpath('//td[@class="price"]/text()').get()
                yield {
                    'name': name,
                    'description': description,
                    'price': price
                }       
        pass