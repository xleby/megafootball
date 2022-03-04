#!/usr/bin/env pybricks-micropython
import math
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.iodevices import Ev3devSensor

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
compass = Ev3devSensor(Port.S2)
ev3.speaker.beep()
lm = Motor(Port.B)
rm = Motor(Port.C)
seeker = Ev3devSensor(Port.S3)

# Write your program here.
ev3.screen.clear()
kc = 1
ks = 20
v = 50
e = 0
alpha = 0

while True:
    seeker_result = seeker.read('AC-ALL')
    dir = seeker_result[0]
    ev3.screen.print(dir)
    u = (dir - 5) * ks
    ev3.screen.print(u)
    lm.dc(v + u)
    rm.dc(v - u)
    wait(10)

"""
while True:
    if e == 100:
        alpha = (alpha + 90) % 360
        e = 0
    angle_raw = compass.read('COMPASS')
    angle = angle_raw[0]
    err = alpha - angle
    er = err / 180
    if er > 0:
        er = math.floor(er)
    else:
        er = math.ceil(er)
    u = err - er * 360
    ev3.screen.print(u)
    lm.dc(v + u)
    rm.dc(v - u)
    wait(10)
    e+=1
"""
