Flask project is implemented to keep the list of companies.
Project is deployed in GOOGLE APP ENGINE and GOOGLE CLOUD SQL.

Program is implemented using SQLAlchemy for Database operations with MySQL database.

Provided csv file is fetched to load and save in the database.

URL https://pwcwebapp.ts.r.appspot.com tabulates the list of all companies.
URL https://pwcwebapp.ts.r.appspot.com/restricted tabulates list of restricted companies.
REST endpoint has been implemented to return the json data to search restricted companies.


Follow to run the project in development environment

`$ python3 -m venv env`
`$ source env/bin/activate`
`$ pip install -U pip`
`$ pip install -r requirements.txt`

`$ python run.py`


