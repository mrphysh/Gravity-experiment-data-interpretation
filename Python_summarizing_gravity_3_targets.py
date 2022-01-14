
import sqlite3   
import datetime
from datetime import datetime,timedelta
import os
import sys
python_script = sys.argv[0]
print ("script name   ", python_script)
#python_script = "window 300"
##
data_source_database =  "example_database_nov28_2021"
##
#          start with              as database  and            mu_summary_table as table 
#########         then     TWO GFCS COMPLETE  as database  and            mu_summary_table      same table
##
summary_table =  "summary"###this is not working
##
conn = sqlite3.connect(data_source_database)
c = conn.cursor()
                                                              ##########    mu    alpha     theta
bonn = sqlite3.connect('C:\\Users\\mrphy\\dec 2021 PEND summaries\\three_data_summary_01')     
b = bonn.cursor()
b.execute("CREATE TABLE IF NOT EXISTS toward_past    (time_stamp TEXT  ,  mu_daily_summary REAL, alpha_daily_summary REAL , \
theta_daily_summary REAL, \
python_script TEXT,   one_count REAL  ,  two_count REAL   ,three_count REAL,  origin_database TEXT  ,  search_number_per_day REAL )") 
print ("++++++++++++++++++")

def dynamic_data_entry_averages():
    b.execute("INSERT INTO toward_past  (time_stamp   ,  mu_daily_summary,   alpha_daily_summary ,theta_daily_summary ,\
python_script , one_count,  two_count , three_count, origin_database    ,    search_number_per_day   ) VALUES (?,?,?,?,?,?,?,?,?,?)",\
              ( date_var,  one_average,  two_average, three_average,  python_script,   one_count,   two_count, three_count,   data_source_database,  search_number  ) )
    bonn.commit()
##
##    
date_var = '2021-11-28 22:00:00'#
#                         #
#
search_number =  5000
#
print()
var_one = 34 # need something here.  Does the search find a value?  this cannot be avoided
print()
number = 0
total_count = 0
num_added_db = 0
print ("++++++++++++++++++++++++++")
while (var_one  ):
    
    var_one = None                  #this needs to null  ..  will it be reset?
    c.execute ("SELECT column_one, column_three, column_four, column_six FROM first_table WHERE column_one > '%s'" %date_var)
    
    number =0                      
    no_val = 0
    one_sum   = 0              
    one_count = 0
    one_average = 0
    two_sum =0
    two_count = 0
    two_average = 0
    three_sum = 0
    three_count = 0
    three_average = 0
   
    
## """"""this has the database search
##    """so this section is run per day

    for row in c.fetchmany(search_number):
        var_one = row[0]
        var_two  = row[1]
        var_thr  = row[2]
        var_four = row[3]
        
        if var_two != None:
            one_sum = one_sum + var_two
            one_count = one_count + 1
            
        if var_thr != None:
            two_sum = two_sum + var_thr
            two_count = two_count + 1

        if var_four != None:
            three_sum = three_sum + var_four
            three_count = three_count + 1
    
        number = number +1
        #print (five_var)
    """  this is post day processing.  this section is run at the end of day:
update counters
calcayte the averages
enter the data into the database with the function call
update the date to date+1
update the targets,,,,,  wait there is no target with this one
"""
    num_added_db = num_added_db + 1
    total_count = total_count + number
    number = 0  #  this needs to be reset
    if one_count != 0:
        one_average = int(one_sum/(one_count ))
    if two_count != 0:
        two_average = int(two_sum/(two_count ))
   
    if three_count != 0:
        three_average = int(three_sum/(three_count ))
     
   
        ################################
    row_count = one_count + two_count
    print("date   ",date_var,"                     ",one_average,"     ", two_average,"    " , three_average)
    ##   no targets with this one  print ("the targets are  ,,                  ",one_target,"   ", two_target )
    print ("row count...total of all counts    ", row_count)

    dynamic_data_entry_averages()
    """
    If the data is sorted, there is no search at all.
    if one_average  != None :
        one_target  = int(one_average/1000)
          
    """
    
       
    date = datetime.strptime(date_var, "%Y-%m-%d %H:%M:%S")  # this sets up the variable for altering
    date = str(date + timedelta(days = 1))     
    date_var = date
    
    print ()
"""
summarize it all:  how many rows were read
                   how many rows were entered into the recieving database?

       
"""    
print ("total rows pulled from db is     ", total_count)
print ("total rows added to database is   ", num_added_db)
print ("           end                end          end                  end                end ")



   

   
