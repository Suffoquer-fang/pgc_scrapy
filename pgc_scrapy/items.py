# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PgcScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    v_title = scrapy.Field()
    v_type = scrapy.Field()
    v_tags = scrapy.Field()
    v_lang = scrapy.Field()
    v_directors = scrapy.Field()
    v_actors = scrapy.Field()
    v_time = scrapy.Field()
    v_score = scrapy.Field()
    v_area = scrapy.Field()
    v_desc = scrapy.Field()

