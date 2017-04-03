'''
Created on Mar 19, 2017

@author: haopeng
'''
import MySQLdb
import time
import json
db = MySQLdb.connect('localhost','root','19921005','Amazon')
cursor = db.cursor()
class Mysql_select():
    asins = []
    def __init__(self,database):
        self.database = database
    def index(self,word):
        global asins
        query = ("SELECT asin FROM index_"+self.database+" WHERE word = '"+word+"'")
        try:
            t1 = time.time()
            cursor.execute(query)
            t2 = time.time()
            print t2 - t1
            asins = eval(cursor.fetchone()[0])
        except:
            asins = []
            
    def item(self):
        global asins
        t1 = time.time()
        for asin in asins:
            query = ("SELECT * FROM item_"+self.database+" WHERE asin = '"+asin+"'")
            cursor.execute(query)
        t2 = time.time()
        return json.dumps({"count":len(asins),"time":t2-t1}) 