# Photo Blog

Simple blogging app with Django and Angular

Setup:

1. Go to frontend/blog folder
* install npm packages
`npm install`
* run project
`ng build --prod --output-path ../../backend/blog/static/ang --watch --output-hashing none`

2. Go to backend folder
* create virtualenv:
`$ python3 -m venv myvenv`

* run virtualenv:
 `source myvenv/bin/activate`

* install Django:
`(myvenv) ~$ python -m pip install --upgrade pip`
`pip install -r requirements.txt`

* create superuser:
`python manage.py createsuperuser`

* run project:
`python manage.py runserver`
