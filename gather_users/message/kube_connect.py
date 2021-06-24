import sys
from subprocess import Popen, PIPE
import socket

from . import config

class db_connection:
    
    def __init__(self):
        db_command = "kubectl port-forward --context messageAKSprod-admin -n message {name} {local_port}:{ext_port}".format(name = config.name, local_port = config.local_port, ext_port = config.ext_port )
        self.port = int(config.local_port)
    
        self.connect_to_database(db_command)

    def connect_to_database(self, command):
        self.connection = Popen(command, shell=True, stderr=sys.stderr, stdout=PIPE)
        self.socket = socket.socket()
        
    def check_connection (self):
        #s = socket.socket()        
        try:
            self.socket.connect(("127.0.0.1", self.port))
            return 1
        except:
            return 0

    def terminate(self):
        self.socket.close()
        self.connection.terminate()
        return 1

        
