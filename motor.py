from gpiozero import Motor
from time import sleep
# For two wheeled robot.
motor = Motor(forward=17, backward=14)

while True:
    motor.forward()
    sleep(5)
    motor.backward()
    sleep(5)
