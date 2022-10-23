def on_button_pressed_a():
    global Arm
    Arm = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Arm
    Arm = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

Arm = 0
radio.set_group(1)
basic.show_leds("""
    . . # # #
        . . # . #
        . . # # #
        . . # # .
        . . # . #
""")

def on_forever():
    led.toggle(2, 2)
    if input.rotation(Rotation.PITCH) < 50 and input.rotation(Rotation.PITCH) > -50:
        radio.send_value("right",
            Math.round(Math.map(Math.constrain(input.rotation(Rotation.ROLL), -90, 90),
                    0,
                    90,
                    90,
                    120)))
        serial.write_line("" + str((Math.round(Math.map(Math.constrain(input.rotation(Rotation.ROLL), -90, 90),
                0,
                90,
                90,
                120)))))
basic.forever(on_forever)
