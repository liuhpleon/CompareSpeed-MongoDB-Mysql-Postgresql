'''
Created on Mar 16, 2017

@author: haopeng
'''
from pymongo import MongoClient
import time
import json
client = MongoClient()
db = client.Amazon
class mongo_select():
    def __init__(self,collection_name):
        self.name = "index_"+collection_name
                
    def search(self,word):
        collection = db[self.name]
        word = str(word)
        asins = []
        print self.name
        try:
            #tx = time.time()
            cur = collection.find_one({"word":word})["asin"]
            #ty = time.time()
            #print str(ty-tx)
            asins = eval(cur)
        except:
            asins = []
        print asins
        t1 = time.time()
        for asin in asins:
            #t3 = time.time()
            collection.find_one({"asin":asin})
            #t4 = time.time()
            #print str(t4 - t3)
        t2 = time.time()
        info = {"count":len(asins),"time":t2-t1}
        return json.dumps(info)
#a = mongo_select("350k")
#print a.search("a")