# -*- coding: utf-8 -*-
import logging, scrapy
from scrapy import Request
from scrapy.selector import Selector

class ThaithaigourmetSpider(scrapy.Spider):
    name = 'thaithaigourmet'
    allowed_domains = ['thaithaigourmet.com', 'beyondmenu.com']
    start_urls = ['http://www.thaithaigourmet.com/']

    def parse(self, response):
        menu_url = response.css('div.logo').attrib['rel']
        logging.info('Redirecting to ' + menu_url)
        yield Request(menu_url, callback=self.parse_menu)
        pass

    def parse_menu(self, response):
        count = 1
        for item in response.css('div.items_wrapper a'):
            logging.info('Menu items scraped: ' + str(count))
            count = count + 1
            name = item.xpath('./h4/text()').get()
            description = item.xpath('./td[@style="width: 80%"]/p/text()').get()
            price = item.xpath('./td[@class="price"]/text()').get()
            yield {
                'name': name,
                'description': description,
                'price': price
            }       
        pass