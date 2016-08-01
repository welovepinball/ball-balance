/* Arduino USB Keyboard HID input for ICB type game
*
* Turns inputs 2-53 into keyboard keystrokes by grounding the pin
*
*/



uint8_t buf[8] = { 0 };	/* Keyboard report buffer */
int pin;

void setup();
void loop();

void setup()
{
    Serial.begin(9600);
    delay(200);


    for (pin=2;pin<54;pin=pin+1){
      pinMode(pin,INPUT_PULLUP);
    }
}

void loop()
{
  int i;

  //clear buffer
  for (i = 2; i < 8; i = i + 1) {
     buf[i]=0;
  }
  i=2;

  for (pin=2;pin<54;pin=pin+1){
      pinMode(pin,INPUT_PULLUP);
      if( digitalRead(pin) == 0){
          buf[i] = pin+5;
          if (i<8){
            i++;
          }
        }
    }

Serial.write(buf, 8); // Send keypress
}
