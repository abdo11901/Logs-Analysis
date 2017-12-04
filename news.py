#!/usr/bin/env python3
# 
# A buggy web service in need of a database.

from flask import Flask, request, redirect, url_for

import newsdb

app = Flask(__name__)


@app.route('/question-1', methods=['GET'])
def articles():
    ar = newsdb.get_articles()
    return ','.join(str(v) for v in ar)


@app.route('/question-2', methods=['GET'])
def authors():
    au = newsdb.get_authors()
    return ','.join(str(v) for v in au)


@app.route('/question-3', methods=['GET'])
def errors():
    err  = newsdb.get_errors()
    return ','.join(str(v) for v in err)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
