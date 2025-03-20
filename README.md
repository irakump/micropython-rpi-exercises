# A collection of exercises for Raspberry Pi

## [ADC to LED blink](https://github.com/irakump/micropython-rpi-exercises/blob/main/adc_to_led_blink.py)

Reading RPI Pico ADC value in MicroPython

In this exercise you need to implement a program that reads ADC value and blinks the Pico’s onboard LED.
The frequency of blinking is controlled by the ADC count.

## [Binary Numbers to LEDs](https://github.com/irakump/micropython-rpi-exercises/blob/main/binary_numbers_to_leds.py)

Your task is to write a program that waits for the user to press a button on the proto board.
When the user presses the button, a variable is incremented by one. If the value is over seven,
then the variable is set to zero. By pressing the button repeatedly, you can cycle the variable
through numbers 0 – 7. In addition to incrementing the variable, the program displays the number
in binary using the proto board’s LEDs.

## [OLED line drawing buttons](https://github.com/irakump/micropython-rpi-exercises/blob/main/OLED_line_drawing_buttons.py) 

Implement a program that uses the three development board buttons to control line drawing. When the
program starts, it starts to draw pixels from the left side of the screen halfway between top and bottom
of the screen and constantly moves towards the right edge of the screen. When the drawing reaches the
right edge of the screen, the drawing is wrapped back to the left side. Buttons SW0 and SW2 are used to
move the pixels towards the top or bottom of the screen, so that by pressing buttons you can draw lines
at different heights. Pressing SW1 clears the screen and continues drawing from middle left side.

## [OLED move character](https://github.com/irakump/micropython-rpi-exercises/blob/main/OLED_move_character.py)

Implement a program that uses the two development board buttons to control a “UFO”. The UFO is
shown at the bottom of the screen with characters “<=>”. SW0 and SW2 are used to move the UFO left
and right. The program must stop the UFO at the edges of the screen so that it is completely visible.
When UFO is at left edge it must only be possible to move the UFO right and vice versa.
The font size is 8x8 pixels.

## [OLED text input list](https://github.com/irakump/micropython-rpi-exercises/blob/main/OLED_text_input_list.py)

Implement a program that reads user input from the keyboard in an infinite loop. The input is typed in
Thonny Shell window while the program is running. The user input is drawn to the OLED screen starting
from the top of the screen. Each input is drawn below the previous one. When the screen is full the
display is scrolled up by one line and then new text is drawn at the bottom of the screen.

## [State machine alarm system](https://github.com/irakump/micropython-rpi-exercises/blob/main/state_machine_alarm_system.py)

Design and implement a state machine

An alarm system has two inputs: alarm signal and a button. Alarm signal goes high when
there is an alarm. Button can be pressed to acknowledge the alarm. There are two outputs:
red light and siren.

The alarm system works so that initially both light and siren are off.
- When alarm is activated both lamp and siren go on.
- When the button is pressed the alarm acknowledged. If the alarm is still active when
it is acknowledged the siren is switched off and the red light starts to blink. The red
light keeps on blinking until the alarm is deactivated.
- If the alarm is deactivated before button has been pressed the siren is switched off
and red light stays on until user presses button.
Draw ASM chart of the alarm system and implement it in MicroPython.

For testing we use button for input signals. The buttons are grounding so they read 0 when
pressed and 1 when NOT pressed. That’s why input signal = 0 indicates active signal in out
tests.

## [State machine LED control](https://github.com/irakump/micropython-rpi-exercises/blob/main/state_machine_led_control.py)

Implement an ASM chart in Python

The state machine controls lights with a push button. When the button is pressed the light
switches on immediately. The button has to be released before lamp can be switched off.
Then when the button is pressed again the light switches off. The following ASM-chart
specifies the state machine operation. Implement the state machine in MicroPython. Use
SW2 (Pin id: 7) for button and LED3 (Pin id: 20) for lamp. Clock frequency of the state
machine is 20 Hz (50 ms period)
