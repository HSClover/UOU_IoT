import board
import adafruit_dht
import time

dht_device = adafruit_dht.DHT22(board.D18)

while True:
    try:
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity

        if humidity is not None and temperature_c is not None:
            print(f"Temp={temperature_c:0.1f}°C  Humidity={humidity:0.1f}%")
        else:
            print("Failed to get reading. Try again!")

    except RuntimeError as error:
        print(error.args[0])
    except Exception as error:
        dht_device.exit()
        raise error

    time.sleep(2.0)