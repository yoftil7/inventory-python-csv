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

update_model = api.model(
    'Record Update', 
    {
        '_id': fields.String(required=True, description='id of document to update'),
        'key': fields.String(required=True, description='specific field to update'),
        'new_value': fileds.String(required=True, description='update content')
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

@api.route('/read')
class RecordList(Resource):
    @api.doc('read_records')
    def get(self):
        mongo_dbh, error_obj = get_mongodb()
        if error_obj:
            return error_obj, 500
        records = []
        for doc in mongo_dbh["c_inventory"].find():
            if "_id" in doc:
                doc["_id"] = str(doc["_id"])
            records.append(doc)
        return {"status": 1, "message": "All Records"}
    
    @api.doc(False)
    def get(self):
        return self.post()

@api.route('/update')
class RecordList(Resource):
    @api.doc('update_records')
    @api.expect(update_model)
    def put(self):
        mongo_dbh, error_obj = get_mongodb()
        if error_obj:
            return error_obj, 500
        update_data = request.get_json()
        update_id = update_data.get('_id')
        key = update_data.get('key')
        new_value = update_data.get('new_value')
        if isinstance(update_id, int):
            query = {'_id': update_id}
        else:
            query = {'_id': ObjectId(update_id)}

        res = mongo_dbh['c_inventory'].update_one(query, {"$set": {key: new_value}})
        if res.modified_count == 1:
            return {"status": 1, "message": "Successfully updated!"}
        else:
            return {"status": 0, "message": "Record not updated"}


@api.route('/delete')
class RecordList(Resource):
    @api.doc('delete_records')
    def delete(self):
        mongo_dbh, error_obj = get_mongodb()
        if error_obj:
            return error_obj, 500
        delete_id = request.json.get('_id')
        if isinstance(delete_id, int):
            query = {'_id': delete_id}
        else:
            query = {'_id': ObjectId(delete_id)}
        res = mongo_dbh['c_inventory'].delete_one(query)
        if res.deleted_count == 1:
            return {"status": 1, "message": "Record successfully deleted"}
        else:
            return {"status": 2, "message": "Record not found!"}


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









