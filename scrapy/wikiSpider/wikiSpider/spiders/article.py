# Learning to Crawl the Web with Python.
# Based on Ryan Mitchell's 'Webscraping with Scrapy'
#
# Matteo

import scrapy

class ArticleSpider(scrapy.Spider):
    # part 1: name
    name = 'article'

    # part 2: requests
    def start_requests(self):
        urls = ['https://en.wikipedia.org/wiki/Bologna',
                'https://en.wikipedia.org/wiki/Pisa',
                'https://en.wikipedia.org/wiki/Rimini',
                'https://en.wikipedia.org/wiki/Ravenna']

        return [scrapy.Request(url=url, callback=self.parse)
                for url in urls]

    # part 3: parse
    def parse(self, response):
        url = response.url
        title = response.xpath('.//h1/text()').get()
        print(f'Title: {title}\nURL: {url}')
