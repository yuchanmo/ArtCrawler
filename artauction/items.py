# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SubLinkInfo(scrapy.Item):
    current_link = scrapy.Field()
    sub_links = scrapy.Field()



class ArtInfo(scrapy.Item):
    exibition = scrapy.Field()
    lotnum = scrapy.Field()
    artist = scrapy.Field()
    title = scrapy.Field()
    estimate = scrapy.Field()
    soldprice = scrapy.Field()
    size = scrapy.Field()
    auctiondate = scrapy.Field()
    imgurl = scrapy.Field()
    description = scrapy.Field()

    # def __repr__(self):
    #     return f'{self.exibition}'

from scrapy import Item,Field

class LandsbotItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ts = Field()
    sale_type = Field()
    building_type = Field()
    building_name = Field()
    area = Field()
    supply_area = Field()
    exclusive_area = Field()
    floor = Field()
    sale_floor = Field()
    max_floor = Field()
    sale_price = Field()
    deposit = Field()
    rent_fee = Field()