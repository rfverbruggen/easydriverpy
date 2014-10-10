EasyDriverPy
============

Take control over the EasyDriver stepperdriver from the RaspberryPi

Usage:

'''python

import easydriver as ed

# set direction booleans:
#    cw - clockwise
#    cww - counterclockwise
cw = True
ccw = False

# initialize easyDriver
#    pin_step - GPIO pin 23
#    pin_dir - GPIO pin 24
easyDriver = ed(23, 24)

# set direction
easyDriver.dir(cw)

# make 100 steps
for i in range(0, 100):
  easyDriver.step()

# clean up
easyDriver.finish()
'''
