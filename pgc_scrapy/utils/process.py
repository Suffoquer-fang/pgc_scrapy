import pymysql 

if __name__ == "__main__":
    db = pymysql.connect('rm-bp1i2b60x7f66982fto.mysql.rds.aliyuncs.com', 'fangyan', 'fangyan123', 'pgc')
    
    cursor = db.cursor()

    sql = "SELECT * FROM `videoitem` WHERE `url`='%s'"%('eee')
    try:
      cursor.execute(sql)
      results = cursor.fetchone()
      print(results)
      sql = "SELECT * FROM `videoitem` WHERE `url`='%s'"%('www')
      cursor.execute(sql)
      results = cursor.fetchone()
      print(results)
    except:
      db.rollback()

    sql = "INSERT INTO `videoitem` (`id`, `url`, `title`, `year`) VALUES (NULL, 'wewe', 'veefe', %s)" %('2020')
    # sql = "INSERT INTO `videoitem` (`id`, `url`, `title`, `time`) VALUES (NULL, 'wqfweg', 'egege', '2000')"
    try:
      cursor.execute(sql)
      db.commit()
    except:
      print('error')
      db.rollback()

    db.close()