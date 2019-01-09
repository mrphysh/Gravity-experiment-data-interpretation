"""
The Python adds the numbers to the database in the order and at the time it sees them.
So the numbers enter the Python one at a time and are put in the database one at a time.
Every entry includes a time identification that is generated with the datetime library.
I wanted the many empty fields to be truly empty, not just zeros.  I made an insert statement for 
each of the columns, leaving the respective blank fields truly null.  There are, I am sure , 
other ways to accomplish this, but this seems fine.
my notes say
column_two      average 1816988  stdev 192
column_three    average 1829091  stdev 288
column_four    average  1820694  stdev 147
The numbers are close, by me design.  I wanted them to be close so that they would be easy 
to visaulize with graphs.  But they are incredibly precise and the Python has no problems sorting
them into their fields.
I fuss with the windows a bit, but mostly they are fine.
I watch the data pretty closely and see irregularities that would not be visible were it not for the 
very precise measurement; one millionth of a second.
And notice that the Python only take one number out of 19.  
This all should be with an SD card reader, but I was never able to make it work.

"""

import serial #import serial library
import sqlite3
import datetime

data_object=serial.Serial('com3',9600)  #  data_object is the object!!
###################  to start a new database, just change the name here
conn = sqlite3.connect ('dec3_database')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS dec26_table (column_one TEXT,column_two REAL,column_three REAL, column_four REAL, column_five REAL,column_six REAL )")
#####    
def dynamic_data_entry_column_two():
    
    c.execute("INSERT INTO dec26_table(column_one,column_two) VALUES (?,?)",
		 ( unix , value_two  ) )
    conn.commit()
def dynamic_data_entry_column_three():
    
    c.execute("INSERT INTO dec26_table(column_one,column_three) VALUES (?,?)",
		 ( unix , value_three  ) )
    conn.commit()
def dynamic_data_entry_column_four():
    
    c.execute("INSERT INTO dec26_table(column_one,column_four) VALUES (?,?)",
		 ( unix , value_four  ) )
    conn.commit()
def dynamic_data_entry_column_five():
    
    c.execute("INSERT INTO dec26_table(column_one,column_five) VALUES (?,?)",
		 ( unix , value_five  ) )
    conn.commit()
def dynamic_data_entry_column_six():
    
    c.execute("INSERT INTO dec26_table(column_one,column_six) VALUES (?,?)",
		 ( unix , value_six  ) )
    conn.commit()

    ###
create_table()
    
    ##########################
unix = (datetime.datetime.now())
value_two = 0
value_three = 0
value_four = 0
value_five = 0
value_six = 1000
dynamic_data_entry_column_six()###this is the stamp for 'start python'  This appears in Column_six as [1000]
i=0
create_table()
#################
while (1==1):
    value_two = 0
    value_three = 0
    value_four = 0
    value_five = 0
    value_six = 0
#####

    
    
    
    (data_object.inWaiting()>0)
    unix = (datetime.datetime.now())
    in_data = data_object.readline().decode('ascii') #this last part is to pull out the extra junk.
   # print (type(in_data)) #  this is 'unicode" whatever that is  (the print works)
    in_data=int(in_data)
    print (in_data)  ##  this goes out to the python monitor;  every number
    i = i+1
    if (i==19):


        if (in_data > 1700000.0) and (in_data <1818000):
            value_two = in_data
        
            dynamic_data_entry_column_two()
        

        
        elif (in_data > 1818000.0) and (in_data < 1824000.0):
            value_four = in_data
            dynamic_data_entry_column_four()
            

        
        elif (in_data > 1824000) and (in_data < 1840000.0):
            value_three = in_data
            dynamic_data_entry_column_three()
            

        
        elif (in_data < 1700000) or (in_data > 18400000):# this has to be an elif
            value_five = in_data
            dynamic_data_entry_column_five() ##this is the error field
                                             ##not working???
           
         
    else :
        continue
    i=0         

"""   
   This is collecting one of 19, but this is an average.
 """
