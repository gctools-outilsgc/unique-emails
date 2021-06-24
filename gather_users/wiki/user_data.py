import pandas as pd
from . import wiki_db
import calendar

import time

def get_users(path, year, month, day):
    try: 
        #set-up
        print("Gathering GCwiki data")

        #get data
        WIKI_DB = wiki_db()
        users = WIKI_DB.get_users(year, month, day)
        
        #print(users.head())

        loc = path + "wiki_users_{y}_{m}_{d}.csv".format(y = year, m = month, d = day)
        users.to_csv(loc, index = False, sep = ",")
        print ("{loc} has been created.\n".format(loc = loc))

    finally:
        #close connection
        WIKI_DB.terminate()
