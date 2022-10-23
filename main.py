def on_button_pressed_a():
    global level, button_action, speed
    if level == 0:
        level = 5
    basic.clear_screen()
    button_action = 1
    basic.pause(100)
    level += -1
    speed = speed_list[level]
    basic.clear_screen()
    basic.show_string("" + str(level))
    basic.pause(500)
    basic.clear_screen()
    button_action = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global target_counter, x1, y1, x2, y2, x3, y3, button_action
    if target_counter == 3:
        target_counter = 0
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    x3 = 0
    y3 = 0
    basic.clear_screen()
    button_action = 1
    target_counter += 1
    basic.pause(100)
    basic.clear_screen()
    basic.show_string("" + str(target_counter))
    basic.pause(500)
    basic.clear_screen()
    button_action = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global button_action
    basic.clear_screen()
    button_action = 1
    basic.pause(100)
    if x1 == 2 and y1 == 2 or x2 == 2 and y2 == 2 or x3 == 2 and y3 == 2:
        for index in range(1):
            basic.show_leds("""
                . . . . .
                                . . # . .
                                . # . # .
                                . . # . .
                                . . . . .
            """)
            basic.show_leds("""
                . . . . .
                                . . # # .
                                . # . # .
                                . # # . .
                                . . . . .
            """)
            basic.show_leds("""
                . . . . .
                                . # # # .
                                . # . # .
                                . # # . .
                                . . . . .
            """)
            basic.show_leds("""
                . . . . .
                                . # # # .
                                . # . # .
                                . # # # .
                                . . . . .
            """)
            basic.show_leds("""
                # . # . #
                                . # # # .
                                # # . # #
                                . # # # .
                                # . # . #
            """)
            basic.pause(1000)
        for index2 in range(3):
            basic.clear_screen()
            basic.show_icon(IconNames.SMALL_HEART)
            basic.pause(100)
            basic.show_icon(IconNames.HEART)
            basic.pause(100)
    else:
        for index3 in range(1):
            basic.show_leds("""
                . . . . .
                                . . # . .
                                . # . # .
                                . . # . .
                                . . . . .
            """)
            basic.show_leds("""
                . . . . .
                                . . # # .
                                . # . # .
                                . # # . .
                                . . . . .
            """)
            basic.show_leds("""
                . . . . .
                                . # # # .
                                . # . # .
                                . # # . .
                                . . . . .
            """)
            basic.show_leds("""
                . . . . .
                                . # # # .
                                . # . # .
                                . # # # .
                                . . . . .
            """)
            basic.show_leds("""
                # . # . #
                                . # # # .
                                # # . # #
                                . # # # .
                                # . # . #
            """)
            basic.pause(1000)
        for index4 in range(1):
            basic.show_icon(IconNames.NO)
            basic.pause(500)
            basic.clear_screen()
            basic.pause(500)
    basic.clear_screen()
    button_action = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

y3 = 0
x3 = 0
y2 = 0
x2 = 0
y1 = 0
x1 = 0
target_counter = 0
speed = 0
level = 0
speed_list: List[number] = []
button_action = 0
basic.show_string("Press A+B to start")
button_action = 0
speed_list = [100, 200, 500, 1000, 1500]
level = 4
speed = speed_list[level]

def on_forever():
    global x3, y3
    if button_action != 1 and target_counter >= 3:
        x3 = randint(0, 4)
        y3 = randint(0, 4)
        led.plot(x3, y3)
        basic.pause(speed)
        led.unplot(x3, y3)
basic.forever(on_forever)

def on_forever2():
    global x1, y1
    if button_action != 1 and target_counter >= 1:
        x1 = randint(0, 4)
        y1 = randint(0, 4)
        led.plot(x1, y1)
        basic.pause(speed)
        led.unplot(x1, y1)
basic.forever(on_forever2)

def on_forever3():
    global x2, y2
    if button_action != 1 and target_counter >= 2:
        x2 = randint(0, 4)
        y2 = randint(0, 4)
        led.plot(x2, y2)
        basic.pause(speed)
        led.unplot(x2, y2)
basic.forever(on_forever3)
