from machine import Pin, ADC
import time

# set up pin 27 as an analog input
adc = ADC(Pin(27))

# define the conversion factor range 0 V to 3.3 V
conversion_factor = 3.3 / 65535

# initialize the LED pin
led = Pin("LED", Pin.OUT)

while True:
    # read analog input and convert to voltage
    adc_voltage = adc.read_u16() * conversion_factor
    print(adc_voltage)
    
    # scale the voltage to a delay time (0 to 1 seconds)
    delay_time = adc_voltage / 3.3
    
    # blink the led
    led.on()
    time.sleep(delay_time)
    led.off()
    time.sleep(delay_time)
    
