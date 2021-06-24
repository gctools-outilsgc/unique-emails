import sys
from subprocess import Popen, PIPE, check_output
import socket
import pandas as pd

from . import config

'''
Forms and handles the db connection aspects, using config.py to keep the more sensitive information (just in case)
'''
class db_connection:
    

    def __init__(self):
        '''
        constructor. 5432 is the port the database is accessible to in the pod.
        '''
        db_command = "kubectl port-forward --context CollabAKSProd-admin -n account {name} {local_port}:5432".format(name = self.get_name(), local_port = config.port )
        self.port = int(config.port)
        
        self.connect_to_database(db_command)


    def get_name(self):
        '''
        Finds the pod name
        '''
        cmd = check_output("kubectl get pods --context CollabAKSProd-admin -n account", shell=True)
        list_of_db = cmd.decode().split("\n"[0])

        def startswith(var):
            return var.startswith("account-db-deployment")

        filtered_list = filter(startswith, list_of_db)

        for db in filtered_list: 
            return db.split()[0]
            

    def connect_to_database(self, command):
        '''
        Performs the port-forwarding and creates socket to check if database is ready to interact with
        '''
        self.connection = Popen(command, shell=True, stderr=sys.stderr, stdout=PIPE)
        self.socket = socket.socket()

    def check_connection (self): 
        try:
            self.socket.connect(("127.0.0.1", int(self.port)))
            return 1
        except:
            return 0

    def terminate(self):
        '''
        close all connections
        '''
        self.socket.close()
        self.connection.terminate()
        