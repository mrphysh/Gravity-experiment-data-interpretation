/* # The compiler never gets hung up with an 'if' statement.  It flies along and trips these triggers setting the times.  
The data goes out through the serial monitor as a flat file; just a series of numbers.  The Python catches these numbers,
sorts them by size and puts them accordingly in the sqlite3 database.
I was using photo interrupter modules.  The pendulum had a little vane that interrupted the IR radiation.  
It worked fine, but was delicate.  They defaulted LOW.  I moved to hall effect detectors.  These are magnetic.  
So there is a little magnet on the pendulum.  They default HIGH.  I am assuming that I need to change 
the HIGHS to LOWS and vice versa.  Then it occurred to me that it might work fine with no change. and that was the case.
My LEDs instead of flashing on, flash off.  But the program is exactly the same.  I thought that was cool.
This sketch is written for transparency, not to be elegant.
*/

#define led_out_9 9
#define led_out_10 10
#define led_out_11 11

#define sensor_in_4 4
#define sensor_in_5 5
#define sensor_in_6 6
/*  let's make the variable 4  5   and 6  and use it as a suffix

*/

boolean val_4;//  this defines the variale for the input
boolean oldval_4;  //old state of the variable
boolean val_5;//  this defines the variale for the input
boolean oldval_5;  //old state of the variable
boolean val_6;//  this defines the variale for the input
boolean oldval_6;  //old state of the variable


long int mytime_4 = 0 ;
long int oldtime_4 = 0;
long int diftime_4 = 0;

long int mytime_5 = 0 ;
long int oldtime_5 = 0;
long int diftime_5 = 0;

long int mytime_6 = 0 ;
long int oldtime_6 = 0;
long int diftime_6 = 0;


void setup() {
  // put your setup code here, to run once:
  pinMode (led_out_9, OUTPUT);
  pinMode (led_out_10, OUTPUT);
  pinMode (led_out_11, OUTPUT);
  pinMode (sensor_in_4, INPUT);
  pinMode (sensor_in_5, INPUT);
  pinMode (sensor_in_6, INPUT);

  Serial.begin(9600);
}

void loop() {
  /////////////////////////////////////////////////////
  /////       SENSOR IN 4 AND  LED OUT 9 THIS IS THETA, THE PENDULU ON THE RIGHT
  
  oldval_4 = val_4;
  val_4 = (digitalRead (sensor_in_4));
  while ((val_4 == HIGH) && (oldval_4 == LOW))  {
    digitalWrite (led_out_9, HIGH);
    break;
  }
  while ((val_4 == LOW) && (oldval_4 == HIGH))  {
    digitalWrite (led_out_9, LOW);
    mytime_4 = micros();
    diftime_4 = mytime_4 - oldtime_4;

    Serial.println (diftime_4);
    break;
  }


  oldtime_4 = mytime_4;
  
//////////////////////////////////////////////////////////
////      SENSOR IN 5 AND LED OUT 10  this is BETA  the one in the middle
 oldval_5 = val_5;
  val_5 = (digitalRead (sensor_in_5));
  while ((val_5 == HIGH) && (oldval_5 == LOW))  {
    digitalWrite (led_out_10, HIGH);
    break;
  }
  while ((val_5 == LOW) && (oldval_5 == HIGH))  {
    digitalWrite (led_out_10, LOW);
    mytime_5 = micros();
    diftime_5 = mytime_5 - oldtime_5;

    Serial.println (diftime_5);
    break;
  }


  oldtime_5 = mytime_5;
  //////////////////////////////////////////THIS IS ALPHA  
  
 oldval_6 = val_6;
  val_6 = (digitalRead (sensor_in_6));
  while ((val_6 == HIGH) && (oldval_6 == LOW))  {
    digitalWrite (led_out_11, HIGH);
    break;
  }
  while ((val_6 == LOW) && (oldval_6 == HIGH))  {
    digitalWrite (led_out_11, LOW);
    mytime_6 = micros();
    diftime_6 = mytime_6 - oldtime_6;

    Serial.println (diftime_6);
    break;
  }


  oldtime_6 = mytime_6;
  
  ////////////////////////////////////////
}
