#!/usr/bin/env python3
# 
# A buggy web service in need of a database.

from flask import Flask, request

import newsdb

app = Flask(__name__)

# the 1st route which gets the most popular three articles of all time




# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>DB Forum</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>

    <!-- post content will go here -->
    <h1>Most popular articles</h1>
    
    %s
  
      <br>
  
    <h1>Most popular authors</h1>
    
    %s
    
    <br>
  
    <h1>Errors more than 1</h1>
  
    %s
  
  
  </body>
</html>
'''

# HTML template for an individual comment
question1 = '''
     <div class=post><em class=date>Title : %s</em><br>Views : %s</div>
'''
question2 = '''
     <div class=post><em class=date>Author Name : %s</em><br>Views : %s</div>
'''
question3 = '''
     <div class=post><em class=date>Date : %s</em><br>Percentage : %s</div>
'''


@app.route('/', methods=['GET'])
def main():
    q1 = "".join(question1 % (title, views) for title, views in newsdb.get_articles())
    q2 = "".join(question2 % (name, views) for name, views in newsdb.get_authors())
    q3 = "".join(question3 % (day, percentage) for day, percentage in newsdb.get_errors())
    html = HTML_WRAP % (q1 , q2 , q3)
    # , q2, q3)
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
