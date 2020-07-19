from pgc_scrapy.items import PgcScrapyItem
from pgc_scrapy.utils.db_helper import DBHelper

import random
from tqdm import tqdm
import time

def randomCheckVideo(db, idx):
  idx = str(idx)
  _ = getInfo(db, idx)
  for name in _:
    __ = getPeopleInfo(db, name)
    if __ is None:
      print('asd', idx, name, _)
      
      db._insertSinglePerson(name, idx)

    elif idx not in __:
      print('check failed')
      print(idx, name)
      db._handleSinglePerson(name, idx)
      return False
  # print(idx, 'check succ')
  return True

def checkPeople(db, name):
  _ = getPeopleInfo(db, name)
  for idx in _:
    __ = getInfo(db, idx)
    if name not in __:
      print('check failed')
      print(idx, name)
      return False
  # print(name, 'check succ')
  return True

def getInfo(db, idx):
  res = db.selectVideoByID(idx)
  if res is None:
    return None
  else:
    ret = res[-2].split(',') + res[-1].split(',')
    ret = [i for i in ret if i != '']
    return ret

def getPeopleInfo(db, name):
  
  res = db.selectPeople(name)
  if res is None:
    return None
  else:
    return res[1].split(',')


def testSearch(db, name):
  pass

if __name__ == "__main__":
  db = DBHelper(None, '127.0.0.1', 'root', '', 'pgc')

  flag = True 
  print('\nStarting Test...')
  print()
  print('*'*50)
  for i in tqdm(range(300)):
    idx = random.randint(1, 28000)
    if not randomCheckVideo(db, idx):
      flag = False
      break
      
  print('*'*50)

  nameList = []
  for i in range(100):
    idx = random.randint(1, 28000)
    nameList += getInfo(db, idx)

  for name in tqdm(nameList):
    if not checkPeople(db, name):
      flag = False
      break
  print('*'*50)
  # print()
  if flag:
    print('Test Passed')
  else:
    print('Test Failed')
  print()

  # for name in nameList:
  #   print('name:', name)
  #   begin = time.time()
  #   retList = getPeopleInfo(db, name)
  #   # print(retList, len(retList))
  #   sql = "SELECT * from `videoitem` WHERE `id` IN ('%s')"%("','".join(retList))
  #   # print(sql)
  #   ans = db.SQL(sql)
  #   print('inverted index:', time.time()-begin)

  #   begin = time.time()
  #   sql = "SELECT * FROM `videoitem` WHERE `actors` LIKE '%%%s%%'"%(name)
  #   ans = db.SQL(sql)
  #   # print(ans)
  #   print('like search', time.time()-begin)
  #   print()