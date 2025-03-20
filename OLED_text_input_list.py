import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

"""
Task 1.2
Implement a program that reads user input from the keyboard in an infinite loop. The input is typed in
Thonny Shell window while the program is running. The user input is drawn to the OLED screen starting
from the top of the screen. Each input is drawn below the previous one. When the screen is full the
display is scrolled up by one line and then new text is drawn at the bottom of the screen.
"""

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

words = []
x = 0
colour = 1

while True:
    y = 0
    oled.fill(0)
    
    if len(words) >= 8: # 64/8 = 8, so max 8 inputs in the list
        words.pop(0) # remove the first element 
    user_input = input('Write something: ')
    words.append(user_input)

    for w in words: 
        if y > 63:
            y = 55
        oled.text(w, x, y, colour)
        y += 8
    oled.show()
