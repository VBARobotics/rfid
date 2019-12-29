#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.cleanup()

redled = 7
dooropen = 8

GPIO.setup(redled,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(dooropen,GPIO.OUT,initial=GPIO.LOW)

reader = SimpleMFRC522()

while True:
    id, text= reader.read()
    print("id: " + str(id))
    print("Text: "+ text)
    if id==108374469526:
        print("Acces Granted")
        GPIO.output(dooropen,GPIO.HIGH)
    else:
        print("acces denied")
        GPIO.output(redled,GPIO.HIGH)

    sleep(3)
    GPIO.output(dooropen,GPIO.LOW)
    GPIO.output(redled,GPIO.LOW)
