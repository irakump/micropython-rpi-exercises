## A collection of exercises for Raspberry Pi

### Binary Numbers to LEDs

Your task is to write a program that waits for the user to press a button on the proto board.
When the user presses the button, a variable is incremented by one. If the value is over seven,
then the variable is set to zero. By pressing the button repeatedly, you can cycle the variable
through numbers 0 – 7. In addition to incrementing the variable, the program displays the number
in binary using the proto board’s LEDs.

### ADC to LED blink

Reading RPI Pico ADC value in MicroPython

In this exercise you need to implement a program that reads ADC value and blinks the Pico’s onboard LED.
The frequency of blinking is controlled by the ADC count.

### State machine LED control

Implement an ASM chart in Python

The state machine controls lights with a push button. When the button is pressed the light
switches on immediately. The button has to be released before lamp can be switched off.
Then when the button is pressed again the light switches off. The following ASM-chart
specifies the state machine operation. Implement the state machine in MicroPython. Use
SW2 (Pin id: 7) for button and LED3 (Pin id: 20) for lamp. Clock frequency of the state
machine is 20 Hz (50 ms period)
