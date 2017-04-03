'''
Created on Mar 20, 2017

@author: haopeng
'''
'''
in this part we will create an item and insert it into the item 100k,350k,500k and 1500k table and see the speed
'''
from pymongo import MongoClient
import psycopg2
import MySQLdb
import time
item = {
    "asin":"1234567890",
    "title":"NOUPDATE",
    "description":"qwertyuiop",
    "price":"12.5",
    "category":"abdcd",
    "image":"http;//null//"
    }
asin = item["asin"]
title = item["title"]
description = item["description"]
price = item["price"]
category = item["category"]
image = item["image"]
class mysql():
    def __init__(self,name):
        self.name = "item_"+name
        print "mysql: "+self.name
    def insert(self):
        conn = MySQLdb.connect("localhost","root","19921005","Amazon" )
        c = conn.cursor()
        insert = (asin,title,description,price,category,image)
        t0 = time.time()
        c.execute("INSERT INTO "+self.name+" VALUES (%s,%s,%s,%s,%s,%s)",insert)
        conn.commit()
        conn.close()
        t1 = time.time()
        return t1 - t0

    def update(self):
        #UPDATE table1 SET col_a='k1', col_b='foo' WHERE key_col='1';
        conn = MySQLdb.connect("localhost","root","19921005","Amazon" )
        c = conn.cursor()
        t0 = time.time()
        c.execute('UPDATE '+self.name+' SET title ="UPDATED" WHERE asin = "1234567890"')
        conn.commit()
        conn.close()
        t1 = time.time()
        return t1 - t0

    def delete(self):
        conn = MySQLdb.connect("localhost","root","19921005","Amazon" )
        c = conn.cursor()
        t0 = time.time()
        c.execute('DELETE FROM '+self.name+' WHERE asin = "1234567890"')
        conn.commit()
        conn.close()
        t1 = time.time()
        return t1 - t0

class postgresql():
    def __init__(self,name):
        self.name = "item_"+name
        print "postgresql: "+self.name
    def insert(self):
        db = psycopg2.connect("dbname='Amazon' user='haopeng' host='localhost' password='19921005'")
        cur = db.cursor()
        insert = (asin,title,description,price,category,image)
        t0 = time.time()
        try:
            cur.execute('INSERT INTO '+self.name+'(asin,title,description,price,category,image) VALUES (%s,%s,%s,%s,%s,%s)', insert)
        except:
            print "error"
        cur.close()
        db.commit()
        t1 = time.time()
        return t1- t0

    def update(self):
        db = psycopg2.connect("dbname='Amazon' user='haopeng' host='localhost' password='19921005'")
        cur = db.cursor()
        t0 = time.time()
        cur.execute("UPDATE "+self.name+" SET title ='UPDATED' WHERE asin = '1234567890'")
        cur.close()
        db.commit()
        t1 = time.time()
        return t1 - t0

    def delete(self):
        db = psycopg2.connect("dbname='Amazon' user='haopeng' host='localhost' password='19921005'")
        cur = db.cursor()
        t0 = time.time()
        cur.execute("DELETE FROM "+self.name+" WHERE asin = '1234567890'")
        cur.close()
        db.commit()
        t1 = time.time() 
        return t1 - t0
class mongodb():
    def __init__(self,name):
        self.name = "item_"+name
        print "mongodb: "+self.name
        
    def insert(self):
        client = MongoClient()
        db = client.Amazon
        t0 = time.time()
        try:
            db[self.name].insert_one(item)
        except:
            i = 1
        t1 = time.time()
        return t1 - t0
    
    def update(self):
        client = MongoClient()
        db = client.Amazon
        t0 = time.time()
        db[self.name].update_one({'asin': '1234567890'},{'$set': {'title': 'updated'}}, upsert=False)
        t1 = time.time()
        return t1 - t0

    def delete(self):
        client = MongoClient()
        db = client.Amazon
        t0 = time.time()
        db[self.name].delete_one({'asin': '1234567890'})
        t1 = time.time()
        return t1 - t0

m1 = mysql("100k")
m2 = mysql("350k")
m3 = mysql("500k")
m4 = mysql("1500k")
p1 = postgresql("100k")
p2 = postgresql("350k")
p3 = postgresql("500k")
p4 = postgresql("1500k")
g1 = mongodb("100k") 
g2 = mongodb("350k")
g3 = mongodb("500k") 
g4 = mongodb("1500k")

print "mysql insertion:"
print m1.insert()
print m2.insert()
print m3.insert()
print m4.insert()

print "postgresql insertion:"
print p1.insert()
print p2.insert()
print p3.insert()
print p4.insert()

print "mongodb insertion:"
print g1.insert()
print g2.insert()
print g3.insert()
print g4.insert()

print "----------------------"

print "mysql update:"
print m1.update()
print m2.update()
print m3.update()
print m4.update()

print "posrgresql update:"
print p1.update()
print p2.update()
print p3.update()
print p4.update()

print "mongodb update:"
print g1.update()
print g2.update()
print g3.update()
print g4.update()

print "----------------------"


print "mysql delete:"
print m1.delete()
print m2.delete()
print m3.delete()
print m4.delete()

print "postgresql delete:"
print p1.delete()
print p2.delete()
print p3.delete()
print p4.delete()

print "mongodb delete:"
print g1.delete()
print g2.delete()
print g3.delete()
print g4.delete()
