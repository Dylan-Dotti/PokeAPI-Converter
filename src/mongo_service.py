import pymongo


__client = pymongo.MongoClient('mongodb+srv://Dylan_D:<password>'
                               '@cluster0-ddcyt.gcp.mongodb.net/'
                               'test?retryWrites=true&w=majority')
try:
    __client.list_database_names()
    print('Database connection successful')
except Exception:
    print('Database connection failed')


def insert_one(document, coll_name):
    coll = __get_collection(coll_name)
    return coll.insert_one(document)


def insert_many(documents, coll_name):
    coll = __get_collection(coll_name)
    return coll.insert_many(documents)


def delete_one(query_obj, db_name, coll_name):
    coll = __get_collection(coll_name)
    return coll.delete_one(query_obj)


def drop_collection(coll_name):
    coll = __get_collection(coll_name)
    return coll.drop()


def __get_collection(coll_name):
    db = __client['pokeapi']
    return db[coll_name]