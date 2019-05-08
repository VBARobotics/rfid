#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

#NOte that the MFRC522 requires Board numbering thus all components use Board as opposed to BMC Numbering
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.cleanup()

redled = 7
greenled = 18
motoropen = 11
motorclose = 8

GPIO.setup(motoropen,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(motorclose,GPIO.OUT,initial=GPIO.LOW)

GPIO.setup(redled,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(greenled,GPIO.OUT,initial=GPIO.LOW)

reader = SimpleMFRC522()

while True:
    id, text= reader.read()
    print("id: " + str(id))
    print("Text: "+ text)
    if id==370554718609:
        print("This is the correct Card")
        GPIO.output(greenled,GPIO.HIGH)
        GPIO.output(motoropen,GPIO.HIGH)
        sleep(4)
        GPIO.output(motoropen,GPIO.LOW)
    else:
        print("Authorization Denied")
        GPIO.output(redled,GPIO.HIGH)

    sleep(3)
    GPIO.output(greenled,GPIO.LOW)
    GPIO.output(redled,GPIO.LOW)
