from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import config

app = Flask (__name__)
app.config.from_object (config)
db = SQLAlchemy (app)

from app import models
from app import routes
from create_tables import runFetcher

@app.before_first_request
def before_first_request():
    app.logger.info("Initializing database before_first_request")
    runFetcher()



