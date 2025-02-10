from machine import Pin, PWM # PWM = Pulse Width Modulation, to control the brightness
import time

"""
Exercise: Binary Numbers to LEDs

Your task is to write a program that waits for the user to press a button on the proto board.
When the user presses the button, a variable is incremented by one. If the value is over seven,
then the variable is set to zero. By pressing the button repeatedly, you can cycle the variable
through numbers 0 – 7. In addition to incrementing the variable, the program displays the number
in binary using the proto board’s LEDs.
"""

# create class Button
class Button:
    def __init__(self, id):
        self.button = Pin(id, Pin.IN, Pin.PULL_UP)
    
    def pressed(self):
        if self.button.value() == 0: # button pressed
            time.sleep(0.05) # debounce delay in ms
            if self.button.value() == 0: # confirm button is still pressed
                while self.button.value() == 0:
                    pass # wait for button release
                return True
        return False
        
# create class Led
class Led:
    def __init__(self, id):
        self.led = PWM(Pin(id, Pin.OUT))
        self.led.freq(1000) # set PWM frequency to 1kHz
        self.brightness = 50 # set low brightness, ~0.08% (50 / 65535 x 100) # 100% would be 65535 = led fully on
                          
    def turn_on(self):
        self.led.duty_u16(self.brightness) # the method duty_u16 sets the duty cycle of a PWM signal using a 16-bit value 
                          
    def turn_off(self):
        self.led.duty_u16(0) # duty cycle 0% = led off
       
# define button   
button = Button(12)

# variable for button
button_number = 0

# define pins
led1 = Led(22)
led2 = Led(21)
led3 = Led(20)

# set led values to binary numbers, off = 0, on = 1
def set_led_values(button_number):
    # set led 1, bitwise operation
    if button_number & 1: # 1 = 001 = the first bit
        led1.turn_on()
    else:
        led1.turn_off()
    
    # led 2 
    if button_number & 2: # 2 = 010, the second bit
        led2.turn_on()
    else:
        led2.turn_off()
    
    # led 3
    if button_number & 4: # 4 = 100, the third bit
        led3.turn_on()
    else:
        led3.turn_off()

while True: # always true = infinite loop
    if button.pressed():
        button_number += 1
        if button_number > 7:
            button_number = 0
    set_led_values(button_number)
    #print(button_number) # for debugging
    time.sleep(0.1) # small delay to avoid fast looping    
