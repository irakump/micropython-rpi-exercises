from machine import Pin
import time

"""
Exercise 1.1 - Implement an ASM chart in Python
The state machine controls lights with a push button. When the button is pressed the light
switches on immediately. The button has to be released before lamp can be switched off.
Then when the button is pressed again the light switches off. The following ASM-chart
specifies the state machine operation. Implement the state machine in MicroPython. Use
SW2 (Pin id: 7) for button and LED3 (Pin id: 20) for lamp. Clock frequency of the state
machine is 20 Hz (50 ms period)
"""

class ASM:
    def __init__(self, delay, switch, led):
        self.delay = delay # clock frequency
        self.switch = Pin(switch, Pin.IN, Pin.PULL_UP) # SW2 = push button = Pin 7
        self.led = Pin(led, Pin.OUT) # LED3 = lamp = Pin 20

    def on(self):
        self.led.on()
        time.sleep(self.delay)
    
    def off(self):
        self.led.off()
        time.sleep(self.delay)

asm = ASM(0.05, 7, 20) # 0.05 s = 50 ms

while True:
    
    if asm.switch.value() == 0: # button pressed, value = 0
        asm.on()
        #print('Led on')
        
        # button released
        while asm.switch.value() == 1:
            asm.on()
            #print('Led still on')
            
            # button pressed again, value = 0
            if asm.switch.value() == 0:
                while asm.switch.value() == 0:
                    asm.off()
                    #print('Led turned off')
                break # when switch value = 1
       
    else: # button not pressed = value = 1 = led off
        asm.off()
        #print('Led off')
        
