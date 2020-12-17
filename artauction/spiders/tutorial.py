import scrapy


class TutorialSpider(scrapy.Spider):
    name = 'tutorial'
    allowed_domains = ['https://docs.scrapy.org/en/latest/intro/tutorial.html']
    start_urls = ['http://https://docs.scrapy.org/en/latest/intro/tutorial.html/']

    def parse(self, response):
        pass
