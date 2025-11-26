import RPi.GPIO as GPIO
import time

# 사용할 핀 번호
MOTOR_PWM = 23  # MDDS60 RC1 입력

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PWM, GPIO.OUT)

# PWM 주파수 설정
pwm = GPIO.PWM(MOTOR_PWM, 50)  # 50Hz
pwm.start(0)

def forward(speed=70):
    """
    speed = 0 ~ 100
    RC 모드에서 50% = 정지
    50% 이상 = 전진
    """
    duty = 50 + (speed * 0.5)  # speed=100 → duty75
    pwm.ChangeDutyCycle(duty)
    print(f"Forward: speed {speed}, duty {duty}")

def backward(speed=70):
    duty = 50 - (speed * 0.5)  # speed=100 → duty25
    pwm.ChangeDutyCycle(duty)
    print(f"Backward: speed {speed}, duty {duty}")

def stop():
    pwm.ChangeDutyCycle(50)
    print("STOP")

try:
    print("전진 3초...")
    forward(60)
    time.sleep(3)

    print("정지 1초...")
    stop()
    time.sleep(1)

    print("후진 3초...")
    backward(60)
    time.sleep(3)

    print("정지")
    stop()

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
