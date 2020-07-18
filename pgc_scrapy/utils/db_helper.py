import pymysql


class DBHelper:
  def __init__(self, exceptionCallback=None, host='rm-bp1i2b60x7f66982fto.mysql.rds.aliyuncs.com', user='fangyan', passwd='fangyan123', db='pgc'):
    super().__init__()
    self.db = pymysql.connect(host, user, passwd, db)
    self.cursor = self.db.cursor()
    self.callback = exceptionCallback

  def getMaxID(self):
    return 

  def selectVideoByID(self, idx):
    sql = "SELECT * FROM `videoitem` WHERE `id`='%s'"%(idx)
    self.cursor.execute(sql)
    results = self.cursor.fetchone()
    return results

  def selectVideo(self, item):
    url = item['url']
    sql = "SELECT * FROM `videoitem` WHERE `url`='%s'"%(url)
    self.cursor.execute(sql)
    results = self.cursor.fetchone()
    return results

  def selectPeople(self, name):
    sql = "SELECT * FROM `peopleitem` WHERE `name`='%s'"%(name)
    self.cursor.execute(sql)
    results = self.cursor.fetchone()
    return results

  def insertVideo(self, item, idx=None):
    if idx == None:
      sql = "INSERT INTO `videoitem` (`id`, `url`, `title`, `time`, `type`, `lang`, `score`, `area`, `descp`, `tags`, `directors`, `actors`) VALUES (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
        (item['url'], item['v_title'], item['v_time'], item['v_type'], item['v_lang'], item['v_score'], item['v_area'], item['v_desc'], ','.join(item['v_tags']), ','.join(item['v_directors']), ','.join(item['v_actors']))
    else:
      sql = "INSERT INTO `videoitem` (`id`, `url`, `title`, `time`, `type`, `lang`, `score`, `area`, `descp`, `tags`, `directors`, `actors`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
        (idx, item['url'], item['v_title'], item['v_time'], item['v_type'], item['v_lang'], item['v_score'], item['v_area'], item['v_desc'], ','.join(item['v_tags']), ','.join(item['v_directors']), ','.join(item['v_actors']))
    
    try:
      self.cursor.execute(sql)
      self.db.commit()
    except:
      self.db.rollback()
      print(sql)
      if self.callback is not None:
        self.callback()

 

  def updateVideo(self, item):
    pass

  def _insertSinglePerson(self, name, idx):
    sql = "INSERT INTO `peopleitem` (`name`, `video`) VALUES ('%s', '%s')" % (name, idx)
    try:
      self.cursor.execute(sql)
      self.db.commit()
    except:
      self.db.rollback()
      if self.callback is not None:
        self.callback()
  
  def _updateSinglePerson(self, name, idx):
    sql = "UPDATE `peopleitem` SET `video`='%s' WHERE `name`='%s'"%(idx, name)
    try:
      self.cursor.execute(sql)
      self.db.commit()
    except:
      self.db.rollback()
      if self.callback is not None:
        self.callback()


  def _handleSinglePerson(self, name, idx):
    result = self.selectPeople(name)
    if result == None:
      self._insertSinglePerson(name, idx)
    else:
      idxList = result[1].split(',')
      if idx not in idxList:
        idxList.append(idx)
        self._updateSinglePerson(name, ','.join(idxList))
    

  def handlePeople(self, item):
    actors = item['v_actors']
    directors = item['v_directors']
    idx = self.selectVideo(item)
    if idx is None:
      return
    else:
      idx = str(idx[0])
    for actor in actors:
      self._handleSinglePerson(actor, idx)
    for dire in directors:
      self._handleSinglePerson(dire, idx)

  def handleVideo(self, item):
    result = self.selectVideo(item)
    if result == None:
      self.insertVideo(item)
    else:
      self.updateVideo(item)

  def closeDB(self):
    self.db.close()