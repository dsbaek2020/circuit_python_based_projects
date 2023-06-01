
#Author: jelly-coding

# SPDX-FileCopyrightText: 2021 John Furcean
# SPDX-License-Identifier: MIT

import board
import digitalio
import time
from adafruit_seesaw import seesaw, rotaryio
# For use with RP2040
import busio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

#Arduino nano RP2040
i2c = busio.I2C(board.SCL, board.SDA)
"""I2C rotary encoder simple test example."""
seesaw = seesaw.Seesaw(i2c, 0x36)

#for Raspberry pi ? 
#i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
#seesaw = seesaw.Seesaw(i2c, addr=0x36)

seesaw_product = (seesaw.get_version() >> 16) & 0xFFFF
print("Found product {}".format(seesaw_product))
if seesaw_product != 4991:
    print("Wrong firmware loaded?  Expected 4991")

#seesaw.pin_mode(24, seesaw.INPUT_PULLUP)
#button = digitalio.DigitalIO(seesaw, 24)
#button_held = False

encoder = rotaryio.IncrementalEncoder(seesaw)
last_position = None

print('hello world')
while True:
    '''
    led.value = True
    time.sleep(0.2)
    led.value = False
    time.sleep(1)
    '''
    
    # negate the position to make clockwise rotation positive
    position = -encoder.position

    if position != last_position:
        last_position = position
        print("Position: {}".format(position))

    '''if not button.value and not button_held:
        button_held = True
        print("Button pressed")

    if button.value and button_held:
        button_held = False
        print("Button released")
        '''






