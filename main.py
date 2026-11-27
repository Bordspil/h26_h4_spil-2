#IMPORTS
from machine import Pin, PWM
from random import randint
import neopixel
from time import sleep_ms, ticks_ms

#WIN LEDS
winsledp1 = [
    Pin(??, Pin.OUT),
    Pin(??, Pin.OUT),
    Pin(??, Pin.OUT),
]

winsledp2 = [
    Pin(??, Pin.OUT),
    Pin(??, Pin.OUT),
    Pin(??, Pin.OUT),
]

#PLAYER 1 BUTTONS
p1takka = [
    Pin(??, Pin.IN, Pin.PULL_UP),
]

p1takki2 = [
    Pin(??, Pin.IN, Pin.PULL_UP),
]

#PLAYER 2 BUTTONS
p2takka = [
    Pin(??, Pin.IN, Pin.PULL_UP),
]

p2takki2 = [
    Pin(??, Pin.IN, Pin.PULL_UP),
]

#NEOPIXEL
npscore = neopixel.NeoPixel(Pin(??, Pin.OUT), 10)

np = neopixel.NeoPixel(Pin(??, Pin.OUT), 60)


