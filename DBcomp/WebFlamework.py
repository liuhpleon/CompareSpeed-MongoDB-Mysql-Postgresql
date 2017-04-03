'''
Created on Mar 16, 2017

@author: haopeng
'''
from flask import Flask, render_template, request, jsonify
from Postgresql_search import postgresql_select
from Mongodb_search import mongo_select
from Mysql_search import Mysql_select
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def search():
    if request.method =="POST":
        data = request.form
        print data
        word = data.get("word").__str__()
        size = data.get("datasize").__str__()
        '''
        startprice = data.get("startprice").__str__()
        endprice = data.get("endprice").__str__()
        startprice = int(startprice)
        endprice = int(endprice)
        print startprice 
        print endprice
        '''
        print word 
        print size 
        mysql = Mysql_select(size)
        mysql.index(word)
        mysql_info = mysql.item()
        print mysql_info
        postgresql = postgresql_select(size)
        postgresql.index(word)
        postgresql_info = postgresql.item()
        print postgresql_info
        mongodb = mongo_select(size)
        mongodb_info = mongodb.search(word)
        print mongodb_info
        return jsonify({"mysql":mysql_info,"postgresql":postgresql_info,"mongodb":mongodb_info})
    else:
        return render_template("search.html")


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port = 5000)