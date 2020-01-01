import scrapy
from properties3.items import ListingItem
# from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader


class propertySpider(scrapy.Spider):
    name = 'simple'
    city = 'Bologna'

    start_urls = [
        f'https://www.immobiliare.it/vendita-case/{city}/'
    ]

    def parse(self, response):
        ds = ItemLoader(item=ListingItem(), response=response)

        for page in response.xpath('//ul[@id="listing-container"]'):
            # ds.add_xpath('title', '//h1/text()',
            #                       MapCompose(str.strip, str.title))
            # ds.add_xpath('price', '//li[@class="features__price"]/span',
            #                       re='\d+[.]?\d+')
            # ds.add_xpath('description', '//div[@id="description"]/div//text()',
            #                             MapCompose(str.strip, str.capitalize))
            # ds.add_xpath('link', '//div[@class="showcase__list"]//div/img/@src',
            #                      MapCompose(str.strip))
            yield {
                'title': page.xpath('//p/a/@title').extract(),
                'price': page.xpath('//li[@class="lif__item lif__pricing"]/text()').re('\d+[.]?\d+'),
                'description': page.xpath('//p[@class="descrizione__truncate"]/text()').extract(),
                'link': page.xpath('//div[@class="showcase__item showcase__item--active"]/img[@src]/@src').extract()
            }

        next_page = response.xpath('//li/a[@title="Pagina successiva"]/@href').extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
