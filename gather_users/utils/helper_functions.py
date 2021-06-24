import time
import datetime

"""
converts a given day, month, year to its unixtime
"""
def to_unixtime(day, month, year):
    s = "1/" + str(day) + "/" + str(month) + "/" + str(year)
    return int(time.mktime(datetime.datetime.strptime(s, "%H/%d/%m/%Y").timetuple()))

"""
Increments the given month, year by one month.
"""
def increment (month, year):
    if month < 12:
        return (month + 1, year)
    else:
        return(1, year + 1)

def monthly_increment(month, year): 
    if month < 12:
        return {"month" : month + 1, "year" : year}
    else:
        return {"month" : 1, "year" : year + 1}

def string_month(month):
    str_month = str(month)
    if month < 10:
        str_month = "0" + str_month
    return str_month


"""
Returns string with date format YYYYMMDDHHMMSS
"""
def format_time(day, month, year):
    year = str(year)
    month = str(month)
    day = str(day)

    if len(month) == 1:
        month = "0" + month
    if len(day) == 1:
        day = "0" + day
        
    return year + month + day + "000000" 

def fiscal_to_actual(quarter_num, fiscal_year):
    
    initial_month = (1 + quarter_num * 3) % 12

    if quarter_num == 4:
        year = fiscal_year + 1
    else:
        year = fiscal_year

    final_month = initial_month + 3
    tup = {"start_month": initial_month, "end_month": final_month, "year": year} #End month is actually one more, as it's only used with to_unixtime where we do start < time < end 
    return tup

    

