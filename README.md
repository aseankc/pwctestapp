Flask project is implemented to keep the list of companies.
Project is deployed in GOOGLE APP ENGINE and GOOGLE CLOUD SQL.

Program is implemented using SQLAlchemy for Database operations with MySQL database.

Provided csv file is fetched, and processed to correct the bussiness number to number format and then is saved in the database.

URL https://pwcwebapp.ts.r.appspot.com tabulates the list of all companies.
URL https://pwcwebapp.ts.r.appspot.com/restricted tabulates list of restricted companies.
REST endpoint has been implemented to get the company by business number and returns json payload.
URL https://pwcwebapp.ts.r.appspot.com/filter?businessnumber=354853524

Follow to run the project in development environment

`$ python3 -m venv env`
`$ source env/bin/activate`
`$ pip install -U pip`
`$ pip install -r requirements.txt`

`$ python run.py`


