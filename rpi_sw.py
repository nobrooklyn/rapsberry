#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED1 = 25
SW1  = 24

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
  while True:
    print GPIO.input(SW1)
    if GPIO.input(SW1) == GPIO.HIGH:
      GPIO.output(LED1, GPIO.HIGH)
    else:
      GPIO.output(LED1, GPIO.LOW)

    time.sleep(0.1)

except KeyboardInterrupt:
  pass

GPIO.cleanup()

print("done")
