# -------------------- NOT WORKING -------------------------------
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from properties2.items import PropertiesItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose


class EasySpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['web']
    city = 'bologna'

    start_urls = [f'https://www.immobiliare.it/'
                  f'vendita-case/{city}/']

    # LinkExtractors are specialised in extracting links: in the xpath leave out
    # any /a or /href as they are extracted by default! 
    # eg in the manual spider we had:   '//li/a[@title="Pagina successiva"]/@href'
    # that got replaced with:           '//li/a[@title="Pagina successiva"]'
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//*[contains(@class,"pull-right pagination")]/li')),
        Rule(LinkExtractor(restrict_xpaths='//li[@data-id]//p[@class="titolo text-primary"]'),
             callback='parse_item', follow=True)
        )

    def parse_item(self, response):
        '''Parses a property page from www.immobiliare.it.'''
        l = ItemLoader(item=PropertiesItem(), response=response)
        l.add_xpath('title', "//h1/text()", MapCompose(str.strip, str.title))
        l.add_xpath('price', '//li[@class="features__price"]/span', re='\d+[.]?\d+')
        l.add_xpath('description', '//div[@id="description"]/div//text()', MapCompose(str.strip, str.capitalize))
        l.add_xpath('link', '//div[@class="showcase__list"]//div/img/@src', MapCompose(str.strip))
        return l.load_item()
