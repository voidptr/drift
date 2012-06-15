"""
Drift: A Fallthru Clone
"""

import curses


def forward_time_step(units):
    """
    Do the things involved with moving forward a time step
    """
    return 0


def handle_input(value):
    """ Handle the keypresses """

    if value == "hi":
        screen.addstr("HELLO TO YOU TOO")
    elif value == "quit":
        quit_program()
    else:
        screen.addstr("WHA?")

    screen.move(WINDOW_HEIGHT - 1, 0)


def setup_screen():
    screen.clear()
    screen.border()  # all the way around

    #screen.move(WINDOW_HEIGHT - 1, 0)


def quit_program():
    curses.endwin()
    exit()

## set up the basic curses stuff
screen = curses.initscr()
curses.curs_set(0)
WINDOW_HEIGHT, WINDOW_WIDTH = screen.getmaxyx()

## draw the border


while True:
    screen.refresh()
    value = screen.getstr()
    handle_input(value)

curses.endwin()
