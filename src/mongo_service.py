import pymongo
import utilities as util


print('Connecting to database...')
__client = pymongo.MongoClient('mongodb+srv://Dylan_D:Vo7tron0@cluster0-ddcyt.gcp.mongodb.net/test?retryWrites=true&w=majority')
try:
    __client.list_database_names()
    print('Database connection successful')
except Exception:
    print('Database connection failed')


def insert_one(document, coll_name):
    coll = __get_collection(coll_name)
    coll.insert_one(document)


def insert_many(documents, coll_name):
    util.print_progress_bar(0, len(documents))
    for index, document in enumerate(documents):
        insert_one(document, coll_name)
        util.print_progress_bar(index + 1, len(documents), same_line=(index <= len(documents)))
    print('')


def delete_one(query_obj, db_name, coll_name):
    coll = __get_collection(coll_name)
    coll.delete_one(query_obj)


def drop_collection(coll_name):
    coll = __get_collection(coll_name)
    return coll.drop()


def __get_collection(coll_name):
    db = __client['pokeapi']
    return db[coll_name]