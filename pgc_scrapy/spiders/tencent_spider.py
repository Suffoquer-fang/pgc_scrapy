import scrapy
from bs4 import BeautifulSoup
from ..items import PgcScrapyItem
from scrapy.spiders import SitemapSpider

class TencentTVSpider(SitemapSpider):
  name = 'tencent_tv'

  sitemap_urls = ['https://v.qq.com/sitemap/cover_tv.xml']

  def start_requests(self):
    requests = list(super(TencentTVSpider, self).start_requests())
    print()
    print()
    print()
    print('req', requests[:10])
    return requests

  def parse(self, response):
    url = response.url.replace('x/cover', 'detail/1')
    yield scrapy.Request(url, self.parse_item)
    # return item

  def parse_item(self, response):
    # print(response.text)
    v_title = response.xpath('/html/body/div[2]/div[1]/div/div/div/div[2]/h1/a/text()').extract()[0]
    v_type = response.xpath('/html/body/div[2]/div[1]/div/div/div/div[2]/h1/span[2]/text()').extract()[0]
    v_tags = response.xpath('/html/body/div[2]/div[1]/div/div/div/div[5]/div/a/text()').extract()
    v_score = response.xpath('/html/body/div[2]/div[1]/div/div/div/div[1]/div/span[1]/text()').extract()[0]
    v_actors = []
    v_directors = []
    

    soup = BeautifulSoup(response.text, 'lxml')
    ac_info = soup.find(class_='actor_list cf').find_all(class_='item')
    type_info = soup.find_all(class_='type_item')
    
    for actor in ac_info:
      name = actor.find(class_='name').get_text()
      is_dire = actor.find(class_='director')
      if len(name) == 0: continue
      if is_dire is not None:
        v_directors.append(name)
      else:
        v_actors.append(name)
      # print(name, is_dire)
    v_area = ''
    v_lang = ''
    v_time = ''
    v_desc = ''
    v_desc = soup.find(class_='video_desc')
    if v_desc != None:
      v_desc = v_desc.find(class_='txt _desc_txt_lineHight').get_text()
    else:
      v_desc = ''

    for type_item in type_info:
      slot = type_item.find(class_='type_tit')
      value = type_item.find(class_='type_txt')
      if slot is not None:
        if slot.get_text() == '语　言:':
          v_lang = value.get_text()
        elif slot.get_text() == '出品时间:':
          v_time = value.get_text()
        elif slot.get_text() == '地　区:':
          v_area = value.get_text()



    item = PgcScrapyItem(url=response.url, v_title=v_title, v_lang=v_lang, 
            v_tags=v_tags, v_type=v_type, v_actors=v_actors, 
            v_directors=v_directors, v_time=v_time, v_score=v_score, v_area=v_area, v_desc = v_desc)
    return item