from . import message
import calendar

msg = message.Message()

#handles getting data (using message.py), and storing it
def get_users(path, year, month, day):
    try:
            
        print("Gathering GCmessage data")
        
        users = msg.get_users(year, month, day)
        
        #print(users.head())

        loc = path + "message_users_{y}_{m}_{d}.csv".format(y = year, m = month, d = day)
        users.to_csv(loc, index = False, sep = ",")
        print ("{loc} has been created.\n".format(loc = loc))
    finally:
        msg.terminate()
    #return users

