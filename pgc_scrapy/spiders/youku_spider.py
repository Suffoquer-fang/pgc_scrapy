import scrapy
from bs4 import BeautifulSoup
from ..items import PgcScrapyItem
from scrapy.spiders import SitemapSpider
import json

class YouKuSpider(SitemapSpider):
  name = 'youku'

  sitemap_urls = ['http://v.qq.com/sitemap/cover_movie.xml', 
                  'https://v.qq.com/sitemap/cover_tv.xml']

  def start_requests(self):
    requests = list(super(YouKuSpider, self).start_requests())
    print()
    print()
    print()
    print('req', requests[:10])
    return requests

  def parse(self, response):
    ret_json = json.loads(response.text)
    ret_data = ret_json['data']
    for item in ret_data:
      url = 'http:'+item['videoLink']
      # print(url)
      yield scrapy.Request(url, self.parse_item)
    # return item

  def parse_item(self, response):
    


    item = PgcScrapyItem(url=response.url, v_title=v_title, v_lang=v_lang, 
            v_tags=v_tags, v_type=v_type, v_actors=v_actors, 
            v_directors=v_directors, v_time=v_time, v_score=v_score, v_area=v_area, v_desc = v_desc)
    return item