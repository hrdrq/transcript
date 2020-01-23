# -*- coding: utf-8 -*-
import pdb
d = pdb.set_trace
from mysql import connector

from credentials import HOST, PORT, USER, PASSWORD

CREATE_SQL = \
'''
    CREATE TABLE {} (
      id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
      word VARCHAR(32),
      count INT UNSIGNED,
      s1 TEXT,
      ep1 VARCHAR(8),
      s2 TEXT,
      ep2 VARCHAR(8),
      s3 TEXT,
      ep3 VARCHAR(8),
      s4 TEXT,
      ep4 VARCHAR(8),
      s5 TEXT,
      ep5 VARCHAR(8),
      KEY word (word)
    )
'''

class DB():

    def __init__(self, name):
        super().__init__()
        conn = connector.connect(
            host = HOST,
            port = PORT,
            user = USER,
            password = PASSWORD,
            database = 'transcript',
        )
        if not conn.is_connected():
            raise Exception('db is not connected!')
        self.cur = conn.cursor(dictionary=True)
        self.conn = conn
        self.name = name

        self.check()

    def check(self):
        cur = self.conn.cursor()
        cur.execute("SHOW TABLES")
        if self.name not in [t[0] for t in list(cur)]:
            cur.execute(CREATE_SQL.format(self.name))
        cur.close()

    def add(self, season, episode, sentence, word):
        word = word.replace('"', '')
        if len(word) > 32:
            return
        sql = 'SELECT * FROM {} WHERE word="{}"'.format(self.name, word)
        try:
            self.cur.execute(sql)
            res = self.cur.fetchone()
        except Exception as e:
            print(word)
            raise e
        sentence = sentence.replace('"', '`')
        if res is None:
            sql = 'INSERT INTO {} (word, count, s1, ep1) VALUES ("{}", 1, "{}", "{}")' \
                  .format(self.name, word, sentence, season + episode)
        else:
            set_s = None
            for s in ['1', '2', '3', '4', '5']:
                s_db = res['s' + s]
                if s_db == sentence:
                    break
                if s_db is None:
                    set_s = s
                    break
            if set_s:
                sql = 'UPDATE {} SET count={}, {}="{}", {}="{}" where id={}' \
                      .format(self.name, res['count'] + 1, 's' + set_s, sentence, 'ep' + set_s, season + episode, res['id'])
            else:
                sql = 'UPDATE {} SET count={} where id={}' \
                      .format(self.name, res['count'] + 1, res['id'])
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(season, episode, word)
            print(sentence)
            raise e


