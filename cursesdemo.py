######################
# Python Curses Demo
# And window wrapper
######################

import curses
from optparse import OptionParser

from WindowPref import WindowPref
from DebugLog import DebugLog

# Set up options
usage = """usage: %prog [options]
"""
parser = OptionParser(usage)
parser.add_option("-d", "--debug_messages", action="store_true", dest="debug_messages",
                  default=False, help="print debug messages to stdout")

## fetch the args
(options, args) = parser.parse_args()

debug_handle = DebugLog()
debug_handle.init()


def init_colors():
    curses.start_color()
    curses.use_default_colors()

    colorlist = (("red", curses.COLOR_RED),
                 ("green", curses.COLOR_GREEN),
                 ("yellow", curses.COLOR_YELLOW),
                 ("blue", curses.COLOR_BLUE),
                 ("cyan", curses.COLOR_CYAN),
                 ("magenta", curses.COLOR_MAGENTA),
                 ("black", curses.COLOR_BLACK),
                 ("white", curses.COLOR_WHITE))
    colors = {}
    colorpairs = 0
    for name, i in colorlist:
        colorpairs += 1
        curses.init_pair(colorpairs, i, -1)
        colors[name] = curses.color_pair(i)

    return colors


def handle_input(value):
    """ Handle the keypresses """

    input_box.clear()

    if value == "hi":
        status_bar.draw_text("HELLO TO YOU TOO")
    elif value == "quit":
        curses.echo()
        curses.endwin()
        exit()
    else:
        status_bar.draw_text("WHA?")

stdscr = curses.initscr()
colors = init_colors()

__bottom, __right = stdscr.getmaxyx()

## windows
whole_window = WindowPref(left=0,
                          right=__right,
                          top=0,
                          bottom=__bottom,
                          debughook=debug_handle.log)
status_bar = WindowPref(left=whole_window.pos.left,
                          right=whole_window.pos.right,
                          top=whole_window.pos.top,
                          bottom=whole_window.pos.top + 1,
                          windowname="status_bar",
                          debughook=debug_handle.log,
                          mainwindow=stdscr)
input_box = WindowPref(left=whole_window.pos.left,
                          right=whole_window.pos.right,
                          top=whole_window.pos.bottom - 3,
                          bottom=whole_window.pos.bottom,
                          has_border=True,
                          windowname="input_box",
                          debughook=debug_handle.log,
                          mainwindow=stdscr)
main_window = WindowPref(left=whole_window.pos.left,
                          right=whole_window.pos.right,
                          top=status_bar.pos.bottom,
                          bottom=input_box.pos.top,
                          has_border=True,
                          windowname="main_window",
                          debughook=debug_handle.log,
                          mainwindow=stdscr)

main_window.init()
input_box.init()
status_bar.init()

#main_window.draw_text("Main Window!")
status_bar.draw_text("Status Bar!")
input_box.grab_cursor()

while True:
    stdscr.refresh()
    value = stdscr.getstr()
    handle_input(value)
    input_box.grab_cursor()

curses.endwin()
