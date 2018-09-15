#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED1 = 25
GPIO.setup(LED1, GPIO.OUT)

try:
  for i in range(10):
    print(i)
    GPIO.output(LED1, GPIO.HIGH)
    time.sleep(0.2)
  
    GPIO.output(LED1, GPIO.LOW)
    time.sleep(0.3)

except KeyboardInterrupt:
  pass

GPIO.cleanup()

print("done")
