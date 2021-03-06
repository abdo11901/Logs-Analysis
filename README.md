Project name:  
====================
Logs-Analysis: The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

Prerequisite:  
====================
* Python 3
* news database https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
* vagrant https://www.vagrantup.com/downloads.html
* virtualbox  https://www.virtualbox.org/wiki/Download_Old_Builds_5_1

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
before doing anything we should create a view called ratio 
  * open up your terminal and write the following:
  * vagrant up
  * vagrant ssh
  * cd to the database directory
  * psql -d news -f newsdata.sql
  * psql news
  * then create the view.
  
  * How to create the view:
  * just write the query but you ***should write it in one line*** don't make new lines in the terminal this will case an error.
    
    create view ratio as select Date(time) as day, cast(sum(case when status != '200 OK' then 1 else 0 end) as decimal) /cast(count(status) as decimal)*100  as percentage from log l group by day order by percentage desc ;

 1-Run the vagrant: 
  * -vagrant up
  * -vagrant ssh
  * -cd /vagrant/
  * -cd Logs-Analysis/
  * -python news.py
    
 2-open your browser and write:
  * -localhost:8000/
