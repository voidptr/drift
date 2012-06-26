## models
import DriftMap
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
        self.world_map = DriftMap.DriftWorld("world_map.dat")
        self.player = Player(name)

        self.state = State(current_level=self.world_map.starting_level,
                x=self.world_map.starting_x, y=self.world_map.starting_y)

    def get_player_name(self):
        return self.player.name

    def get_odometer(self):
        return (self.state.odometer, self.state.last_direction)

    def get_clock(self):
        return (self.state.clock.hours(), self.state.clock.minutes_in_hour())

    def get_date(self):
        return self.state.clock.days()

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
        lighting_paradigm = self.world_map.get_lighting_paradigm(
                self.state.current_level,
                self.state.x,
                self.state.y)

        if lighting_paradigm == "outdoors":
            if self.state.clock.section_of_day() != "NIGHT":
                return "DAYLIGHT"
            elif self.state.clock.moon_phase() != "NEW MOON":
                return "MOONLIGHT"
            elif self.state.lamp_on:
                return "LAMPLIGHT"
            elif self.state.fire_on:
                return "FIRELIGHT"
            else:
                return "STARLIGHT"  # todo - danger
        elif lighting_paradigm == "indoor_lit":
            return "LIT"
        else:
            return "DARK"  # todo - danger

    def get_current_displaying_text(self):
        return self.world_map.get_description(
                self.state.current_level,
                self.state.x,
                self.state.y)
