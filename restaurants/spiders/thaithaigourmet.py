# -*- coding: utf-8 -*-
import logging
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
        items = response.xpath('//div[@class="items_wrapper"]/a')
        for item in items:
            name = item.xpath('//h4/text()').get()
            description = item.xpath('//td[@style="width: 80%"]/p/text()').get()
            price = item.xpath('//td[@class="price"]/text()').get()
            logging.info(name)
            logging.info(description)
            logging.info(price)
            yield {
                'name': name,
                'description': description,
                'price': price
            }       
        pass