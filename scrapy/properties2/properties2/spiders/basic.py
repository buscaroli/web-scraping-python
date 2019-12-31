import scrapy
from properties2.items import PropertiesItem
from scrapy.loader import ItemLoader


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    city = 'bologna'
    start_urls = [f'https://www.immobiliare.it/'
                  f'vendita-case/{city}/?criterio=rilevanza']

    def parse(self, response):
        # DEBUGGING: HANDY TO PLAY WITH XPATH
        # self.log(response.xpath("//li[@data-id]//p[@class='titolo text-primary']//@title").extract())
        # self.log(response.xpath("//li[@data-id]//li[@class='lif__item lif__pricing']//text()").re('\d+[.]?\d+'))
        # self.log(response.xpath("//li[@data-id]//p[@class='descrizione__truncate']/text()").extract())
        # self.log(response.xpath("//li[@data-id]//p[@class='titolo text-primary']/a/@href").extract())

        # THE FOLLOWING 'BLOCK' HAS BEEN REPLACED BY ITEMLOADER TO MAKE IT
        # TIDIER AND TO BE ABLE TO USE ITEMLOADER'S METHODS
        # item = PropertiesItem()
        # item['title'] = response.xpath("//li[@data-id]//p[@class='titolo text-primary']//@title").extract()
        # item['price'] = response.xpath("//li[@data-id]//li[@class='lif__item lif__pricing']//text()").re('\d+[.]?\d+')
        # item['description'] = response.xpath("//li[@data-id]//p[@class='descrizione__truncate']/text()").extract()
        # item['link'] = response.xpath("//li[@data-id]//p[@class='titolo text-primary']/a/@href").extract()
        # return item

        l = ItemLoader(item=PropertiesItem(), response=response)
        l.add_xpath('title', "//li[@data-id]//p[@class='titolo text-primary']//@title")
        l.add_xpath('price', "//li[@data-id]//li[@class='lif__item lif__pricing']//text()", re='\d+[.]?\d+')
        l.add_xpath('description', "//li[@data-id]//p[@class='descrizione__truncate']/text()")
        l.add_xpath('link', "//li[@data-id]//p[@class='titolo text-primary']/a/@href")
        return l.load_item()
