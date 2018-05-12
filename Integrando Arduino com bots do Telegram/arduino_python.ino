// arduino_python.ino

int led = 13;
void setup(){
    Serial.begin(9600);
    pinMode(led, OUTPUT);
}

void loop(){
    char light = Serial.read();
    if(light == '0') {
        digitalWrite(led, false);
    }else if(light == '1') {
        digitalWrite(led, true);
    }
}
