import pymysql
from ..items import PgcScrapyItem

class DBHelper:
  def __init__(self, exceptionCallback):
    super().__init__()
    self.db = pymysql.connect('rm-bp1i2b60x7f66982fto.mysql.rds.aliyuncs.com', 'fangyan', 'fangyan123', 'pgc')
    self.cursor = self.db.cursor()
    self.callback = exceptionCallback

  def _selectSQL(self, url):
    return "SELECT * FROM `videoitem` WHERE `url`='%s'"%(url)

  def select(self, item):
    url = item['url']
    sql = self._selectSQL(url)
    self.cursor.execute(sql)
    results = self.cursor.fetchone()
    return results

  def _insertSQL(self, item):
    sql = "INSERT INTO `videoitem` (`id`, `url`, `title`, `time`, `type`, `lang`, `score`, `area`, `descp`, `tags`, `directors`, `actors`) VALUES (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
       (item['url'], item['v_title'], item['v_time'], item['v_type'], item['v_lang'], item['v_score'], item['v_area'], item['v_desc'], ','.join(item['v_tags']), ','.join(item['v_directors']), ','.join(item['v_actors']))
    return sql

  def insert(self, item):
    sql = self._insertSQL(item)
    try:
      self.cursor.execute(sql)
      self.db.commit()
    except:
      self.db.rollback()
      self.callback()

  def insertNewVideo(self, item):
    pass 

  def updateVideo(self, item):
    pass 

  def closeDB(self):
    self.db.close()