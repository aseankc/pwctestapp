import os
SQLALCHEMY_TRACK_MODIFICATIONS = False

# GCP
CLOUD_SQL_USERNAME= 'dbadmin'
CLOUD_SQL_PASSWORD= 'dbadmin'
CLOUD_SQL_DATABASE_NAME= 'comdata'
CLOUD_SQL_CONNECTION_NAME= 'pwcwebapp:australia-southeast1:pwctestdata'

LOCAL_SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{nam}:{pas}@127.0.0.1:3306/{dbn}').format (
    nam=CLOUD_SQL_USERNAME,
    pas=CLOUD_SQL_PASSWORD,
    dbn=CLOUD_SQL_DATABASE_NAME,
)

LIVE_SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{nam}:{pas}@localhost/{dbn}?unix_socket=/cloudsql/{con}').format (
    nam=CLOUD_SQL_USERNAME,
    pas=CLOUD_SQL_PASSWORD,
    dbn=CLOUD_SQL_DATABASE_NAME,
    con=CLOUD_SQL_CONNECTION_NAME,
)

if os.environ.get ('GAE_INSTANCE'):
    SQLALCHEMY_DATABASE_URI = LIVE_SQLALCHEMY_DATABASE_URI
else:
    SQLALCHEMY_DATABASE_URI = LOCAL_SQLALCHEMY_DATABASE_URI

# Override to SQLITE (for testing ...)
# SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'