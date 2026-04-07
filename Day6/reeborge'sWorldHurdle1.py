def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    move()
    turn_right()
    move()


def move_up():
    turn_left()
    move()
    turn_right()
    turn_around()


def round():
    move()
    move_up()
    turn_left()


for i in range(4):
    round()
move()
