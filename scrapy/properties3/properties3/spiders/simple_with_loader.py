# Scraping and Crawling a website for properties.
# Using scrapy's temporary data storege: Items and
# using scrapys' item loader functionality.
# Matteo

import scrapy
from properties3.items import ListingItem
from scrapy.loader import ItemLoader


class propertySpider(scrapy.Spider):
    name = 'simple_with_loader'
    city = 'Bologna'

    start_urls = [
        f'https://www.immobiliare.it/vendita-case/{city}/'
    ]

    def parse(self, response):
        ds = ItemLoader(item=ListingItem(), selector=response)

        for page in response.xpath('//ul[@id="listing-container"]'):

            ds.add_xpath('title', '//p/a/@title')
            ds.add_xpath('price', '//li[@class="lif__item lif__pricing"]/text()', re=('\d+[.]?\d+'))
            ds.add_xpath('description', '//p[@class="descrizione__truncate"]/text()')
            ds.add_xpath('link', '//div[@class="showcase__item showcase__item--active"]/img[@src]/@src')
            yield ds.load_item()

        next_page = response.xpath('//li/a[@title="Pagina successiva"]/@href').extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            # yield scrapy.Request(url=next_page_link, callback=self.parse)
            # is same as:
            yield response.follow(url=next_page_link, callback=self.parse)