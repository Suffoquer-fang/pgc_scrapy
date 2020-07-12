import scrapy
import time
from pgc_scrapy.items import PgcScrapyItem
import json


class iqiyi_spider(scrapy.Spider):
    name = 'iqiyi'

    def start_requests(self):
        for channel_id in [1, 2, 4]:
            page = 1
            while page < 50:
                yield scrapy.Request('http://pcw-api.iqiyi.com/search/recommend/list?channel_id={}&data_type=1&page_id={}&ret_num={}'.format(channel_id, page, 48))
                page += 1


    def parse(self, response):
        ret = json.loads(response.text)
        for data in ret['data']['list']:
            yield scrapy.Request('http://pcw-api.iqiyi.com/video/video/videoinfowithuser/{}'.format(data['tvId']), self.parse_item)

    def parse_item(self, response):
        ret = json.loads(response.text)['data']
        v_title = ret['name']
        if ret['channelId'] == 1:
            v_type = '电影'
        elif ret['channelId'] == 2:
            v_type = '电视剧'
        elif ret['channelId'] == 4:
            v_type = '动画'
        v_tags = []
        v_lang = ''
        v_time = ''
        v_area = ''
        for tag in ret['categories']:
            if tag['subName'] == '类型' or tag['subName'] == '题材':
                v_tags.append(tag['name'])
            elif tag['subName'] == '地区':
                v_area = tag['name']
            elif tag['subName'] == '配音语种':
                v_lang = tag['name']
        v_score = ret['score']
        v_time = ret['formatIssueTime']
        people = ret['people']
        v_directors = []
        v_actors = []
        for dire in people['director']:
            v_directors.append(dire['name'])
        for actor in people['main_charactor']:
            v_actors.append(actor['name'])

        url = ret['playUrl']

        v_desc = ret['description']
        item = PgcScrapyItem(url=url, v_title=v_title, v_lang=v_lang,
            v_tags=v_tags, v_type=v_type, v_actors=v_actors,
            v_directors=v_directors, v_time=v_time, v_score=v_score, v_area=v_area, v_desc = v_desc)
        return item
