# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OptionsItem(scrapy.Item):
    contract = scrapy.Field()
    last_trade = scrapy.Field()
    strike = scrapy.Field()
    last_price = scrapy.Field()
    bid = scrapy.Field()
    ask = scrapy.Field()
    change = scrapy.Field()
    pct_change = scrapy.Field()
    volume = scrapy.Field()
    open_int = scrapy.Field()
    imp_vol = scrapy.Field()
