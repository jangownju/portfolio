const int fan_pin = 19;
const int fan_channel=1;
const int fan_resolution=10;

const int melody[]={
  //262,294,330,349,393,440,494,523, 도~도
  //262,294,330,349,393,393,440,440,393,440,523,494,440,393,349,330,294,262 성난 허수아비
 
  //392,524,587,659,587,524,524,392,524,598,659,587,524,587,659,659,392,524,587,659,587,524,524,392,524,598,659,587,524,587,784,659,
 // 659,698,784,784,784,784,784,659.524,659,698,784,784,784,784,784,659.524, summer
 330,440,524,659,659,659,587,524,494,524,524,524,440,524,659,880,880,880,880,989,784,698,784 하울의 움직이는성
};
void setup() {
     ledcAttachPin(fan_pin,fan_channel);

     for(int note=0;note<23;note++){
           ledcSetup(fan_channel,melody[note],fan_resolution);
           ledcWrite(fan_channel,10);
           delay(500);

           ledcWrite(fan_channel,0);
           delay(50);

     }

     ledcWrite(fan_channel,0);
}

void loop(){

}

