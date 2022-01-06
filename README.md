README FOR ARDUINO, C++, PYTHON, SQLITE3 DATA CAPTURE
Generic README for all three repositories.

Two of the fundamental constants in physical science are gravity and mass.  My academic qualifications to approach this question are not strong, but I have the diverse background, creativity and curiosity to ask this question:  are they really constant?  I think of myself as the creative lab tech that came up with the question and the path toward an answer, but realize that my limits stop me at that point.   These experiments may indicate that gravity and mass are not constant.  If this is indicated (I hesitate to use the word ‘proven’) then I need to pass it all to another team.
 
Gravity is assumed to be a constant.   The experiment is fairly straightforward:  look carefully at the period of a pendulum.  If there are variations in the period, then this indicates that gravity is not constant.  (Everything else is constant)
The power of this primitive experiment is the “micros()” function in C++.  The micros() function returns the number of microseconds from the time, the Arduino board begins running the current program. This number overflows i.e. goes back to zero after approximately 70 minutes
The anniversary clock is the one that is always found in a glass dome, about 14 inches high.  There is a shiny brass thing with four balls that rotates back and forth.  The period of the rotation is determined by a complex set of variables, but at the center of this is the mass.  This experiment proposes that variations in the period indicate that mass is not constant.  Let’s hold all variables constant.   For example, during the months of January and February, the period goes down, that is; the rotor speeds up,    This indicates that the mass of the rotating object has gone down.  This is complicated, but mass is at the center.
This is all about the reproducibility of the data.  The specifics of the period are not of interest.

I originally joined GitHub to invite, even ask for help.  I thought that there was a general need for this software development and still believe this.  But I did not understand how the platform was to be used and, in any event, never attracted any attention.  

I developed it all myself and have looked at the data and found data that needs another set of eyes, that is, a peer review, as it is called in academic circles.  This GitHub account is changed to present the software with this project.   This project is largely software development.   I think this is fair.   It is divided into three repositories:  
Arduino, C++ , Python, sqlite3  data capture for gravity and mass experiment.
xxxxxxxxxxxxxxxxxxxxx     xxxxxxxxxxxxxxxxxx

The Arduino microcontroller is a small, inexpensive computer that makes it easy for any computer to interact with the outside world.  It accepts input from sensors, sends output to motors, solenoids, lights etc.   I write a little program in C++ and put it in the little computer (Arduino Uno) and the program accepts input creates output and sends out data.  I have little understanding of it, but it is not difficult to do cool thigs with it.

The signals come in through a Hall detector.  There is a magnet on the pendulum.  At the end of its swing the magnet trips the Hall.  Two signals result in a time interval which it then sends  out and to a computer through the computer’s serial port.  

In the computer the signal is caught by Python.  The data is from clocks, is precise and accurate.  The Python sorts the numbers by size, adds a UNIX time stamp and puts it in a table in a sqlite3 database.

There was an enormous amount of development behind both the C++ and the Python, but in the end neither is tremendously complex.

The data streams are through essentially clocks which are both accurate and precise.  The Python simply separates them by size with ‘if’ statements.    Some of the fields threatened to overlap with others and I added 30 million and 20 million to two of the data streams respectively.  These were added unambiguously at the input.  With these, the Python was able to absolutely separate them.

This repository shows this software.  The languages are C++ and Python and the database is sqlite3.  
Quickly, the columns are
Column_one     	UNIX timestamp
Column_two	data stream
Colum_three	data stream
Column_four	data stream. Etc
Column_last	error…exceptions
The bulk of the databases have eight columns.  Timestamp,  six data and one exception

Arduino  C++  and Python
The Arduino code is pretty typical logic statements:  If  var == high and old_var ==low then    etc etc.
There are two experiments under the same platform.  The Hall is at the end of the swing of the pendulum.  With the rotating pendulums the Hall is placed in the middle.  That is, every other high to low is the trigger.  This required an extra set of Boolean variables.  It took me weeks to figure this out.  So, there are two different sets of logic gates.  It uses only the serial library.
The interval of the actual Hall signal (how long is the signal high) does not impact the data.
The Python mostly can cleanly separate them but there were some problems.  I added 20 and 30 million to respective inputs, such that the Python could more definitely separate them and then subtracted it before adding to the database.  The Python uses these libraries: serial  sqlite3 datetime OS.
This repository includes copies of these programs.

https://youtu.be/PH7FHUDZ4PM

