#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/17 13:19
import time
import os
import pickle

class MySQL():
    DB_PATH = "db"
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.id = MySQL.get_id()

    @staticmethod
    def get_id():
        return int(time.time())

    def save(self):

        db_file = os.path.join(MySQL.DB_PATH, str(self.id))
        if os.path.isfile(db_file):
            raise OSError("")
        with open(db_file, 'wb') as f:
            pickle.dump(self, f)
        pass

    @classmethod
    def get_obj_by_id(cls, id):
        db_file = os.path.join(MySQL.DB_PATH, str(id))
        with open(db_file,'rb') as f:
            return pickle.load(f)

if __name__ == "__main__":
    pass
    db = MySQL('127.0.0.1', 3306)
    db.save()
    # db = MySQL.get_obj_by_id(1537164126)
    # print(db.__dict__)