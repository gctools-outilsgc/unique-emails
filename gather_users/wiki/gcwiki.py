import pandas as pd
import json

import mysql.connector
from mysql.connector import errorcode

from . import config
from . import kube_connect

class wiki_db:

    def __init__(self):
        self.DB = kube_connect.db_connection()
        self.connect_to_database()

    def connect_to_database(self):
        while (not bool(self.DB.check_connection())):
            continue #waiting for db connection to be established

        self.conn = mysql.connector.connect(**config)
        self.cursor = self.conn.cursor()

    def format_time(self, year, month, day):
        year = str(year)
        month = str(month)
        day = str(day)
        if len(month) == 1:
            month = "0" + month
        if len(day) == 1:
            day = "0" + day
        return year + month + day + "000000" 

    def get_users(self, year, month, day):

        END = self.format_time(year, month, day)
        self.cursor.execute(
            """
            SELECT CONVERT( user_email USING utf8) as  emails, CONVERT(user_name USING utf8) as usernames, CONVERT(user_real_name USING utf8) as full_name
            FROM user
            WHERE user_registration < "{end}" """.format(end = END)
        )

        df = pd.DataFrame(self.cursor.fetchall()) 
        df.columns = ["email", "username", "full name"]
        return df

    def terminate(self):
        self.DB.terminate()

#definitely works
#SELECT CONVERT( user_email USING utf8) as  emails, CONVERT(user_name USING utf8) as usernames, CONVERT(user_real_name USING utf8) as full_name
#FROM user
#WHERE user_registration < "20191101000000"
  
   
    
    