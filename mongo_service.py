import pymongo

__client = pymongo.MongoClient('mongodb+srv://Dylan_D:<Password>'
                               '@cluster0-ddcyt.gcp.mongodb.net/'
                               'test?retryWrites=true&w=majority')
try:
    __client.list_database_names()
    print('Database connection successful')
except Exception:
    print('Database connection failed')


def insert_one(document, db_name, coll_name):
    db = __client[db_name]
    coll = db[coll_name]
    return coll.insert_one(document)


def insert_many(documents, db_name, coll_name):
    db = __client[db_name]
    coll = db[coll_name]
    return coll.insert_many(documents)


def delete_one(query_obj, db_name, coll_name):
    db = __client[db_name]
    coll = db[coll_name]
    return coll.delete_one(query_obj)
