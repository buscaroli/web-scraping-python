# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Field, Item


class ListingItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    price = Field()
    description = Field()
    link = Field()
