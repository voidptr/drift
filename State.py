class State:
    """
    The state of the world around the player
    """
    class Clock:
        """
        A simple clock, based on minutes in a day
        """
        def __init__(self):
            self.minutes = 0

        def hours(self):
            return self.minutes / 60

        def minutes_in_hour(self):
            return self.minutes % 60

        def section_of_day(self):
            if self.minutes < 480:
                return "NIGHT"
            elif self.minutes < 960:
                return "MORNING"

            return "AFTERNOON"

        def advance(self, minutes):
            self.minutes += minutes
            self.minutes = self.minutes % 1440

    def __init__(self):  # for the new game! -- TODO - fix so that this can be informed by the map's default state
        self.date = 0
        self.clock = self.Clock()
        self.encounter = None
        self.odometer = 0
        self.last_direction = "n"  # default to north. (because we came from the south :)
        self.current_text = "You are in a place. There's nothing around."  # todo, fix this
        self.lighting = "DAYLIGHT"
