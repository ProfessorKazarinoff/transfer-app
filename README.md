# transfer-app

An example web application built with Python and Django to show which community college courses transfer to which 4-year college courses

## To get started

Create virtual env and install requirements.txt

```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata course/fixtures/database_data.json
python manage.py runserver
```

To save the data in the database to a fixture:

```
python manage.py dumpdata --indent 2 > course/fixtures/database_data.json
```
