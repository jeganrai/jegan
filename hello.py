from flask import Flask,render_template
import requests
import json
from pymongo import MongoClient


app=Flask(__name__)
conn=MongoClient("mongodb+srv://jeganrai:mongodb@cluster0-3qmcu.mongodb.net/test?retryWrites=true&w=majority")
database=conn['db']
collection=database['roughcoll']
data={"Name":"rajihhh"}
collection.insert_one(data)
print(conn.list_database_names())
dblist = conn.list_database_names()
@app.route('/ram/')
def iram():
    return render_template('ram.html',love=dblist)
@app.route('/angular/')
def angular():
    return render_template('angular.html')
@app.route('/')
def index():
    r=requests.get("http://api.icndb.com/jokes/random")
    data=json.loads(r.text)
    joke=data['value']['joke']
    return render_template('index.html',joke=joke)


if __name__ == '__main__':
    app.run()
