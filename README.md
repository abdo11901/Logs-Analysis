Project name:  
====================
Logs-Analysis  

Prerequisite:  
====================
* Python 3
* vagrant
* virtualbox  

Files List:  
====================
* news.py 
* newsdb.py   
* README.md  

Files explanation  
====================
  * news.py  contains the routes (url)  
  * newsdb.py contains the functions which does the queries
  * README.md contains a description of our project  
  
  How to run it:  
====================
before doing anything we should create a view called ratio so we will open vagrant then open the "news" database with psql news and then wirte this query:
    
    create view ratio as select Date(time) as day, cast(sum(case when status != '200 OK' then 1 else 0 end
    ) as decimal) /cast(count(status) as decimal)*100  as percentage from log l group by day order by percentage d
    esc ;

 1-Run the vagrant: 
  * -vagrant up
  * -vagrant ssh
  * -cd /vagrant/
  * -cd Logs-Analysis/
  * -python news.py
    
 2-open your browser and write:
  * -localhost:8000/question-1
  * -localhost:8000/question-2
  * -localhost:8000/question-3

