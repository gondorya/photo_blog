# Photo Blog

Simple blogging app with Django and Angular

Setup:
i. Go to frontend/blog folder
* install npm packages
`npm install`
* run project
`ng build --prod --output-path ../../backend/blog/static/ang --watch --output-hashing none`

ii. Go to backend folder
* create virtualenv:
`$ python3 -m venv myvenv`

* run virtualenv:
** Linux, OS X
`source myvenv/bin/activate`
** Windows
`C:\Users\Name\djangogirls> myvenv\Scripts\activate`

* install Django:
`(myvenv) ~$ python -m pip install --upgrade pip`
`pip install -r requirements.txt`

* run project:
`python manage.py runserver`
