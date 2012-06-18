import curses
from WindowPref import WindowPref

class ViewManager:
"""
Manage the View
"""
    def __init__(self, debug_hook):
        self.debug_hook = debug_hook
        self.init = False
        
    def init(self):
#        assert(self.init == False)

        ## window init
        self.stdscr = curses.initscr()
        __bottom, __right = stdscr.getmaxyx()

        self.whole_window = WindowPref(left=0, right=__right, top=0, bottom=__bottom,
                          debughook=debug_handle.log)
        self.status_bar = WindowPref(left=whole_window.pos.left, right=whole_window.pos.right,
                          top=whole_window.pos.top, bottom=whole_window.pos.top + 1,
                          windowname="status_bar", debughook=debug_handle.log,
                          mainwindow=stdscr)
        self.input_box = WindowPref(left=whole_window.pos.left, right=whole_window.pos.right,
                          top=whole_window.pos.bottom - 3, bottom=whole_window.pos.bottom,
                          has_border=True, windowname="input_box",
                          debughook=debug_handle.log, mainwindow=stdscr)
        self.main_window = WindowPref(left=whole_window.pos.left, right=whole_window.pos.right,
                          top=status_bar.pos.bottom, bottom=input_box.pos.top,
                          has_border=True, windowname="main_window",
                          debughook=debug_handle.log, mainwindow=stdscr)
        self.main_window.init()
        self.input_box.init()
        self.status_bar.init()
        self.input_box.grab_cursor()

        self.init = True

    def get_input(self):
        return self.stdscr.getstr()

