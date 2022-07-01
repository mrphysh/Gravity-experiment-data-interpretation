
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
import sqlite3   
import datetime
from datetime import datetime,timedelta
import os
import sys
python_script = sys.argv[0]
print ("script name   ", python_script)
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##                     this will indicate tha this is NO SORT
#######################################################################

data_source_path =  "C:\\Users\\mrphy\\Desktop\\data by julian month\\"

#                   ????????????????????????????
data_source_name =  "011_july_4_2019_db_no_sort"
#                   ????????????????????????????

db_with_path = data_source_path+data_source_name


data_source_table = "first_table"     ####this is working
### ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##                     this will indicate tha this is NO SORT
summary_database = "summary gravity hourly"  ####      "summary hourly daily mass gravity" 
#
#
summary_table_name = "table_gravity"  # default to [summary]   and [summary_extra] for testinbg
#summary_table_name = "summary_extra"   #  this is the test table


##         ?????????????????????
date_var = '2019-07-04 12:00:00'#  this worked starting with january?  that would be cool
#          ?????????????????????
##
search_number =  1500

conn = sqlite3.connect(db_with_path)      # one table only 'first_table'
c = conn.cursor()

bonn = sqlite3.connect(summary_database)      # one table only 'first_table'
b = bonn.cursor()
b.execute("CREATE TABLE IF NOT EXISTS "+summary_table_name+"  (time_stamp TEXT  , alpha_elect REAL, beta_elect REAL ,  theta_elect REAL, \
python_script TEXT,   one_count REAL  ,  two_count REAL   ,three_count REAL,  origin_database TEXT  ,  search_number_per_day REAL )") 

print ("++++++++++++++++++")

def dynamic_data_entry_averages():
    b.execute("INSERT INTO "+summary_table_name+"  (time_stamp   ,  alpha_elect,   beta_elect ,theta_elect ,python_script , one_count,  two_count , \
three_count, origin_database    ,    search_number_per_day   ) VALUES (?,?,?,?,?,?,?,?,?,?)",\
              ( date_var,  one_average,  two_average, thr_average,  python_script,   one_count,   two_count, thr_count,   data_source_name,  search_number  ) )
    bonn.commit()
    
##
######
    ######

#######
#######
one_target = 1817
two_target  = 1822
thr_target  =  1831

for_target = 1
five_target = 59
six_target = 13450
#
window      = 2000  #  and this is apples and oranges example 1870000 plus or minus 400
#

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
    c.execute ("SELECT column_one,  column_five FROM "+data_source_table+" WHERE column_one > '%s'" %date_var)
    
    number =0                      
    no_val = 0
    one_sum   = 0              
    one_count = 0
    
    two_sum   = 0
    two_count = 0
       
    thr_sum   = 0
    thr_count = 0
    
     
        
    one_average = 0
    two_average = 0
    thr_average = 0
    ###

    
   
   
    
## """"""this has the database search
##    """so this section is run per day



    for row in c.fetchmany(search_number):
        var_one = row[0]
        five_var = 2                  #I see ....  five_var is the name for the presently unidentified variable.
        if row[1] != None:
            five_var = int(row[1])
