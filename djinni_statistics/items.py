# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DjinniStatisticsItem(scrapy.Item):
    title = scrapy.Field()
    technologies = scrapy.Field()
    experience = scrapy.Field()
    date = scrapy.Field()
    views = scrapy.Field()
    applications = scrapy.Field()
