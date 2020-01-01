import scrapy
from properties2.items import PropertiesItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.http import Request


class BasicSpider(scrapy.Spider):
    name = 'manual'
    allowed_domains = ['web']
    city = 'bologna'
    start_urls = [f'https://www.immobiliare.it/'
                  f'vendita-case/{city}/']

    def parse(self, response):
        ''' Gets the index of the next page, if exists'''
        # # next_link_selector is a selector because the methos .extract() is not evoked on it,
        # # that's left to the following line, inside the for loop: 
        # next_link_selector = response.xpath('//*[contains(@class,"pull-right pagination")]/li/a/@href')
        # for url in next_link_selector.extract():
        #     yield Request(url)

        # Getting the total number of pages, creating a list of links and yielding every link
        pages_number = int(response.xpath('//ul[@class="pagination pagination__number"]//li[last()]//text()').get())
        # links = []
        for i in range(2, pages_number):
            new_link = self.start_urls[0] + '?pag=' + str(i)
            yield scrapy.Request(url=response(new_link))
            # links.append(new_link)
        # return [scrapy.Request(url=link, callback=self.parse_item) for link in links]

        item_selector = response.xpath("//li[@data-id]//p[@class='titolo text-primary']/a/@href")
        for url in item_selector.extract():
            yield Request(response.url, callback=self.parse_item)

        # next_link = response.xpath('//li/a[@title="Pagina successiva"]/@href').extract()
        # for url in next_link:
        #     yield Request(urljoin(response.url, url), callback=self.parse_item)

    def parse_item(self, response):
        '''Parses a property page from www.immobiliare.it
        # UNIT TESTING: run 'scrapy check basic'
        @url https://www.immobiliare.it/vendita-case/bologna/
        @returns items 1
        @scrapes title price description link
        '''

        # DEBUGGING: HANDY FOR PLAYING WITH XPATH
        # self.log(response.xpath("//li[@data-id]//p[@class='titolo text-primary']//@title").extract())
        # self.log(response.xpath("//li[@data-id]//li[@class='lif__item lif__pricing']//text()").re('\d+[.]?\d+'))
        # self.log(response.xpath("//li[@data-id]//p[@class='descrizione__truncate']/text()").extract())
        # self.log(response.xpath("//li[@data-id]//p[@class='titolo text-primary']/a/@href").extract())

        # THE FOLLOWING 'BLOCK' HAS BEEN REPLACED BY ITEMLOADER TO MAKE IT
        # TIDIER AND TO BE ABLE TO USE ITEMLOADER'S METHODS (like MapCompose)
        # item = PropertiesItem()
        # item['title'] = response.xpath("//li[@data-id]//p[@class='titolo text-primary']//@title").extract()
        # item['price'] = response.xpath("//li[@data-id]//li[@class='lif__item lif__pricing']//text()").re('\d+[.]?\d+')
        # item['description'] = response.xpath("//li[@data-id]//p[@class='descrizione__truncate']/text()").extract()
        # item['link'] = response.xpath("//li[@data-id]//p[@class='titolo text-primary']/a/@href").extract()
        # return item

        l = ItemLoader(item=PropertiesItem(), response=response)
        l.add_xpath('title', "//h1/text()", MapCompose(str.strip, str.title))
        l.add_xpath('price', '//li[@class="features__price"]/span', re='\d+[.]?\d+')
        l.add_xpath('description', '//div[@id="description"]/div//text()', MapCompose(str.strip, str.capitalize))
        l.add_xpath('link', '//div[@class="showcase__list"]//div/img/@src', MapCompose(str.strip))
        return l.load_item()
