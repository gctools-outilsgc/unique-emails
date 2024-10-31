query = """SELECT user_email as email, user_registration, user_touched 
INTO OUTFILE '/tmp/pedia_users_DATE.csv' 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\\n' 
FROM wikidb.user
WHERE user_registration < END_TIME;"""
