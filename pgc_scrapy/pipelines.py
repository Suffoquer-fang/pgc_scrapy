# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import pymysql

class PgcScrapyPipeline:
  def __init__(self):
    super().__init__()
    self.db = pymysql.connect("localhost","root","","pgc" )
    self.cursor = self.db.cursor()

  def hasSeen(self, url):
    sql = "SELECT * FROM `videoitem` WHERE `url`='%s'"%(url)
    self.cursor.execute(sql)
    results = self.cursor.fetchone()
    return results != None

  def process_item(self, item, spider):
      url = item['url']
      sql = "INSERT INTO `videoitem` (`id`, `url`, `title`, `time`, `type`, `lang`, `score`, `area`, `descp`, `tags`, `directors`, `actors`) VALUES (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
       (url, item['v_title'], item['v_time'], item['v_type'], item['v_lang'], item['v_score'], item['v_area'], item['v_desc'], ','.join(item['v_tags']), ','.join(item['v_directors']), ','.join(item['v_actors']))
      if not self.hasSeen(url):
        try:
          self.cursor.execute(sql)
          self.db.commit()
        except:
          self.db.rollback()

      return item

  def close_spider(self, spider):
    self.db.close()