#     line seems to be required             okaaay
        if ((five_var)>(one_target*1000)- window  and (five_var)< ((one_target*1000)+window)):
            one_sum = one_sum + five_var
            one_count= one_count +1
        if ((five_var)>(two_target*1000)- window  and (five_var)< ((two_target*1000)+window)):
            two_sum = two_sum + five_var
            two_count= two_count +1
        if ((five_var)>(thr_target*1000)- window  and (five_var)< ((thr_target*1000)+window)):
            thr_sum = thr_sum + five_var
            thr_count= thr_count +1
            """
        if ((five_var)>(for_target*1000)- window  and (five_var)< ((for_target*1000)+window)):
            for_sum = for_sum + five_var
            for_count= for_count +1
        if ((five_var)>(five_target*1000)- 200000  and (five_var)< ((five_target*1000)+ 200000)):
            five_sum = five_sum + five_var
            five_count= five_count +1
        if ((five_var)>(six_target*1000)- 14000  and (five_var)< ((six_target*1000)+ 14000)):
            six_sum = six_sum + five_var
            six_count= six_count +1
        """
        number = number +1
        #print (five_var)
    """  this is post day processing.  this section is run at the end of day:
update counters
calcayte the averages
enter the data into the database with the function call
update the date to date+1
update the targets
"""
    num_added_db = num_added_db + 1
    total_count = total_count + number
    number = 0  #  this needs to be reset
    
   
 
    if (one_sum > 1700000 and one_sum != None):
        
        one_average = int(one_sum/(one_count ))
    else:
        one_average = None
       
    if (two_sum > 1800000 and two_sum != None):
        ######  this is not  calculating correctly
        two_average = int(two_sum/(two_count ))
    else:
        two_average = None
       # print ("          the average for col_thr for this day is ",  two_average)
    if (thr_sum > 1800000 and thr_sum !=None):  #  is null less than 1500000?
                                                        #  this is not causing problems, but not helping
        
        thr_average = int(thr_sum/(thr_count ))
    else:
        thr_average = None
        """

    if (for_sum > 1700000 and for_sum != None):
        
        for_average = int(for_sum/(for_count ))
    else:
        for_average = None
       
    if (five_sum > 1700000 and five_sum != None):
       
        five_average = int(five_sum/(five_count ))
    else:
        five_average = None
        
       # print ("          the average for col_thr for this day is ",  two_average)
    if (six_sum > 1700000 and six_sum !=None):  #  is null less than 1500000?
                                                        #  this is not causing problems, but not helping
        
        six_average = int(six_sum/(six_count ))
    else:
        six_average = None
        """
        ################################
    row_count = one_count + two_count + thr_count 
    print("date   ",date_var,"  ",one_average,"   ", two_average,"  ",  thr_average,"      ")
    print ("the targets are,repectively   ",one_target,"        ",two_target,"      ", thr_target )
    print ("row count...total of all counts    ", row_count)###             thi is printed at the end of every time period
############
    dynamic_data_entry_averages()
###############  this updates the averages
    
    if one_average  != None :
        one_target  = int(one_average/1000)
             
    
    if two_average != None:
        two_target = int(two_average/1000) 
    
    if thr_average != None:
        thr_target = int(thr_average/1000)
        """
    if for_average  != None :
        
        for_target  = int(for_average/1000)
             
    
    if five_average != None:
        five_target = int(five_average/1000) 
    
    if six_average != None:
        six_target = int(six_average/1000)
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
print ()
print ("AND  total rows added to database is                             ", num_added_db) 
print ()
print ("script name is  "  , python_script  )
print ()
print ("    database name is                               ", data_source_name)
print ()
print ("summary database   ", summary_database)
print ( "  end    end   end   "  )

"""
7777777777777   date format   '2021-08-25 22:00:00'
                             just use search number 5000
'C:\\Users\\mrphy\\Desktop\\data by julian month\\


'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\001_sept11_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\001_sept18_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\001_sept24_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\001_sept4_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\002_oct01_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\002_oct08_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\002_oct13_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\002_oct21_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\004_dec3_database first table'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\004_dec3_database second table'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\005_jan18_2019_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\007_mar_2_2019_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\008_april_19_2019_db_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\008_april_26_no sort_db'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\009_may_15_2019_db_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\009_may_26_2019_db_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\011_july_4_2019_db_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\012_aug21_2019_db_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\013_sept19_2019_db_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\015_nov11_2019_db_no_sort_bigger'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\017_jan08_2020_partdb_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\018_feb22__database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\019_mar14_2020_db_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\021_may27_2020_'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\023_jul18_2020_db_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\025 sept15_2020_db_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\026 oct09_2020_db_no_sort first_table'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\026 oct09_2020_db_no_sort second table'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\027 nov23_2020_db_sorted'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\029 jan23_2021_db_sorted'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\031 mar22_2021_db_sorted'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\033 all_numbers_june28_2021_aa_7_6'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\034 june26_all_numbers'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\035 one_of_two_july11_2021'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\036 one_of_two_aug24_2021'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\038 one_of_four_oct26_2021'
C:/Users/mrphy/Desktop/048 data through dec 2021                 /039 raw data example_nov_28_2021

'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\041 1_19_jan_16_2022'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\043 1_19_mar_16_2022 pre4_15'

"""
   


   
