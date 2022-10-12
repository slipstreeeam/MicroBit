def on_button_pressed_a():
    global level, button_action, speed
    if level == 0:
        level = 5
    basic.clear_screen()
    button_action = 1
    basic.pause(100)
    level = level - 1
    speed = speed_list[level]
    basic.clear_screen()
    basic.show_string("" + str((level)))
    basic.pause(500)
    basic.clear_screen()
    button_action = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global button_action
    basic.clear_screen()
    button_action = 1
    basic.pause(100)
    if x == 2 and y == 2:
        for index in range(3):
            basic.clear_screen()
            basic.show_icon(IconNames.SMALL_HEART)
            basic.pause(100)
            basic.show_icon(IconNames.HEART)
            basic.pause(100)
    else:
        for index2 in range(1):
            basic.show_icon(IconNames.NO)
            basic.pause(500)
            basic.clear_screen()
            basic.pause(500)
    basic.clear_screen()
    button_action = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

y = 0
x = 0
speed = 0
level = 0
speed_list: List[number] = []
button_action = 0
button_action = 0
speed_list = [100, 200, 500, 1000, 1500]
level = 4
speed = speed_list[level]

def on_forever():
    global x, y
    if button_action != 1:
        x = randint(0, 4)
        y = randint(0, 4)
        led.plot(x, y)
        basic.pause(speed)
        led.unplot(x, y)
basic.forever(on_forever)
