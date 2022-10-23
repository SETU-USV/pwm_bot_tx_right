input.onButtonPressed(Button.A, function () {
    Arm = 1
})
input.onButtonPressed(Button.B, function () {
    Arm = 0
})
let Arm = 0
radio.setGroup(1)
basic.showLeds(`
    . . # # #
    . . # . #
    . . # # #
    . . # # .
    . . # . #
    `)
basic.forever(function () {
    if (Arm == 1) {
        led.toggle(2, 2)
        if (input.rotation(Rotation.Pitch) < 50 && input.rotation(Rotation.Pitch) > -50) {
            radio.sendValue("right", Math.round(Math.map(Math.constrain(input.rotation(Rotation.Roll), -90, 90), 0, 90, 90, 120)))
        }
    }
})
