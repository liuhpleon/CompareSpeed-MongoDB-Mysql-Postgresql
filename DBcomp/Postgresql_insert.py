'''
Created on Mar 16, 2017

@author: haopeng
'''
import psycopg2
import time
#insert index_100k
def index_100k():
    db = psycopg2.connect("dbname='Amazon' user='haopeng' host='localhost' password='19921005'")
    cur = db.cursor()
    index_100k = open("/home/haopeng/UCR-Courses/CS236/Project/Data/index_100k.json")
    line = index_100k.readline()
    while(True):
        try:
            info = eval(line)
            asin = info["asin"]
            word = info["word"]
            insert = (word,asin)
            cur.execute('INSERT INTO index_100k(word,asin) VALUES (%s,%s)', insert)
            line = index_100k.readline()
        except:  
            break
    cur.close()
    db.commit()

#insert item_100k
def item_100k():
    db = psycopg2.connect("dbname='Amazon' user='haopeng' host='localhost' password='19921005'")
    cur = db.cursor()
    item_100k = open("/home/haopeng/UCR-Courses/CS236/Project/Data/item_100k.json")
    line = item_100k.readline()
    while(True):
        try:
            info = eval(line)
            asin = info["asin"]
            category = info["category"]
            title = info["title"]
            description = info["description"]
            image = info["image"]
            price = info["price"]
            insert = (asin,title,description,price,category,image)
            cur.execute('INSERT INTO item_100k(asin,title,description,price,category,image) VALUES (%s,%s,%s,%s,%s,%s)', insert)
            line = item_100k.readline()
        except:  
            break
    cur.close()
    db.commit()

#insert index_350k
def index_350k():
    db = psycopg2.connect("dbname='Amazon' user='haopeng' host='localhost' password='19921005'")
    cur = db.cursor()
    index_350k = open("/home/haopeng/UCR-Courses/CS236/Project/Data/index_350k.json")
    line = index_350k.readline()
    while(True):
        try:
            info = eval(line)
            asin = info["asin"]
            word = info["word"]
            insert = (word,asin)
            cur.execute('INSERT INTO index_350k(word,asin) VALUES (%s,%s)', insert)
            line = index_350k.readline()
        except:  
            break
    cur.close()
    db.commit()

#insert item_350k
def item_350k():
    db = psycopg2.connect("dbname='Amazon' user='haopeng' host='localhost' password='19921005'")
    cur = db.cursor()
    item_350k = open("/home/haopeng/UCR-Courses/CS236/Project/Data/item_350k.json")
    line = item_350k.readline()
    while(True):
        try:
            info = eval(line)
            asin = info["asin"]
            category = info["category"]
            title = info["title"]
            description = info["description"]
            image = info["image"]
            price = info["price"]
            insert = (asin,title,description,price,category,image)
            cur.execute('INSERT INTO item_350k(asin,title,description,price,category,image) VALUES (%s,%s,%s,%s,%s,%s)', insert)
            line = item_350k.readline()
        except:  
            break
    cur.close()
    db.commit()
    
#insert index_500k
def index_500k():
    db = psycopg2.connect("dbname='Amazon' user='haopeng' host='localhost' password='19921005'")
    cur = db.cursor()
    index_500k = open("/home/haopeng/UCR-Courses/CS236/Project/Data/index_500k.json")
    line = index_500k.readline()
    while(True):
        try:
            info = eval(line)
            asin = info["asin"]
            word = info["word"]
            insert = (word,asin)
            cur.execute('INSERT INTO index_500k(word,asin) VALUES (%s,%s)', insert)
            line = index_500k.readline()
        except:  
            break
    cur.close()
    db.commit()


#insert item_500k
def item_500k():
    db = psycopg2.connect("dbname='Amazon' user='haopeng' host='localhost' password='19921005'")
    cur = db.cursor()
    item_500k = open("/home/haopeng/UCR-Courses/CS236/Project/Data/item_500k.json")
    line = item_500k.readline()
    while(True):
        try:
            info = eval(line)
            asin = info["asin"]
            category = info["category"]
            title = info["title"]
            description = info["description"]
            image = info["image"]
            price = info["price"]
            insert = (asin,title,description,price,category,image)
            cur.execute('INSERT INTO item_500k(asin,title,description,price,category,image) VALUES (%s,%s,%s,%s,%s,%s)', insert)
            line = item_500k.readline()
        except:  
            break
    cur.close()
    db.commit()

#insert index_1500k
def index_1500k():
    db = psycopg2.connect("dbname='Amazon' user='haopeng' host='localhost' password='19921005'")
    cur = db.cursor()
    index_1500k = open("/home/haopeng/UCR-Courses/CS236/Project/Data/index_1500k.json")
    line = index_1500k.readline()
    while(True):
        try:
            info = eval(line)
            asin = info["asin"]
            word = info["word"]
            insert = (word,asin)
            cur.execute('INSERT INTO index_1500k(word,asin) VALUES (%s,%s)', insert)
            line = index_1500k.readline()
        except:  
            break
    cur.close()
    db.commit()


#insert item_1500k
def item_1500k():
    db = psycopg2.connect("dbname='Amazon' user='haopeng' host='localhost' password='19921005'")
    cur = db.cursor()
    item_1500k = open("/home/haopeng/UCR-Courses/CS236/Project/Data/item_1500k.json")
    line = item_1500k.readline()
    while(True):
        try:
            info = eval(line)
            asin = info["asin"]
            category = info["category"]
            title = info["title"]
            description = info["description"]
            image = info["image"]
            price = info["price"]
            insert = (asin,title,description,price,category,image)
            cur.execute('INSERT INTO item_1500k(asin,title,description,price,category,image) VALUES (%s,%s,%s,%s,%s,%s)', insert)
            line = item_1500k.readline()
        except:  
            break
    cur.close()
    db.commit()
     
index_100k()
print "100k done"
index_350k()
print "350k done"
index_500k()
print "500k done"
index_1500k()
print "1500k done"
t0 = time.time()
item_100k()
t1 = time.time()
item_350k()
t2 = time.time()
item_500k()
t3 = time.time()
item_1500k()  
t4 = time.time()
print "time for insert 100k data: " +str(t1-t0)
print "time for insert 350k data: " +str(t2-t1)
print "time for insert 500k data: " +str(t3-t2)
print "time for insert 1500k data: " +str(t4-t3)