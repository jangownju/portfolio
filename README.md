# **PORTFOLIO**

## **📗 목차**

<b>
  
  - 📝 [개요]
  - 👨🏻‍💻 [프로젝트]
    - [Turtle을 활용한 게임](#1-TurTle을-활용한-게임)
    - [Aduino 드론](#2-Aduino-드론)
    - [Aduino 자동차](#3-Aduino-자동차)
    - [Tello 드론 ](#4-Tello-드론)

</b>

## **📝 포트폴리오 개요**

![initail](https://user-images.githubusercontent.com/132328203/236523687-f5ecd58d-3163-4909-bb0c-4d25ea00c002.jpg)

> **프로젝트:** 2023 로봇·AI(인공지능) 핵심인재 양성교육
>
> **제작자:** 주장원
>
> **제작 기간:** 2023.03.27~2023.05.03
>
> **사용 기술:** thonny, aduino
>
> **문의:** jangwonju383@gmail.com
<br />

## **👨🏻‍💻 프로젝트**

### [**1. TurTle을-활용한-게임**](https://github.com/jangownju/portfolio/tree/main/game_turtle)

<img width="100%" alt="터틀을 활용한 게임" src="https://user-images.githubusercontent.com/132328203/236529746-e21cdc34-f7d0-4317-b615-fd01a21b1182.png" />

- 터틀을 사용하여 구현한 게임 
- pygame을 사용하지 않고 구현 
- 적이 계속 내려오는 가운데 캐릭터가 총알을 사용하여 적을 맞추는 게임 

### [**2.Aduino 드론**](https://github.com/jangownju/portfolio/tree/main/drone_aduino)

<img width="100%" alt="Aduino 드론" src="https://user-images.githubusercontent.com/132328203/236535681-f52a3c04-d25c-4765-be98-1b6fbde03c71.jpg" />

- [모터 제어하기](https://github.com/jangownju/portfolio/blob/main/drone_aduino/turn_motor_in_turn.ino)
   각 날개의 모터를 번갈아 작동시키며 모터의 작동여부를 확인 
- [LED 불빛 제어하기](https://github.com/jangownju/portfolio/blob/main/drone_aduino/on_and_off_LED.ino)
   LED를 키고 끔으로서 불빛을 어둡게 혹은 밝게 조절할수 있도록 구현 
- [모터로 노래 연주하기](https://github.com/jangownju/portfolio/blob/main/drone_aduino/song_aduino.ino)
  모터의 주파수를 활용한 노래 연주
  특정 구간을 활성화/비활성화 함으로 노래 선택이 가능 하도록 구현 

### [**3. Aduino-자동차**](https://github.com/jangownju/portfolio/tree/main/car)

<img width="100%" alt="반응형" src="https://user-images.githubusercontent.com/132328203/236538535-9ea76b3d-869d-4231-9e73-47e9fddd8825.jpg" />

- [원격 조종하기](https://github.com/jangownju/portfolio/blob/main/car/video_joystick.py)
  조이스틱을 구현, 카메라 센서를 이용하여 자동차를 조종가능하도록 구현 
- [자율 주행](https://github.com/jangownju/portfolio/blob/main/car/ai_driving.py)
  [DataColletcion](https://github.com/jangownju/portfolio/blob/main/car/video_joystick_data_collection.py)을 이용하여 원격조종한 데이터를 
  수집시킴
- [CNN Training](https://github.com/jangownju/portfolio/blob/main/car/cnn_training.py)으로 수집된 데이터를 학습
  만들어진 model과 data파일을 활용하여 [Ai driving](https://github.com/jangownju/portfolio/blob/main/car/ai_driving.py)을 구현 
  
### [**4. Tello Drone**](https://github.com/jangownju/portfolio/tree/main/drone_tello)

<img width="100%" alt="Tello Drone" src="https://user-images.githubusercontent.com/132328203/236541168-44d45586-dcaa-4581-9ebc-d536969c2d7c.jpg" />

- Python을 활용하여 드론의 [카메라 데이터](https://github.com/jangownju/portfolio/blob/main/drone_tello/Receive%20Tello%20Video%20Stream-OpenCV.py) [위치 데이터](https://github.com/jangownju/portfolio/blob/main/drone_tello/Receive%20Tello%20State.py)를 수집
- [KEY MODUL](https://github.com/jangownju/portfolio/blob/main/drone_tello/KeyPressedModule.py)을 사용하여 [드론과 연결](https://github.com/jangownju/portfolio/blob/main/drone_tello/Drone%20Control%20to%20Key.py) 후 직접 키를 사용하여 드론을 원격조종이 가능하도록 구현
- 드론이 나의 얼굴을 인식하여 따라오도록 설계 

