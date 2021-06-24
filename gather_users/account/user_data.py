from . import gcaccount
import calendar

def get_users(path, year, month, day):
    '''
    Handles any time formatting, getting data (using gcaccount.py) and storing it
    '''

    try: 
        print("\nGathering GCaccount data")
        account = gcaccount.Account()
        
        st = "{y}-{m}-{d}".format(y = year, m = month, d = day)
        users = account.get_users(st)
        #print(users.head())
        url = path + "account_users_{y}_{m}_{d}.csv".format(y = year, m = month, d = day)
        users.to_csv(url, index = False, sep = ",")
        print ("{URL} has been created.".format(URL = url))
    
    finally: 
        account.terminate()
