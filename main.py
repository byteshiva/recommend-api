from flask import Flask
from flask import jsonify
from flask import request
import json
import pandas as pd
import numpy as np

app = Flask(__name__)

#url = 'https://gist.githubusercontent.com/jaidevd/23aef12e9bf56c618c41/raw/c05e98672b8d52fa0cb94aad80f75eb78342e5d4/books.csv'

url_large = 'https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv'

data = pd.read_csv(url_large, nrows=150)
data.fillna(value='field is empty', inplace = True)

books = data.values.tolist()

@app.route('/', methods=['GET'])
def home():
    return 'API for recommendation systems: search by title and it will return other similar books as json format'
    
@app.route('/api/books/all', methods=['GET'])
def api_all():
    return jsonify(books)
    
@app.route('/api/books', methods=['GET'])
def api_title():
    
    if 'title' in request.args:
        title = str(request.args['title'])
    else:
        return "Error: No title field provided. Please specify a title."

    results = []
    
    for book in books:
        if title.lower() in book[10].lower():
            results.append(book)

    return jsonify(results)
