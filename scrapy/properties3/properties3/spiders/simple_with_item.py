# Scraping and Crawling a website for properties.
# Using scrapy's temporary data storege: Items
# Matteo

import scrapy
from properties3.items import ListingItem


class propertySpider(scrapy.Spider):
    name = 'simple_with_item'
    city = 'Bologna'

    start_urls = [
        f'https://www.immobiliare.it/vendita-case/{city}/'
    ]

    def parse(self, response):
        ds = ListingItem()

        for page in response.xpath('//ul[@id="listing-container"]'):

            title = page.xpath('//p/a/@title').extract()
            price = page.xpath('//li[@class="lif__item lif__pricing"]/text()').re('\d+[.]?\d+')
            description = page.xpath('//p[@class="descrizione__truncate"]/text()').extract()
            link = page.xpath('//div[@class="showcase__item showcase__item--active"]/img[@src]/@src').extract()

            ds['title'] = title
            ds['price'] = price
            ds['description'] = description
            ds['link'] = link
            yield ds

        next_page = response.xpath('//li/a[@title="Pagina successiva"]/@href').extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            # yield scrapy.Request(url=next_page_link, callback=self.parse)
            # is same as:
            yield response.follow(url=next_page_link, callback=self.parse)