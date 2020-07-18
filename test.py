from pgc_scrapy.items import PgcScrapyItem
from pgc_scrapy.utils.db_helper import DBHelper

import random
from tqdm import tqdm

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

if __name__ == "__main__":
  db = DBHelper(None, '127.0.0.1', 'root', '', 'pgc')

  print('*'*50)
  for i in tqdm(range(300)):
    idx = random.randint(1, 28000)
    if not randomCheckVideo(db, idx):
      
      break
      
  print('*'*50)

  nameList = []
  for i in range(100):
    idx = random.randint(1, 28000)
    nameList += getInfo(db, idx)

  for name in tqdm(nameList):
    if not checkPeople(db, name):
      break
  print('*'*50)

