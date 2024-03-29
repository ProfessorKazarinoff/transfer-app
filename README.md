# transfer-app

A web application built with Python and Django to show which community college courses transfer to which 4-year college courses in Oregon.

## To get started

Create virtual env and install requirements.txt

```text
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata courses/fixtures/database_data.json
python manage.py collectstatic
python manage.py runserver
```

## To save the data in the database to a fixture:

```text
python manage.py dumpdata --indent 2 > courses/fixtures/database_data.json
```

## To deploy to Heroku, install the Heroku CLI:

```text
heroku login
heroku create
heroku # set SECRET_KEY environment variable
git push heroku master:main
heroku run manage.py migrate
heroku run manage.py loaddata courses/fixtures/database_data.json
heroku open
```
