from flask import Flask, jsonify, request 
from flask_restful import Resource, Api, reqparse
from pymongo import MongoClient
import configparser
import os

"""
Like any normal python file write all the functions and make sure the functions are invoked on correct routes
"""


# Getting configuration data for service
config = configparser.ConfigParser()
config.readfp(open(r'./application.cfg'))
client_connection = config.get('Mongo', 'client')
db = config.get('Mongo', 'db')

# Defining Flask APP
app = Flask(__name__) 
api = Api(app) 



@app.route('/model', methods=['POST'])
def userRecommendation():
    try:
        req_data = request.get_json()
        input1 = req_data['input1']
        input2 = req_data['input2']
	"""
	 1 ) Get all the inputs needed for your app from the post call
	 
	 2 ) Process the script or fetch value from the db or what ever you want to do
	 
	 3 ) Assign it to output and return it.
	
	
	"""
        return jsonify({'Result' : output})
    except Exception as e:
        return jsonify({"errors" : [{"status": "400", "code": "", "details": 'missing '+str(e)}]})


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"errors" : [{"status": "404", "code": "", "details": "No such service request found"}]})
