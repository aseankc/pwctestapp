import logging
from flask import render_template, json, request, abort
from app import app, db, models


@app.route ('/', methods = ['GET','POST'])
def index ():
    company = models.ComData
    data_all = company.query.all ()
    if data_all:
        # data=json.jsonify ([company.serialize () for company in all_data])
        data=[x.serialize() for x in data_all]
        return render_template('index.html',data=data)
    else:
        return "Request Failed Please reload page"

@app.route('/fetchrestricted', methods= ['GET','POST'])
def fetchrestricted():
    page_num = request.args.get('page', 1, type=int)
    page_size = request.args.get('pagesize', 100, type=int)
    company = models.ComData
    result = company.query.filter(company.restricted== 'Yes').paginate(page=page_num,per_page=page_size)
    return json.jsonify({'data':[x.serialize() for x in result.items]})

@app.route('/restricted',methods=['GET'])
def restricted():
    return render_template('restricted.html')

@app.route('/filter',methods=['GET'])
def filter():
    b_number = request.args.get('businessnumber',type=int)
    company = models.ComData
    result = company.query.filter(company.businessnumber==b_number).first()
    if(result):
        return json.jsonify(result.serialize())
    else: 
        return "NO Data avialable"
    

