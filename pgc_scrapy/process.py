from utils.db_helper import DBHelper
from items import PgcScrapyItem

def callback():
  print()
  print('error!')
  print()

if __name__ == "__main__":
  db = DBHelper(callback, '127.0.0.1', 'root', '', 'pgc')

  # item = PgcScrapyItem(url='atest', v_title='', v_, v_actors=['a1', 'a2'], v_directors=[])
  for url in ['1', '2', '3', '4', '1', '5']:
    item = PgcScrapyItem(url=url, v_title='v_title', v_lang='v_lang', 
              v_tags=['asd'], v_type='v_type', v_actors=['a2', 'b2', 'uad'], 
              v_directors=['d1', 'd2', 'qdg'], v_time=2000, v_score=9.0, v_area='v_area', v_desc = 'v_desc')

    db.handleVideo(item)
    db.handlePeople(item)
