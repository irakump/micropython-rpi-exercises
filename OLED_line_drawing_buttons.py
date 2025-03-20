import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

"""
Task 1.3
Implement a program that uses the three development board buttons to control line drawing. When the
program starts, it starts to draw pixels from the left side of the screen halfway between top and bottom
of the screen and constantly moves towards the right edge of the screen. When the drawing reaches the
right edge of the screen, the drawing is wrapped back to the left side. Buttons SW0 and SW2 are used to
move the pixels towards the top or bottom of the screen, so that by pressing buttons you can draw lines
at different heights. Pressing SW1 clears the screen and continues drawing from middle left side.
"""
button0 = Pin(9, Pin.IN, Pin.PULL_UP) # SW0
button1 = Pin(8, Pin.IN, Pin.PULL_UP) # SW1
button2 = Pin(7, Pin.IN, Pin.PULL_UP) # SW2

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

oled.fill(0)
x = 0
y = 32 # halfway
colour = 1

while True:
    if button0() == 0: # button pressed
        y += 1 # move down
        if y >= 63:
            y = 63
        oled.pixel(x, y, colour)
    
    elif button2() == 0:
        y -= 1 # move up
        if y < 0:
            y = 0
        oled.pixel(x, y, colour)
    
    elif button1() == 0:
        oled.fill(0) # clear the display
        x = 0
        y = 32
    
    oled.pixel(x, y, colour)
    x += 1
    if x >= 128: # when the line reaches right edge
        x = 0
    oled.show()
