
#include <Servo.h>

int x;
int y;
String serialData;
Servo servo_x; 
Servo servo_y;

void setup() {
  Serial.begin(9600);
  servo_x.attach(10);
  servo_y.attach(9);
  Serial.setTimeout(15);
  servo_x.write(0);
  servo_y.write(0);
  
}

void loop(){
  serialData = Serial.readString();
  x = parseDataX(serialData);
  y = parseDataY(serialData);

  
  servo_x.write(180 - x); 
  servo_y.write(y + 70);       
  
     
  delay(1000);
}
int parseDataX(String str){
  str.remove(str.indexOf("Y"));
  str.remove(str.indexOf("X"), 1);

  return str.toInt();
  

  }
int parseDataY(String str){
  str.remove(0, str.indexOf("Y")+1);

  

  return str.toInt();
  

  }
