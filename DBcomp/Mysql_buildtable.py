'''
Created on Mar 19, 2017

@author: haopeng
'''
import MySQLdb


db = MySQLdb.connect("localhost","root","19921005","Amazon" )
cursor = db.cursor()
#100k
sql = """CREATE TABLE index_100k (
         word  varchar(256) PRIMARY KEY,
         asin  MEDIUMTEXT
          )ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE utf8_bin;
"""
try:
    cursor.execute(sql)
except:
    print "exsit"
#50k
sql = """CREATE TABLE index_350k (
         word  varchar(256) PRIMARY KEY,
         asin  MEDIUMTEXT
          )ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE utf8_bin;
"""
try:
    cursor.execute(sql)
except:
    print "exsit"
#500k
sql = """CREATE TABLE index_500k (
         word  varchar(256) PRIMARY KEY,
         asin  MEDIUMTEXT
          )ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE utf8_bin;
"""
try:
    cursor.execute(sql)
except:
    print "exsit"
#1500k
sql = """CREATE TABLE index_1500k (
         word  varchar(256) PRIMARY KEY,
         asin  MEDIUMTEXT
          )ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE utf8_bin;
"""

try:
    cursor.execute(sql)
except:
    print "exsit"

#100k
sql = """CREATE TABLE item_100k (
         asin varchar(200) PRIMARY KEY,
         title TEXT,
         description MEDIUMTEXT,
         price FLOAT,
         category varchar(100),
         image TEXT
          );
"""
try:
    cursor.execute(sql)
except:
    print "exsit"
#350k
sql = """CREATE TABLE item_350k (
         asin varchar(200) PRIMARY KEY,
         title TEXT,
         description MEDIUMTEXT,
         price FLOAT,
         category varchar(100),
         image TEXT
          );
"""
try:
    cursor.execute(sql)
except:
    print "exsit"
#500k
sql = """CREATE TABLE item_500k (
         asin varchar(200) PRIMARY KEY,
         title TEXT,
         description MEDIUMTEXT,
         price FLOAT,
         category varchar(100),
         image TEXT
          );
"""
try:
    cursor.execute(sql)
except:
    print "exsit"
#1500k
sql = """CREATE TABLE item_1500k (
         asin varchar(200) PRIMARY KEY,
         title TEXT,
         description MEDIUMTEXT,
         price FLOAT,
         category varchar(100),
         image TEXT
          );
"""

try:
    cursor.execute(sql)
except:
    print "exsit"
db.close()