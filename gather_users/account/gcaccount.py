from . import config
from . import kube_connect

import psycopg2
import pandas as pd

class Account:
#
    def __init__(self): 
        self.KUBE = kube_connect.db_connection()
        self.connect_to_database()
    
    def connect_to_database(self):
        '''
        helper function, forms the connection
        '''
        while (not bool (self.KUBE.check_connection() ) ): #waiting for db to be port-forwarded and available, shouldn't take long
            continue 
        self.connection = psycopg2.connect(user = config.user, password = config.password, host = config.host, port = config.port, database = config.database)
        self.cursor = self.connection.cursor()

 
    def get_users(self, END):
        '''
        The core function, performs the gathering of data
        '''


        st_old = """SELECT email, username, name
FROM (
	SELECT email, username, name, last_activity 
	FROM (
		SELECT DISTINCT uss1.user_id, (SELECT MIN(last_activity) AS last_activity FROM user_sessions_session uss2 WHERE uss2.user_id = uss1.user_id)
		FROM user_sessions_session uss1
		) sessions
	JOIN core_user AS cu ON sessions.user_id = cu.id 
) AS table1
WHERE last_activity < '{END}'""".format(END = END)



        st = """SELECT email, username, name
FROM core_user
WHERE is_active = true and id <= (select MAX(uss1.user_id) from user_sessions_session uss1 where last_activity < '{END}')""".format(END = END)
        self.cursor.execute(st) 
        rows = self.cursor.fetchall()
        return self.format(rows)


    def format(self, rows):
        '''
        Formats data to remove commas so it can be stored as a csv
        '''
        lsts = []

        for row in rows:

            #Remove commas from elements, otherwise it breaks the csv
            for elem in row:
                if "," in elem:
                    elem = str.replace(elem, ",", " - ")
                    
            lst = [row[0], row[1], row[2] ]
            lsts.append(lst)
        df = pd.DataFrame(lsts)
        df.columns = ["email", "username", "full name"]
        return df
      

    def terminate(self):
        '''
        Close all connections
        '''
        self.cursor.close()
        self.connection.close()
        self.KUBE.terminate()

