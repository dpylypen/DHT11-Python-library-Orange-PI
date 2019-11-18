# from pyA20.gpio import gpio
# from pyA20.gpio import port
import OPi.GPIO as GPIO


#import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
#gpio.setwarnings(False)
#gpio.setmode(GPIO.BCM)
# PIN2 = port.PA6
PIN2 = 7
GPIO.setup(GPIO.BOARD)
#gpio.cleanup()


# read data using pin 14
instance = dht11.DHT11(pin=PIN2)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)

    time.sleep(1)
