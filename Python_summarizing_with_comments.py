import sqlite3                       #   This takes care of the sqlite3 database.  I use DB Browser to look at the databases
import datetime                         #  and cut and paste to excel for stats and graphs.
from datetime import datetime,timedelta    #  this the source of the UnIX time stamp.  The data is all time, but it comes through the micros() function 
import os                                # this allows the python script name to e inserted
import sys                               # not sure about this one
python_script = sys.argv[0]             ## this goes into the database
print ("script name   ", python_script)
"""
I a chemist and taught this to myself.  This thellsyou that it may not be as complicated as a program created by a team of professionals
The platform is veru powerful, but awkward.  Modifications must be made within the code.
How many rws are sampled "search_number"  I leave it at 5000
The raw data database must be added manually.  And the name must be added into another field to put the name into the database.
The start date of the raw file must be entered manually.  If this is overlooked, weird stuff can occur.  For big summaries, the database must be entered into two fields,
the start date must be entered and that is all.  This will pile the summary data into one table in one database.  If done carefully and with luck, 
the table will show nice summaries in chronological order.  I have set up a practice table and used that to make sure that everything is fine, then moved to the final summary.


"""
data_source_database =  "example_database_nov28_2021"

conn = sqlite3.connect(data_source_database)
c = conn.cursor()
                                                              ##########    mu    alpha     theta   >>>>   These are the names of the anniversary clocks
                                                              #### mu and alpha are mechanical grandfather clocks.  theta is an electronic pendulum drive    
bonn = sqlite3.connect('C:\\Users\\mrphy\\dec 2021 PEND summaries\\three_data_summary_01')     
b = bonn.cursor()                            ## the connection object relates to the database.
                                            ##If the summary goes into a different table, two connection objects are not needed
b.execute("CREATE TABLE IF NOT EXISTS rotating_nov2021    (time_stamp TEXT  ,  rodney_daily_summary REAL, robbie_daily_summary REAL , \
           rachel_daily_summary REAL, \
python_script TEXT,   one_count REAL  ,  two_count REAL   ,three_count REAL,  origin_database TEXT  ,  search_number_per_day REAL )") 
print ("++++++++++++++++++")

def dynamic_data_entry_averages():
    b.execute("INSERT INTO rotating_nov2021  (time_stamp   ,  rodney_daily_summary,   robbie_daily_summary ,rachel_daily_summary ,python_script , \
               one_count,  two_count , three_count, origin_database    ,    search_number_per_day   ) VALUES (?,?,?,?,?,?,?,?,?,?)",\
              ( date_var,  one_average,  two_average, three_average,  python_script,   one_count,   two_count, three_count,   data_source_database,  search_number  ) )
    bonn.commit()
##
    
date_var = '2021-11-28 22:00:00'#  This must be manually entered.  The start date is part of the name of the database.
#                          o
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
    c.execute ("SELECT column_one, column_two, column_five, column_seven FROM first_table WHERE column_one > '%s'" %date_var)
    
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
##    """so this section is run per day\
    ##  The fetch says. "pull rows from the database and put the rows into an array.  Then, one row, at a time process them"
    ##  I usually use search number = 5000.  

    for row in c.fetchmany(search_number):
        var_one = row[0]  # date time
        var_two  = row[1] #  mu
        var_thr  = row[2] # alpha
                            
        var_four = row[3]  #theta
        
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
    date = str(date + timedelta(days = 1))     ############this is a good example of the majic of Python...  take the date field (a string)
                                               #$$ and make it into a datetime value  ....  add a day to it and turn it back into a string.
    date_var = date
    
    print ()
"""
summarize it all:  how many rows were read
                   how many rows were entered into the recieving database?

       
"""    
print ("total rows pulled from db is     ", total_count)
print ("total rows added to database is   ", num_added_db)
print ("           end                end          end                  end                end ")


