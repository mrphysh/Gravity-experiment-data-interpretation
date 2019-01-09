import datetime
import sqlite3
conn    = sqlite3.connect ('dec3_database')
c = conn.cursor()

c.execute ("SELECT * FROM dec26_table_cont WHERE column_one BETWEEN '2018-12-26 21:48:13.377000' and '2018-12-26 21:53:13.363000' ")

num_result = c.fetchall()
for row in num_result:
    print (row[0])
    print (row[1])
    print (row[2])
"""  
sort by time is working!  leave no spaces in the 'between' field.  seems to be no problem
so add the create index:
# declare the index
c.execute("CREATE INDEX IF NOT EXISTS index_time_table_one ON table_one(time_column)")
no problem adding this to the database!  Thanks to that guy on stackexchange.
let me look at organization.  why don't I move this into another area and then keep using this 
for my development
"""


conn.commit()
c.close()
#########*******************
