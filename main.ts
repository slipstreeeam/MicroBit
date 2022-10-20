input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (level == 0) {
        level = 5
    }
    
    basic.clearScreen()
    button_action = 1
    basic.pause(100)
    level = level - 1
    speed = speed_list[level]
    basic.clearScreen()
    basic.showString("" + ("" + level))
    basic.pause(500)
    basic.clearScreen()
    button_action = 0
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    basic.clearScreen()
    button_action = 1
    basic.pause(100)
    if (x == 2 && y == 2) {
        for (let index = 0; index < 3; index++) {
            basic.clearScreen()
            basic.showIcon(IconNames.SmallHeart)
            basic.pause(100)
            basic.showIcon(IconNames.Heart)
            basic.pause(100)
        }
    } else {
        for (let index2 = 0; index2 < 1; index2++) {
            basic.showIcon(IconNames.No)
            basic.pause(500)
            basic.clearScreen()
            basic.pause(500)
        }
    }
    
    basic.clearScreen()
    button_action = 0
})
let y = 0
let x = 0
let speed = 0
let level = 0
let speed_list : number[] = []
let button_action = 0
button_action = 0
speed_list = [100, 200, 500, 1000, 1500]
level = 4
speed = speed_list[level]
basic.forever(function on_forever() {
    
    if (button_action != 1) {
        x = randint(0, 4)
        y = randint(0, 4)
        led.plot(x, y)
        basic.pause(speed)
        led.unplot(x, y)
    }
    
})
