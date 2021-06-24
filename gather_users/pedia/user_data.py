from . import config

import calendar

from ..utils.helper_functions import format_time

#handles time formatting, getting data (using gccollab.py) and storing it
def get_script(path, year, month, day):
    
    print("Creating GCpedia query")
    
    end_time = format_time(day, month, year)

    query = config.query

    query = str.replace(query, "END_TIME", str(end_time))
    query = str.replace(query, "DATE", "{year}_{month}_{day}".format(year = str(year), month = str(month), day = str(day)))

    url = path + "pedia_script_{y}_{m}_{d}.sql".format(y = year, m = month, d = day)
    
    with open(url, "w") as f:
        for line in query:
            f.write(line)

    print ("{URL} has been created.".format(URL = url))
    
    