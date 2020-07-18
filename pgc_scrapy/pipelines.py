# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import pymysql
from .utils.db_helper import DBHelper

def _printCallback(item):
    # log
    pass


class PgcScrapyPipeline:
  def __init__(self):
    super().__init__()
    self.dbHelper = DBHelper(_printCallback, '127.0.0.1', 'root', '', 'pgc')

  def hasSeen(self, item):
    return self.dbHelper.selectVideo(item) != None

  

  def process_item(self, item, spider):
    self.dbHelper.handleVideo(item)
    self.dbHelper.handlePeople(item)
    
    return item

  def close_spider(self, spider):
    self.dbHelper.closeDB()
