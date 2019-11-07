from flask import Flask, request, render_template 
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route("/members")
def user_url():
    lists = [[1,'太郎'], [2,'次郎'], [3,'三郎']]
    return render_template("member.html", lists=lists)


@app.route("/member_detail/<int:id>/<name>")
def detail(id,name):
    lists = [['太郎',24,'サッカー'], ['次郎',45,'野球'], ['三郎',67,'バスケ']]
    index = id-1
    data = lists[index]
    return render_template("detail.html", data=data, name=name)




