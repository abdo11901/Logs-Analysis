# Database code for the DB Forum.
#
# This is still NOT the full solution!

import psycopg2
import bleach

DBNAME = "news"


# 1st function which gets the most popular three articles of all time
def get_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''
        SELECT a.title,count(*) AS views
        FROM log l INNER JOIN articles a
        ON l.path like concat('%', a.slug)
        WHERE l.status = '200 OK' GROUP BY
        a.title ORDER BY views DESC LIMIT 3;
        ''')
    posts = c.fetchall()
    db.close()
    return posts


# 2nd function which gets the most popular article authors of all time
def get_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''
        SELECT au.name,count(*) as views FROM log lo
        INNER JOIN articles ar ON lo.path LIKE
        concat('%',ar.slug) INNER JOIN authors au
        ON ar.author = au.id GROUP BY au.name ORDER BY views DESC ;'''
              )
    posts = c.fetchall()
    db.close()
    return posts


# 3rd function which gets the days did more than 1% of requests lead to errors
def get_errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT * FROM ratio WHERE percentage > 1 ;")
    posts = c.fetchall()
    db.close()
    return posts
