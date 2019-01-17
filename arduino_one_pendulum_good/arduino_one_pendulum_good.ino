/* # The compiler hangs up on an 'if' statement and waits for the next trigger.  
this was fine, but precluded monitoring more than a single timing event.  
this sketch is no longer used.  
But for persons interesting in following this thread, it is a good starting place

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
