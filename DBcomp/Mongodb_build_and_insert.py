'''
Created on Mar 16, 2017

@author: haopeng
'''
from pymongo import MongoClient
import time
import pymongo
# insert index_100k
def insert(name):
    client = MongoClient()
    db = client.Amazon
    insert = open("/home/haopeng/UCR-Courses/CS236/Project/Data/"+name+".json")
    line = insert.readline()
    info = eval(line)
    db[name].insert_one(info)
    if "index" in name:
        db[name].create_index("word")
    else:
        db[name].create_index("asin")
    t0 = time.time()
    while(True):
        try:
            line = insert.readline()
            info = eval(line)
            if "index" in name:
                word = info["word"]
                if(len(word)<256):
                    db[name].insert_one(info)
                    db[name].create_index("word")
            else:
                db[name].insert_one(info)
                db[name].create_index("asin")
        except:
            print line  
            break
    t1 = time.time()
    return t1 - t0
 
'''
insert("index_100k")
print "done"
insert("index_350k")
print "done"

insert("index_500k")
print "done"

insert("index_1500k")
print "done"
'''

'''
t0 = insert("item_100k")
print "time for insert 100k data: " +str(t0)

t1 = insert("item_350k")
print "time for insert 350k data: " +str(t1)
'''
t2 = insert("item_500k")
print "time for insert 500k data: " +str(t2)
t3 = insert("item_1500k")
print "time for insert 1500k data: " +str(t3)

