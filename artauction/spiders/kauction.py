import scrapy


class KauctionSpider(scrapy.Spider):
    name = 'kauction'
    allowed_domains = ['http://kartprice.net']
    start_urls = ['http://http://kartprice.net/']

    def parse(self, response):
        pass
