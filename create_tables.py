from app import db,models
import logging
import os
import csv
def dataloader():
    list = []
    filename= 'faux_id_fake_companies.csv'
    file_path = os.path.join(os.path.dirname(__file__), filename)
    print(file_path)
    try: 
        with open(file_path,'r') as datafile:    
            csv_reader = csv.DictReader(datafile)    
            for row in csv_reader:        
                c = models.ComData(
                    cname = row['fake-company-name'],
                    description = row['description'],
                    email = row['company-email'],
                    tagline = row['tagline'],
                    # business_number_temp=row['business number'],
                    businessnumber = int(row['business number'].replace('-','')),
                    restricted = row['Restricted'])
                db.session.add(c)
            print(' list appender')
            # db.session.add (list)
            db.session.commit ()
            return 'success'
    except Exception as e:
            logging.error (e.__class__.__name__)
            db.session.rollback ()
            print('exception')
            return 'Error. Something bad happened.'

def runFetcher():
    db.drop_all ()
    db.create_all ()
    dataloader()
    print ('Done.')

# if __name__ == '__main__':
#     db.drop_all ()
#     db.create_all ()
#     dataloader()
#     print ('Done.')
