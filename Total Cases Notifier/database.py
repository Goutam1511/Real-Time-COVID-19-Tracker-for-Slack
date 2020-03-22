import sqlite3 as sql
import json
from datetime import datetime

class dbconnect:
    conn   = None
    exception = False
    def __init__(self):
        try:
            self.conn = sql.connect('covid19.db')
            c = self.conn.execute('''SELECT COUNT(name) FROM sqlite_master WHERE type = 'table' AND name = 'COVID19';''')
            
            if c.fetchone()[0] == 0:
                self.conn.execute('''CREATE TABLE COVID19
                                     (TIMESTAMP TEXT NOT NULL,
                                      INDIAN_CASES INT NOT NULL,
                                      CURED INT NOT NULL,
                                      DIED INT NOT NULL);''')
        except:
            print "Exception Occured in Connection establishment to Database"
            self.exception = True


    def insert_into_db(self, current_stat):
        try:
            sql = '''INSERT INTO COVID19 (TIMESTAMP, INDIAN_CASES, CURED, DIED)
                   VALUES(?, ?, ?, ?)'''
            self.conn.execute(sql, current_stat)
            self.conn.commit()
        except:
            print "Exception Occured in Data Insertion"
            self.exception = True

    def retrieve_from_db(self):
        try:
            sql = '''SELECT * FROM COVID19;'''
            return self.conn.execute(sql)
        except:
            print "Data Retrieval Failure"
            self.exception = True
