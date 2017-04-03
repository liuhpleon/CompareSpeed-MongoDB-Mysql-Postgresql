'''
Created on Mar 16, 2017

@author: haopeng
'''
import psycopg2
db = psycopg2.connect("dbname='Amazon' user='haopeng' host='localhost' password='19921005'")
cur = db.cursor()
#Create index_100k
cur.execute('''CREATE TABLE "index_100k" (
                 word varchar PRIMARY KEY, 
                 asin varchar);''')
#Create_item_100k
cur.execute('''CREATE TABLE "item_100k" (
                 asin varchar PRIMARY KEY, 
                 title varchar,
                 description varchar,
                 price real,
                 category varchar,
                 image varchar);''')
#Create index_350k
cur.execute('''CREATE TABLE "index_350k" (
                 word varchar PRIMARY KEY, 
                 asin varchar);''')
#Create_item_350k
cur.execute('''CREATE TABLE "item_350k" (
                 asin varchar PRIMARY KEY, 
                 title varchar,
                 description varchar,
                 price real,
                 category varchar,
                 image varchar);''')
#Create index_500k
cur.execute('''CREATE TABLE "index_500k" (
                 word varchar PRIMARY KEY, 
                 asin varchar);''')
#Create_item_500k
cur.execute('''CREATE TABLE "item_500k" (
                 asin varchar PRIMARY KEY, 
                 title varchar,
                 description varchar,
                 price real,
                 category varchar,
                 image varchar);''')
#Create index_1500k
cur.execute('''CREATE TABLE "index_1500k" (
                 word varchar PRIMARY KEY, 
                 asin varchar);''')
#Create_item_100k
cur.execute('''CREATE TABLE "item_1500k" (
                 asin varchar PRIMARY KEY, 
                 title varchar,
                 description varchar,
                 price real,
                 category varchar,
                 image varchar);''')
cur.close()
db.commit()