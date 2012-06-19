## models
from DriftMap import DriftMap
from Player import Player
from State import State


class DriftModelManager:
    """
    Manages the data models
    """
    def __init__(self, debug_hook):
        self.debug_hook = debug_hook
        self.init = False

        self.player = None
        self.levels = None
        self.world_map = None

        self.state = None

    def create_new_game(self, name):
        self.player = Player(name, 0)

        self.levels = [('Level1', 'Level1.dat')]  # TODO replace this
        self.world_map = DriftMap(self.levels)

        self.state = State()  # TODO - fix to inform the initial state with whatever the proper initial state of the game is

    def get_player_name(self):
        return self.player.name

    def get_odometer(self):
        return (self.state.odometer, self.state.last_direction)

    def get_lighting(self):
        return self.state.lighting

    def get_clock(self):
        return (self.state.clock.hours(), self.state.clock.minutes_in_hour())

    def get_date(self):
        return self.state.date

    def get_section_of_day(self):
        return self.state.clock.section_of_day()

    def get_player_hunger(self):
        return self.player.hunger

    def get_player_thirst(self):
        return self.player.thirst

    def get_player_fatigue(self):
        return self.player.fatigue

    def get_player_injury(self):
        return self.player.injury

    def get_lighting_condition(self):
        return self.state.lighting

    def get_current_displaying_text(self):
        return self.state.current_text
