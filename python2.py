from gpiozero import Servo
from time import sleep

# BCM 23 사용
PIN = 23

# MDDS60 같은 RC 입력과 호환되도록 min/max pulse를 명시 (1ms~2ms)
servo = Servo(PIN, min_pulse_width=0.001, max_pulse_width=0.002, frame_rate=50)

def neutral():
    servo.value = 0    # 0 -> 중립 (약 1.5ms)
    print("Set: neutral (1.5ms)")

def forward():
    servo.value = 1    # 최대 전진 (약 2.0ms)
    print("Set: forward (~2.0ms)")

def backward():
    servo.value = -1   # 최대 후진 (약 1.0ms)
    print("Set: backward (~1.0ms)")

try:
    print("중립 1초")
    neutral()
    sleep(1)

    print("전진 3초")
    forward()
    sleep(3)

    print("중립 1초")
    neutral()
    sleep(1)

    print("후진 3초")
    backward()
    sleep(3)

    print("중립")
    neutral()

except KeyboardInterrupt:
    neutral()
