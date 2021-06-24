import pandas as pd
import json

import mysql.connector
from mysql.connector import errorcode

import sqlalchemy as sq
import time
import sys

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

from sqlalchemy import text
from sqlalchemy.orm import aliased
from sqlalchemy import or_

from . import config

import calendar
import datetime

class collab_db:

    def __init__(self):
        self.conn = mysql.connector.connect(**config)
        self.cursor = self.conn.cursor()

    def get_user_data(self, end_unixtime): 
        self.cursor.execute(
            """
            SELECT email, username, language, name
            FROM elggusers_entity ue
            JOIN elggentities ee ON ee.guid = ue.guid
            WHERE ee.time_created < """ + str(end_unixtime)
        )
        users = pd.DataFrame(self.cursor.fetchall()) 
        return self.format_users(users)

    '''
    
    '''
    def format_users(self, df):
        df.columns = ["email", "username", "language", "full name"]
        
        for x in df:
            for y in df[x]:
                if "," in y:
                    y = str.replace(y, ",", " - ")

        #future formatting. Left in for future usage
        if False:
            first_names = []
            last_names = []
            for x in df["full name"]:
                y = x.split(" ")
                if len(y) != 2:
                    print(y)

        return df

