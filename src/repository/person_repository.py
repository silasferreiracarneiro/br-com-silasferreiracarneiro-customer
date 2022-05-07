
from bson.json_util import dumps



class PersonRepository:
    def __init__(self, db_mongo):
        print('GET', flush = True)
        _customers = db_mongo.findAll()
        result = dumps(_customers, indent = 2)
        print(result, flush = True)
