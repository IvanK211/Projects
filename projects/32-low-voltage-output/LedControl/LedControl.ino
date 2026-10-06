// Low-energy indicator only: a correctly rated LED and current-limiting resistor.
// This is not a high-power LED, laser, motor or mains-load controller.
constexpr byte LED_PWM_PIN=5;
constexpr byte BUTTON_PIN=2;
unsigned long previous=0;
byte brightness=0;
void setup() {
  pinMode(LED_PWM_PIN,OUTPUT);analogWrite(LED_PWM_PIN,0);
  pinMode(BUTTON_PIN,INPUT_PULLUP);
}
void loop() {
  unsigned long now=millis();
  if(now-previous<25) return;
  previous=now;
  bool requested=digitalRead(BUTTON_PIN)==LOW;
  if(requested && brightness<60) ++brightness;
  if(!requested && brightness>0) --brightness;
  analogWrite(LED_PWM_PIN,brightness);
}
