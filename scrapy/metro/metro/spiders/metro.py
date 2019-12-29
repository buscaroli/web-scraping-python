import scrapy


class MetroSpider(scrapy.Spider):
    # spider's name
    name = 'metro'

    # requests
    def start_requests(self):
        urls = ['https://metro.co.uk/news',
                'https://metro.co.uk/sport',
                'https://metro.co.uk/entertainment',
                'https://metro.co.uk/tv-soaps']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # parse
    def parse(self, response):
        page_name = response.url.split('/')[-2]
        _file = '{0}.html'.format(page_name)
        with open(_file, 'wb') as f:
            f.write(response.body)
