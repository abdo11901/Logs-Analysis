# Database code for the DB Forum.
#
# This is still NOT the full solution!

import psycopg2, bleach

DBNAME = "news"


def get_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''
        select a.title,count(*) as views
        from log l inner join articles a
        on l.path like concat('%', a.slug)
        where l.status = '200 OK' group by
        a.title order by views desc;
        ''')
    posts = c.fetchall()
    db.close()
    return posts


def get_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''
        select au.name,count(*) as views from log lo
        inner join articles ar on lo.path like 
        concat('%',ar.slug) inner join authors au 
        on ar.author = au.id group by au.name order by views desc ;'''
              )
    posts = c.fetchall()
    db.close()
    return posts


def get_errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from ratio where percentage > 1 ;")
    posts = c.fetchall()
    db.close()
    return posts
