"""
Environment Setup for Hello World Flask Application
Hello World Flask Uygulamasının Ortam Kurulumu

Sunucu tarafı API'leri oluşturmak için Python programlama dilinden nasıl yararlanabileceğimizi
öğreneceğimiz Flask'taki API geliştirme hakkındaki bu kursa hoş geldiniz.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hey Mustafa"


if __name__ == '__main__':
    app.run(debug=True)

