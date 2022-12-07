import os
import pymongo
import pymongo.errors

class Database:
    @staticmethod
    def connect() -> pymongo.MongoClient:
        try:
            return pymongo.MongoClient(
                host='database',
                port=27017,
                username=os.getenv('MONGO_INITDB_ROOT_USERNAME'),
                password=os.getenv('MONGO_INITDB_ROOT_PASSWORD'),
                # authSource='admin',
                # authMechanism='SCRAM-SHA-256',
            )
        except pymongo.errors.ConnectionFailure:
            print('Failed to connect to mongoDB!')

    dbInstance = connect()
