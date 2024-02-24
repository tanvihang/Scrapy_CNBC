# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PropertiesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # primary fields
    title = scrapy.Field()
    tag = scrapy.Field()
    author = scrapy.Field()
    image_urls = scrapy.Field()
    url = scrapy.Field()

    # calculated fields
    images = scrapy.Field()
    location = scrapy.Field()

    # others
    url = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    server = scrapy.Field()
    date = scrapy.Field()

    pass
