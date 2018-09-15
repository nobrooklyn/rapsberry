#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

LED1 = 25
SW1  = 24

def my_callback(channel):
  global ledState
  if channel == SW1:
    ledState = not ledState
    if ledState == GPIO.HIGH:
      GPIO.output(LED1, GPIO.HIGH)
    else:
      GPIO.output(LED1, GPIO.LOW)

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(SW1, GPIO.RISING, callback=my_callback, bouncetime=200)

ledState = GPIO.LOW

try:
  while True:
    print ledState
    time.sleep(0.1)

except KeyboardInterrupt:
  pass

GPIO.cleanup()

print("done")
