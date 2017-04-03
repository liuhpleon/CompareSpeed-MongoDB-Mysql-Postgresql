'''
Created on Mar 19, 2017

@author: haopeng
'''
import time     
import MySQLdb


# insert index_100k
def index_100k():
    conn = MySQLdb.connect("localhost","root","19921005","Amazon" )
    c = conn.cursor()
    index_100k = open("/home/haopeng/UCR-Courses/CS236/Project/Data/index_100k.json")
    line = index_100k.readline()
    while(True):
        try:
            info = eval(line)
            asin = info["asin"]
            word = info["word"]
            insert = (word,asin)
            if len(word)<=255:
                c.execute("""INSERT INTO index_100k VALUES (%s,%s)""",insert)
            line = index_100k.readline()
        except:  
            print line
            break
        
    conn.commit()
    conn.close()
    
# insert item_100k
def item_100k():
    conn = MySQLdb.connect("localhost","root","19921005","Amazon" )
    c = conn.cursor()  
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
            c.execute("""INSERT INTO item_100k VALUES (%s,%s,%s,%s,%s,%s)""",insert)
            line = item_100k.readline()
        except:  
            break
    conn.commit()
    conn.close()

# insert index_350k
def index_350k():
    conn = MySQLdb.connect("localhost","root","19921005","Amazon" )
    c = conn.cursor()
    index_350k = open("/home/haopeng/UCR-Courses/CS236/Project/Data/index_350k.json")
    line = index_350k.readline()
    while(True):
        try:
            info = eval(line)
            asin = info["asin"]
            word = info["word"]
            insert = (word,asin)
            if len(word)<=255:
                c.execute("""INSERT INTO index_350k VALUES (%s,%s)""",insert)
            line = index_350k.readline()
        except:  
            print line
            break
        
    conn.commit()
    conn.close()

# insert item_350k
def item_350k():
    conn = MySQLdb.connect("localhost","root","19921005","Amazon" )
    c = conn.cursor()  
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
            c.execute("""INSERT INTO item_350k VALUES (%s,%s,%s,%s,%s,%s)""",insert)
            line = item_350k.readline()
        except:  
            break
    conn.commit()
    conn.close()
    
 
# insert index_500k
def index_500k():
    conn = MySQLdb.connect("localhost","root","19921005","Amazon" )
    c = conn.cursor()
    index_500k = open("/home/haopeng/UCR-Courses/CS236/Project/Data/index_500k.json")
    line = index_500k.readline()
    while(True):
        try:
            info = eval(line)
            asin = info["asin"]
            word = info["word"]
            insert = (word,asin)
            if len(word)<=255:
                c.execute("""INSERT INTO index_500k VALUES (%s,%s)""",insert)
            line = index_500k.readline()
            
        except:  
            print line
            break
            
        
    conn.commit()
    conn.close()

# insert item_500k
def item_500k():
    conn = MySQLdb.connect("localhost","root","19921005","Amazon" )
    c = conn.cursor()  
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
            c.execute("""INSERT INTO item_500k VALUES (%s,%s,%s,%s,%s,%s)""",insert)
            line = item_500k.readline()
        except:  
            break
    conn.commit()
    conn.close()
        
# insert index_1500k
def index_1500k():
    conn = MySQLdb.connect("localhost","root","19921005","Amazon" )
    c = conn.cursor()
    index_1500k = open("/home/haopeng/UCR-Courses/CS236/Project/Data/index_1500k.json")
    line = index_1500k.readline()
    while(True):
        try:
            info = eval(line)
            asin = info["asin"]
            word = info["word"]
            insert = (word,asin)
            if len(word)<=255:
                c.execute("""INSERT INTO index_1500k VALUES (%s,%s)""",insert)
            line = index_1500k.readline()
        except:  
            print line
            break
        
    conn.commit()
    conn.close()
        
    
def item_1500k():
    conn = MySQLdb.connect("localhost","root","19921005","Amazon" )
    c = conn.cursor()  
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
            c.execute("""INSERT INTO item_1500k VALUES (%s,%s,%s,%s,%s,%s)""",insert)
            line = item_1500k.readline()
        except:  
            break
    conn.commit()
    conn.close()

index_100k()
index_350k()
index_500k()
index_1500k()

t0 = time.time()
item_100k()
t1 = time.time()
print "time for insert 100k data: " +str(t1-t0)

t2 = time.time()
item_350k()
t3 = time.time()
print "time for insert 350 data: " +str(t3-t2)

t4 = time.time()
item_500k()
t5 = time.time()
print "time for insert 500k data: " +str(t5-t4)

t6 = time.time()
item_1500k()
t7 = time.time()
print "time for insert 1500k data: " +str(t7-t6)

  


