import calendar
import os
import sys
from requests import head as requests_head

from gather_users import collab_get_users, account_get_users, message_get_users, wiki_get_users, connex_get_script, pedia_get_script

'''
Calling style
    python unique_users.py 2019 11 1

Gets user data up to the date given (not including).
'''
if __name__ == "__main__": 

    if len(sys.argv) != 4:
        raise Exception("Invalid arguments")

    year = int (sys.argv[1])
    month = int (sys.argv[2])
    day = int (sys.argv[3])

    print("Gathering user data for {m} {d}, {y}".format(m = str(calendar.month_name[month]), d = day, y = year))

    #directory set-up
    PATH = "user_data/" + str(year) + "-" + str(month) + "-" + str(day) + "/" #e.g. user_data/2019-11-1/
    if not os.path.exists(PATH[0:-1]):
        os.mkdir(PATH[0:-1])

    #Call functions
    if requests_head("http://www.google.com").status_code == 200:
        connex_get_script(PATH, year, month, day)
        pedia_get_script(PATH, year, month, day)
        
        collab_get_users(PATH, year, month, day)
        message_get_users(PATH, year, month, day)
        wiki_get_users(PATH, year, month, day)
        account_get_users(PATH, year, month, day) # seems to cause issues for anything that goes after it
    else:
        print("Unable to connect. Make sure you're connected to the internet and try again")





                