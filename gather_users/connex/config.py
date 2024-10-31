query = """select email, time_created, last_action FROM (
select e.guid, u.email, e.time_created, u.last_action 
FROM elggentities e 
join elggusers_entity u on e.guid=u.guid where e.type = 'user') as t
where time_created < END_TIME
INTO OUTFILE '/tmp/connex_users_DATE.csv' 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\\n' ;"""
