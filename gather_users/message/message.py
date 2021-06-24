#This file should be time-frame agnostic

import pandas as pd
import calendar
from pymongo import MongoClient
import datetime

from . import kube_connect
from . import config

class Message: 

    def __init__(self): 
        self.KUBE = kube_connect.db_connection()
        self.connect_to_database()
    
    def connect_to_database(self):
        while (not bool(self.KUBE.check_connection())):
           continue #waiting for db connection to be established

        self.myclient = MongoClient("mongodb://localhost:{}/".format(config.local_port))
        self.db = self.myclient["rocketchat"]

    def get_users(self, year, month, day): #return formatted dataframe
        END = datetime.datetime(year, month, day, 0, 0, 0, 0)
        x = self.db["users"].find( { 'createdAt' : { '$lt' : END } }, {"emails": 1, "username": 1, "language": 1, "_id": 0} )
        lst = []
        for x in x:
            lst.append(x)

        df = pd.DataFrame(lst)
        
        return self.format(df)
        #df.to_csv("gcMessage_users.csv", index = False)
            
    def format(self, df):
        df = df[["emails", "username", "language"]] #reorder
        em = []
        for x in df["emails"]:
            if isinstance(x, list):
                em.append(x[0]["address"]) 
            else:
                em.append("NaN")
        df["emails"] = em
        df.columns = ["email", "username", "language"]
        return df
    
    def terminate(self):
        self.KUBE.terminate()
    
