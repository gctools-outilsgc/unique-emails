from . import config

import calendar

from ..utils.helper_functions import to_unixtime

#handles time formatting, getting data (using gccollab.py) and storing it
def get_script(path, year, month, day):
    
    print("\nCreating GCconnex query")
    
    end_time = to_unixtime(day, month, year)

    query = config.query

    query = str.replace(query, "END_TIME", str(end_time))
    query = str.replace(query, "DATE", "{year}_{month}_{day}".format(year = str(year), month = str(month), day = str(day)))
    url = path + "connex_script_{y}_{m}_{d}.sql".format(y = str(year), m = str(month), d = str(day))
    
    with open(url, "w") as f:
        for line in query:
            f.write(line)

    print ("{URL} has been created.\n".format(URL = url))
    
    