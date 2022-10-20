input.onButtonPressed(Button.A, function () {
    if (level == 0) {
        level = 5
    }
    basic.clearScreen()
    button_action = 1
    basic.pause(100)
    level += -1
    speed = speed_list[level]
    basic.clearScreen()
    basic.showString("" + level)
    basic.pause(500)
    basic.clearScreen()
    button_action = 0
})
input.onButtonPressed(Button.AB, function () {
    if (target_counter == 3) {
        target_counter = 0
    }
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    x3 = 0
    y3 = 0
    basic.clearScreen()
    button_action = 1
    target_counter += 1
    basic.pause(100)
    basic.clearScreen()
    basic.showString("" + target_counter)
    basic.pause(500)
    basic.clearScreen()
    button_action = 0
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    button_action = 1
    basic.pause(100)
    if (x1 == 2 && y1 == 2 || x2 == 2 && y2 == 2 || x3 == 2 && y3 == 2) {
        for (let index = 0; index < 3; index++) {
            basic.clearScreen()
            basic.showIcon(IconNames.SmallHeart)
            basic.pause(100)
            basic.showIcon(IconNames.Heart)
            basic.pause(100)
        }
    } else {
        for (let index = 0; index < 1; index++) {
            basic.showIcon(IconNames.No)
            basic.pause(500)
            basic.clearScreen()
            basic.pause(500)
        }
    }
    basic.clearScreen()
    button_action = 0
})
let y3 = 0
let x3 = 0
let y2 = 0
let x2 = 0
let y1 = 0
let x1 = 0
let target_counter = 0
let speed = 0
let level = 0
let speed_list: number[] = []
let button_action = 0
button_action = 0
speed_list = [
100,
200,
500,
1000,
1500
]
level = 4
speed = speed_list[level]
basic.forever(function () {
    if (button_action != 1 && target_counter >= 1) {
        x1 = randint(0, 4)
        y1 = randint(0, 4)
        led.plot(x1, y1)
        basic.pause(speed)
        led.unplot(x1, y1)
    }
})
basic.forever(function () {
    if (button_action != 1 && target_counter >= 2) {
        x2 = randint(0, 4)
        y2 = randint(0, 4)
        led.plot(x2, y2)
        basic.pause(speed)
        led.unplot(x2, y2)
    }
})
basic.forever(function () {
    if (button_action != 1 && target_counter >= 3) {
        x3 = randint(0, 4)
        y3 = randint(0, 4)
        led.plot(x3, y3)
        basic.pause(speed)
        led.unplot(x3, y3)
    }
})
