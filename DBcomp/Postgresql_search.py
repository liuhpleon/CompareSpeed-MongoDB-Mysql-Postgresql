'''
Created on Mar 16, 2017

@author: haopeng
'''
import psycopg2
import time
import json
db = psycopg2.connect("dbname='Amazon' user='haopeng' host='localhost' password='19921005'")
cur = db.cursor()

class postgresql_select():
    asins = []
    def __init__(self,database):
        self.database = database
        
    def index(self,word):
        global asins
        try:
            cur.execute("SELECT asin FROM index_"+self.database+" WHERE word = '"+word+"'")
            query = cur.fetchone()[0]
            asins = eval(query)
        except:
            asins = []
        
    def item(self):
        global asins
        t1 = time.time()
        for asin in asins:
            cur.execute("SELECT * FROM item_"+self.database+" WHERE asin = '"+asin+"'")
        t2 = time.time()
        info = {"count":len(asins),"time":t2-t1}
        return json.dumps(info)   