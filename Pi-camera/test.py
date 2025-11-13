import RPi.GPIO as GPIO

# 경고 메시지를 끄는 것이 좋습니다.
GPIO.setwarnings(False) 

# BCM 또는 BOARD 모드 중 하나를 반드시 선택해야 합니다.
# 예시:
GPIO.setmode(GPIO.BCM) 

# 오류가 발생한 라인
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP) # 버튼 핀 설정