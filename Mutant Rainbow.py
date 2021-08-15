import random
import turtle as t


def inside_window():
    left_limit = (-t.window_width() / 2) + 100
    right_limit = (t.window_width() / 2) - 100
    top_limit = (t.window_height() / 2) - 100
    bottom_limit = (-t.window_height() / 2) + 100
    (x, y) = t.pos()
    inside = left_limit < x < right_limit and bottom_limit < y < top_limit
    return inside


def set_random_color():
    t.colormode(255)
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    t.pencolor(red, green, blue)


def get_turn_size():
    turn_size = input('Enter turn size (wide, square, narrow):')
    return turn_size


def calculate_turn_angle(turn_size):
    if turn_size == 'wide':
        angle = random.randint(120, 150)
    elif turn_size == 'square':
        angle = random.randint(80, 90)
    else:
        angle = random.randint(20, 40)
    return angle


def move_turtle(line_length, turn_size):
    set_random_color()
    if inside_window():
        angle = calculate_turn_angle(turn_size)
        t.right(angle)
        t.forward(line_length)
    else:
        t.backward(line_length)


def get_line_length():
    choice = input('Enter line length (long, medium, short): ')
    if choice == 'long':
       line_length = 400
    elif choice == 'medium':
        line_length = 300
    else:
        line_length = 200
    return line_length


def get_line_width():
    choice = input('Enter line width (superthick, thick, thin):')
    if choice == 'superthick':
        line_width = 50
    elif choice == 'thick':
        line_width = 30
    else:
         line_width  = 20
    return line_width

######## CODE STARTS HERE ##########


line_length = get_line_length()
line_width = get_line_width()
turn_size = get_turn_size()


t.shape('turtle')
t.fillcolor('purple')
t.bgcolor('blue')
t.speed('fast')

t.pensize(line_width)

while True:
    move_turtle(line_length, turn_size)






