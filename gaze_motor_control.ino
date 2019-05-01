const int MotorPinA = 4; // direction motor 1 (Channel A)
const int MotorSpeedPinA = 5; // for motor 1 speed (channel A)

const int MotorPinB = 7; //direction motor 2 (channel B)
const int MotorSpeedPinB = 6; //for motor 2 speed (channel B)



void setup() {

  pinMode(MotorPinA, OUTPUT);
  pinMode(MotorSpeedPinA, OUTPUT);

  pinMode(MotorPinB, OUTPUT);
  pinMode(MotorSpeedPinB, OUTPUT);

  Serial.begin(9600);
  
  
}

void loop() {


  while(Serial.available())
  {

    

    
    int a = (int)Serial.read(); 

    if(a == 49){
    
    Serial.println("not acquired");
    digitalWrite(MotorPinA, LOW);
    analogWrite(MotorSpeedPinA, 0);
    digitalWrite(MotorPinB, LOW);
    analogWrite(MotorSpeedPinB, 0);}
    

    if(a == 50){
    
    Serial.println("straight_gaze");
    digitalWrite(MotorPinA, HIGH);
    analogWrite(MotorSpeedPinA, 189);
    digitalWrite(MotorPinB, HIGH);
    analogWrite(MotorSpeedPinB, 189);}

    if(a == 51){
    
    Serial.println("right_gaze");
    digitalWrite(MotorPinA, HIGH);
    analogWrite(MotorSpeedPinA, 189);
    digitalWrite(MotorPinB, LOW);
    analogWrite(MotorSpeedPinB, 0);}

    if(a == 52){
    
    Serial.println("left_gaze");
    digitalWrite(MotorPinA, LOW);
    analogWrite(MotorSpeedPinA, 0);
    digitalWrite(MotorPinB, HIGH);
    analogWrite(MotorSpeedPinB, 189);}

    
    


    
  }
  

}
