from bson.objectid import ObjectId
import pymongo

import config
from adapters import adapter


class MongoDBAdapter(adapter.DBAdapter):
    def __init__(self, host=config.HOST, port=config.PORT, dbname=config.DBNAME):
        self.client = pymongo.MongoClient(host, port)
        self.db = self.client[dbname]

    def get_report(self, report_id, **filters):
        res = self.db.reports.find_one({'_id': ObjectId(report_id)})
        res['_id'] = str(res['_id'])
        return res

    def create_report(self, data_dict):
        res = self.db.reports.insert(data_dict)
        return str(res)
