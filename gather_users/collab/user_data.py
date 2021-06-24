from . import gccollab
import calendar

from ..utils.helper_functions import to_unixtime

GCCOLLAB_DB = gccollab.collab_db()

#handles time formatting, getting data (using gccollab.py) and storing it
def get_users(path, year, month, day):
    
    print("\nGathering GCcollab data")
    
    #time formatting
    unix_time = to_unixtime(day, month, year)
    
    users = GCCOLLAB_DB.get_user_data(unix_time)
    
    print(users.head())

    url = path + "collab_users_{y}_{m}_{d}.csv".format(y = year, m = month, d = day)
    users.to_csv(url, index = False, sep = ",")
    print ("{URL} has been created.\n".format(URL = url))
    
    return users
