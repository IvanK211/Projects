// Bench-only two-team timer. No pyrotechnics, emitters, sirens or weapon interfaces.
// Buttons connect each reference input to ground; LED is the board indicator.
constexpr byte TEAM_A=2, TEAM_B=3, PAUSE=4;
constexpr unsigned long DEBOUNCE_MS=35;
struct Button {
  byte pin; bool raw=HIGH; bool stable=HIGH; unsigned long changed=0;
  bool pressed(unsigned long now) {
    bool reading=digitalRead(pin);
    if(reading!=raw) {raw=reading;changed=now;}
    if(stable!=raw && (unsigned long)(now-changed)>=DEBOUNCE_MS) {
      stable=raw; return stable==LOW;
    }
    return false;
  }
};
Button a{TEAM_A}, b{TEAM_B}, pauseButton{PAUSE};
int active=-1;
unsigned long previous=0, reportAt=0;
unsigned long long elapsed[2]={0,0};
void setup() {
  Serial.begin(9600); pinMode(TEAM_A,INPUT_PULLUP);pinMode(TEAM_B,INPUT_PULLUP);
  pinMode(PAUSE,INPUT_PULLUP);pinMode(LED_BUILTIN,OUTPUT);
  previous=millis(); Serial.println(F("Timer ready; starts paused."));
}
void loop() {
  unsigned long now=millis();
  unsigned long delta=now-previous;previous=now; // Unsigned subtraction handles one millis rollover.
  if(active>=0) elapsed[active]+=delta;
  bool pressA=a.pressed(now),pressB=b.pressed(now),pressPause=pauseButton.pressed(now);
  if(pressPause || (pressA && pressB)) active=-1;
  else if(pressA) active=0;
  else if(pressB) active=1;
  digitalWrite(LED_BUILTIN,active>=0 ? HIGH : LOW);
  if((unsigned long)(now-reportAt)>=1000) {
    reportAt=now;Serial.print(F("A seconds: "));Serial.print((unsigned long)(elapsed[0]/1000));
    Serial.print(F(" | B seconds: "));Serial.print((unsigned long)(elapsed[1]/1000));
    Serial.print(F(" | active: "));Serial.println(active);
  }
}
