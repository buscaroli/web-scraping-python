import scrapy
from properties2.items import PropertiesItem


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

        item = PropertiesItem()
        item['title'] = response.xpath("//li[@data-id]//p[@class='titolo text-primary']//@title").extract()
        item['price'] = response.xpath("//li[@data-id]//li[@class='lif__item lif__pricing']//text()").re('\d+[.]?\d+')
        item['description'] = response.xpath("//li[@data-id]//p[@class='descrizione__truncate']/text()").extract()
        item['link'] = response.xpath("//li[@data-id]//p[@class='titolo text-primary']/a/@href").extract()
        return item
