Flask project is implemented to keep the list of companies.
Project is deployed in GOOGLE APP ENGINE and GOOGLE CLOUD SQL.

Program is implemented using SQLAlchemy for Database operations with MySQL database.

Provided csv file is fetched to load and save in the database.

Root URL renders the list of all companies.
/restricted yeilds the list of restricted companies.
To run the project in dev environment
`$ python3 -m venv env`
`$ source env/bin/activate`
`$ pip install -U pip`
`$ pip install -r requirements.txt`

`$ python run.py`


