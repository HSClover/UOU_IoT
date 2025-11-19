from picamera2 import Picamera2
import time

# Picamera2 객체를 생성합니다.
picam2 = Picamera2()

# 미리보기를 위해 카메라 구성을 시작합니다.
print("카메라 미리보기 시작 (5초 후 종료)...")
picam2.start_preview()

# 미리보기 화면을 잠시 유지합니다.
time.sleep(5)

# 미리보기를 중지합니다.
picam2.stop_preview()

# 정지 이미지 저장을 위한 카메라 구성을 합니다.
camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)})
picam2.configure(camera_config)
picam2.start()

# 캡처 전에 잠시 기다립니다.
time.sleep(2)

# 이미지를 캡처하고 저장합니다.
file_name = "test_image.jpg"
picam2.capture_file('/home/pi/Documents/UOU_IoT/Pi-camera/' + file_name)
print(f"사진이 성공적으로 촬영되어 '{file_name}'으로 저장되었습니다.")

# 카메라 자원을 해제합니다.
picam2.stop()