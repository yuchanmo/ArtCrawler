##https://docs.scrapy.org/en/latest/topics/spiders.html
##reference : https://medium.com/quick-code/python-scrapy-tutorial-for-beginners-04-crawler-rules-and-linkextractor-7a79aeb8d72
#sample URL : https://www.christies.com/en/results?month=1&year=2019
# import re
# a = 'https://www.christies.com/en/results?month=1&year=2019'
# p = r'en/results\?month=(\w+){1,2}&year=(\w+){4}'
# re.search(p,a)

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ChristiesSpider(CrawlSpider):
    name = 'christies'
    allowed_domains = ['christies.com']
    start_urls = ['http://www.christies.com']

    rules = [
        #Rule(LinkExtractor(allow=(r'en/results\?month=(\w+){1,2}&year=(\w+){4}')),callback='parse_list',follow=True),
        Rule(LinkExtractor(allow=('en/results')),callback='parse_list',follow=True),
    ]

    def parse_list(self, response):
        print(response.url)
