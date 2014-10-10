#!/usr/bin/python

import time

try:
  import RPi.GPIO as gpio
except:
  print("Error importing RPi.GPIO")

'''EasyDriverPy module

Take control over the EasyDriver stepperdriver from the RaspberryPi
'''

__author__ = 'Robbert Verbruggen'
__version__ = '0.1'

class EasyDriver(object):
  '''EasyDriver class'''
  def __init__(self, pin_step = None, pin_dir = None, pin_ms1 = None, pin_ms2 = None, pin_slp = None, pin_rst = None, pin_enable = None, delay = 1):
    '''EasyDriver constructor

    Keyword arguments:
    pin_step -- GPIO-pin for the EasyDriver Step
    pin_dir -- GPIO-pin for the EasyDriver Dir
    pin_ms1 -- GPIO-pin for the EasyDriver MicroStep 1
    pin_ms2 -- GPIO-pin for the EasyDriver MicroStep 2
    pin_slp -- GPIO-pin for the EasyDriver Sleep
    pin_rst -- GPIO-pin for the EasyDriver Reset
    pin_enable -- GPIO-pin for the EasyDriver Enable
    delay -- Delay time between steps
    '''
    self.pin_step = pin_step
    self.pin_dir = pin_dir
    self.pin_ms1 = pin_ms1
    self.pin_ms2 = pin_ms2
    self.pin_slp = pin_slp
    self.pin_rst = pin_rst
    self.pin_enable = pin_enable
    self.delay = delay

    gpio.setmode(gpio.BOARD)

    if self.pin_step != None:
      gpio.setup(self.pin_step, gpio.OUT)

    if self.pin_dir != None:
      gpio.setup(self.pin_dir, gpio.OUT)
      gpio.output(self.pin_dir, True)

    if self.pin_ms1 != None:
      gpio.setup(self.pin_ms1, gpio.OUT)
      gpio.output(self.pin_ms1, False)

    if self.pin_ms2 != None:
      gpio.setup(self.pin_ms2, gpio.OUT)
      gpio.output(self.pin_ms2, False)

    if self.pin_slp != None:
      gpio.setup(self.pin_slp, gpio.OUT)
      gpio.output(self.pin_slp,True)

    if self.pin_rst > 0:
      gpio.setup(self.pin_rst, gpio.OUT)
      gpio.output(self.pin_rst,True)

    if self.pin_enable > 0:
      gpio.setup(self.pin_enable, gpio.OUT)
      gpio.output(self.pin_enable,False)

  def step(self):
    gpio.output(self.pin_step, True)
    time.sleep(self.delay)
    gpio.output(self.pin_step, False)
    time.sleep(self.delay)

  def dir(self, dir):
    gpio.output(self.pin_dir, dir)

  def set_full_step(self):
    gpio.output(self.pin_ms1, False)
    gpio.output(self.pin_ms2, False)

  def set_half_step(self):
    gpio.output(self.pin_ms1, True)
    gpio.output(self.pin_ms2, False)

  def set_quarter_step(self):
    gpio.output(self.pin_ms1, False)
    gpio.output(self.pin_ms2, True)

  def set_eight_step(self):
    gpio.output(self.pin_ms1, True)
    gpio.output(self.pin_ms2, True)

  def slp(self):
    gpio.output(self.pin_slp, False)

  def wake(self):
    gpio.output(self.pin_slp, True)

  def enable(self):
    gpio.output(self.pin_enable, False)

  def disable(self):
    gpio.output(self.pin_enable, True)

  def rst(self):
    gpio.output(self.pin_rst, False)
    time.sleep(1)
    gpio.output(self.pin_rst, True)

  def set_delay(self, delay):
    self.delay = delay

  def finish(self):
    gpio.cleanup()
