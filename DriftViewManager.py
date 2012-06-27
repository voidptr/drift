import curses
from WindowPref import WindowPref


class DriftViewManager:
    """
    Manage the View
    """

    def __init__(self, debug_hook, DataModels):
        self.debug_hook = debug_hook
        self.DataModels = DataModels
        self.is_init = False

    def init(self):
#        assert(self.init == False)

        ## window init
        self.stdscr = curses.initscr()
        bottom, right = self.stdscr.getmaxyx()
        self._bottom = bottom
        self._right = right

        self.whole_window = WindowPref(left=0,
                                       right=right,
                                       top=0,
                                       bottom=bottom,
                                       windowname="whole_window",
                                       debughook=self.debug_hook,
                                       mainwindow=self.stdscr)
        self.whole_window.init()
        self.is_init = True

    def display_intro_screen(self):
        self.whole_window.clear()

        self.whole_window.draw_text_centered("DRIFT", top=3)
        self.whole_window.draw_text_centered("A Text-based Adventure Game", top=4)
        self.whole_window.draw_text_centered("Version 0.1  2012", top=5)
        self.whole_window.draw_text_centered("(C) 2012 Rosangela Canino-Koning - Licensed under GPL", top=6)

        self.whole_window.draw_text_centered("Continue existing game?(C)  Start new game?(S)  Quit?(Q)", top=10)
        self.whole_window.draw_text_centered("Press C, S, or Q", top=12)

    def display_new_character_screen(self):
        self.whole_window.clear()

        self.whole_window.draw_text("Enter name of participant")
        self.whole_window.grab_cursor(top=1)

    def get_input_string(self):
        return self.stdscr.getstr()

    def get_input_ch(self):
        return self.stdscr.getch()

    def quit(self):
        curses.echo()
        curses.endwin()

    def display_main_interface(self):
        self.whole_window.clear()
        self.status_bar = WindowPref(left=self.whole_window.pos.left,
                                     right=self.whole_window.pos.right,
                                     top=self.whole_window.pos.top,
                                     bottom=self.whole_window.pos.top + 1,
                                     windowname="status_bar",
                                     debughook=self.debug_hook,
                                     mainwindow=self.stdscr)

        self.input_box = WindowPref(left=self.whole_window.pos.left,
                                    right=self.whole_window.pos.right,
                                    top=self.status_bar.pos.bottom,
                                    bottom=self.status_bar.pos.bottom + 2,
                                    windowname="input_box",
                                    debughook=self.debug_hook,
                                    mainwindow=self.stdscr)

        self.stats_box = WindowPref(left=self.whole_window.pos.left,
                                    right=self.whole_window.pos.right,
                                    top=self.input_box.pos.bottom,
                                    bottom=self.input_box.pos.bottom + 5,
                                    windowname="stats_box",
                                    debughook=self.debug_hook,
                                    mainwindow=self.stdscr)

        self.command_feedback_bar = WindowPref(left=self.whole_window.pos.left,
                                      right=self.whole_window.pos.right,
                                      top=self.stats_box.pos.bottom,
                                      bottom=self.stats_box.pos.bottom + 1,
                                      windowname="command_feedback_bar",
                                      debughook=self.debug_hook,
                                      mainwindow=self.stdscr)

        self.main_window = WindowPref(left=self.whole_window.pos.left,
                                      right=self.whole_window.pos.right,
                                      top=self.command_feedback_bar.pos.bottom,
                                      bottom=self.whole_window.pos.bottom,
                                      windowname="main_window",
                                      debughook=self.debug_hook,
                                      mainwindow=self.stdscr)

        self.status_bar.init()
        self.input_box.init()
        self.stats_box.init()
        self.command_feedback_bar.init()
        self.main_window.init()

        self.input_box.grab_cursor()

    def refresh(self):
        self.refresh_status_bar()
        self.refresh_stats_box()
        self.refresh_main_window()
        self.refresh_command_feedback_bar()
        self.refresh_input_box()

    def refresh_status_bar(self):
        name = self.DataModels.get_player_name()  # Duh, my name
        od = self.DataModels.get_odometer()  # How many miles traveled in current direction
        lighting = self.DataModels.get_lighting_condition()  # Daylight, Moonlight, Starlight, Dark, Lighted
        clock = self.DataModels.get_clock()  # What the time is of the day, in Hours and Minutes
        date = self.DataModels.get_date()  # Just the day count
        day_section = self.DataModels.get_section_of_day()  # MORNING, AFTERNOON, NIGHT

        self.status_bar.draw_text("%s:" % name, left=0)
        self.status_bar.draw_text("OD %s%s" % (od[0], od[1]), left=27)
        self.status_bar.draw_text(lighting, left=39)
        self.status_bar.draw_text("%s:%02d" % (clock[0], clock[1]), left=50)
        self.status_bar.draw_text("DAY %s: %s" % (date, day_section), left=59)

    def refresh_stats_box(self):
        self.stats_box.clear()
        hunger = self.DataModels.get_player_hunger()
        thirst = self.DataModels.get_player_thirst()
        fatigue = self.DataModels.get_player_fatigue()
        injury = self.DataModels.get_player_injury()

        self.stats_box.draw_text("STATUS:")
        self.stats_box.draw_text("hunger:  %s" % hunger, top=1)
        self.stats_box.draw_text("thirst:  %s" % thirst, top=2)
        self.stats_box.draw_text("fatigue: %s" % fatigue, top=3)
        self.stats_box.draw_text("injury:  %s" % injury, top=4)

    def refresh_command_feedback_bar(self):
        self.command_feedback_bar.clear()

        ## TODO - add multipage capability

    def provide_command_feedback(self, message):
        """
        A self-contained routine to give you feedback on a wrong command
        """
        self.refresh()  # reset the display

        self.command_feedback_bar.draw_text(message)
        self.input_box.clear()
        self.input_box.draw_text("PRESS (C) to CONTINUE")
        selection = ""
        while selection != ord("C") and selection != ord("c"):
            selection = self.get_input_ch()

        self.refresh()  # reset it again

    def refresh_main_window(self):
        self.main_window.clear()
        current_text = self.DataModels.get_current_displaying_text()

        gps = "  gps:%s,%s" % (self.DataModels.state.x, self.DataModels.state.y)

        land_info = ""
        for land in self.DataModels.world_map.levels["root"].Lands:
            land_info += str(self.DataModels.world_map.levels["root"].Lands[land])

        land_locations = " lands:" + land_info

        self.main_window.draw_text(current_text + gps + land_locations)
        ## TODO - add multipage capability

    def refresh_input_box(self):
        self.input_box.clear()
        self.input_box.grab_cursor()
