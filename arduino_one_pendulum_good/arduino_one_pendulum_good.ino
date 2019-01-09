/* # The compiler never gets hung up with an 'if' statement.  It flies along and trips these triggers setting the times.  
The data goes out through the serial monitor as a flat file; just a series of numbers.  The Python catches these numbers,
sorts them by size and puts them accordingly in the sqlite3 database.
I was using photo interrupter modules.  The pendulum had a little vane that interrupted the IR radiation.  
It worked fine, but was delicate.  They defaulted LOW.  I moved to hall effect detectors.  These are magnetic.  
So there is a little magnet on the pendulum.  They default HIGH.  I am assuming that I need to change 
the HIGHS to LOWS and vice versa.  Then it occurred to me that it might work fine with no change. and that was the case.
My LEDs instead of flashing on, flash off.  But the program is exactly the same.  I thought that was cool.

*/


#define led_out 9
#define sensor_in 4

boolean val;//  this defines the variale for the input
boolean oldval;  //old state of the variable

long int mytime = 0 ;
long int oldtime = 0;
long int diftime = 0;
void setup() {
  // put your setup code here, to run once:
  pinMode (led_out, OUTPUT);
  pinMode (sensor_in, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  oldval = val;
  val = (digitalRead (sensor_in));


  if ((val == HIGH) && (oldval == LOW))  {
    digitalWrite (led_out, HIGH);


  }
  else if ((val == LOW) && (oldval == HIGH))  {
    digitalWrite (led_out, LOW);

  
    
      mytime = micros();
      diftime = mytime - oldtime;
      
      Serial.println (diftime);
      //Serial.print (" ");
      //Serial.print (" ");
      //Serial.print (diftime);

   
    oldtime = mytime;

  }
}
