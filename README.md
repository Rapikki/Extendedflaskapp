APPLICATION with Flask and PostgreSQL for DevOps practise

INASTALL REQUIRMENTS
python setup.py install

============

PostgreSQL configure 
(CentOS) sudo yum install postgresql postgresql-contrib psycopg2-binary

Create DB with name books_store
IN TERMINAL (for creating tables in db)
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

============

Run 

python manage.py runserver
