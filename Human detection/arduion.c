
int x;

void setup(){
    Serial.begin(9600);
    Serial.setTimeout(1);
}

void loop() {
  while (!Serial.available());
 x = Serial.readString().toInt();
 if (x==1)
 {
 Serial.println("Human Detected");
 else if(x!=1)
 {
  Serial.println("Human not detected");
 }
  
}
