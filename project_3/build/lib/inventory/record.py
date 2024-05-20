import os,sys
from flask_restx import Namespace, Resource, fields
from flask import (request, current_app)
from werkzeug.utils import secure_filename
import datetime
import time
import subprocess
import json
from inventory.db import get_mongodb

api = Namespace("record", description="Record APIs")

search_model = api.model(
    'Record Search', {'query': fields.String(required=True, default="", description='Query string')}
)

insert_model = api.model(
    'Record Insert', {
        'fname': fields.String(required=True, default="James", description='First name'),
        'lname': fields.String(required=True, default="Bond", description='Last name')                  
    }
)


@api.route('/insert')
class RecordList(Resource):
    @api.doc('insert_records')
    @api.expect(insert_model)
    def post(self):
        req_obj = request.json
        mongo_dbh, error_obj = get_mongodb()
        if error_obj != {}:
            return error_obj
        res = mongo_dbh["c_inventory"].insert_one(req_obj)
        res_obj = {"status":1}
        return res_obj

    @api.doc(False)
    def get(self):
        return self.post()


@api.route('/search')
class RecordList(Resource):
    @api.doc('search_records')
    @api.expect(search_model)
    def post(self):
        req_obj = request.json
        res_obj = req_obj
        mongo_dbh, error_obj = get_mongodb()
        if error_obj != {}:
            return error_obj
        res_obj = {"records":[]}
        for doc in mongo_dbh["c_inventory"].find(req_obj):
            if "_id" in doc:
                doc["_id"] = str(doc["_id"])
            res_obj["records"].append(doc)
        res_obj["status"] = 1

        return res_obj

    @api.doc(False) 
    def get(self):
        return self.post()



def get_mongodb():


    ret_obj, error_obj = {}, {}
    try:
        conn_str, db_name, ser = "", "", ""
        ser = current_app.config["SERVER"] if "SERVER" in current_app.config else ser
        ser = os.environ["SERVER"] if "SERVER" in os.environ else ser
        if ser == "dev":
            conn_str =  current_app.config["MONGODB_CONNSTRING"]
            db_name = current_app.config["DB_NAME"]
        else:
            conn_str, db_name = os.environ['MONGODB_CONNSTRING'], os.environ['DB_NAME']
        client = pymongo.MongoClient(conn_str)
        client.server_info()
        ret_obj = client[db_name]
    except pymongo.errors.ServerSelectionTimeoutError as err:
        error_obj = {"status":0, "error":"Connection to MongoDB failed", "details":err.details}
    except pymongo.errors.OperationFailure as err:
        error_obj = {"status":0, "error":"Connection to MongoDB failed", "details":err.details}
    return ret_obj, error_obj









