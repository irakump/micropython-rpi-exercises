from machine import Pin
import time

"""
Exercise 1.2 - Design and implement a state machine

An alarm system has two inputs: alarm signal and a button. Alarm signal goes high when
there is an alarm. Button can be pressed to acknowledge the alarm. There are two outputs:
red light and siren.
The alarm system works so that initially both light and siren are off.
• When alarm is activated both lamp and siren go on.
• When the button is pressed the alarm acknowledged. If the alarm is still active when
it is acknowledged the siren is switched off and the red light starts to blink. The red
light keeps on blinking until the alarm is deactivated.
• If the alarm is deactivated before button has been pressed the siren is switched off
and red light stays on until user presses button.
Draw ASM chart of the alarm system and implement it in MicroPython.
For testing we use button for input signals. The buttons are grounding so they read 0 when
pressed and 1 when NOT pressed. That’s why input signal = 0 indicates active signal in out
tests.
You have following input signals:
• Button (0 = pressed): SW2 (Pin id: 7)
• Alarm (0 = alarm is active), SW0 (Pin id: 9)
You have following output signals:
• Red lamp (1 = lamp is on): LED1 (Pin id:22)
• Siren (1 = siren is on): LED3 (Pin id:20)
"""

class ASM:
    def __init__(self, delay, button, alarm, red, siren):
        self.delay = delay # clock frequency
        self.button = Pin(button, Pin.IN, Pin.PULL_UP) # SW2 = push button = Pin 7
        self.alarm = Pin(alarm, Pin.IN, Pin.PULL_UP) # SW0 = Pin 9
        self.red = Pin(red, Pin.OUT) # LED1, Pin = 22
        self.siren = Pin(siren, Pin.OUT) # LED3, Pin = 20
        self.state = 'alarm_off'

    def red_on(self):
        self.red.on()
        time.sleep(self.delay)
        
    def siren_on(self):
        self.siren.on()
        time.sleep(self.delay)
    
    def red_off(self):
        self.red.off()
        time.sleep(self.delay)
        
    def siren_off(self):
        self.siren.off()
        time.sleep(self.delay)
    
    def update_state(self):
        
        if self.state == 'alarm_off':
            self.red_off()
            self.siren_off()
            #print(self.state) # for debugging
            if self.alarm.value() == 0:
                self.state = 'alarm_active'     
                
        elif self.state == 'alarm_active': # alarm value 0
            self.red_on()
            self.siren_on()
            #print(self.state)
            if self.button.value() == 0 and self.alarm.value() == 0:
                self.state = 'alarm_acknowledged'
            elif self.button.value() == 1 and self.alarm.value() == 1:
                self.state = 'alarm_turning_off'
        
        elif self.state == 'alarm_turning_off':
            self.red_on()
            self.siren_off()
            #print(self.state)
            if self.button.value() == 0:
                self.state = 'alarm_off'
        
        elif self.state == 'alarm_acknowledged':
            self.siren_off()
            #print(self.state)
            while self.alarm.value() == 0:
                self.red_on() # red light flashing
                self.red_off()
                #print(self.state)
            if self.alarm.value() == 1:
                self.state = 'alarm_off'
        

asm = ASM(0.1, 7, 9, 22, 20) # 0.1 s = 100 ms clock frequency

while True:
    asm.update_state()
