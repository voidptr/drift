class State:
    """
    The state of the world around the player
    """

    def __init__(self,
                 minutes=0,
                 encounter=None,
                 odometer=0,
                 last_direction="n",
                 current_level="",
                 x=0,
                 y=0,
                 lamp_on=False,
                 fire_on=False):

        self.clock = self.Clock(minutes)
        self.encounter = encounter
        self.odometer = odometer
        self.last_direction = last_direction

        self.lamp_on = lamp_on
        self.fire_on = fire_on

        self.current_level = current_level
        self.x = x
        self.y = y

    class Clock:
        """
        A simple clock, based on minutes in a day
        """
        def __init__(self, minutes=0):
            self.minutes = minutes

        def days(self):
            return self.hours() / 24

        def hours(self):
            return self.minutes / 60

        def minutes_in_hour(self):
            return self.minutes % 60

        def section_of_day(self):
            if self.minutes < 480:
                return "MORNING"
            elif self.minutes < 960:
                return "AFTERNOON"

            return "NIGHT"

        def moon_phase(self):
            day_of_month = self.days() % 28
            if day_of_month < 7:
                return "NEW MOON"
            elif day_of_month < 14:
                return "WAXING MOON"
            elif day_of_month < 21:
                return "FULL MOON"

            return "WANING MOON"

        def advance(self, minutes):
            self.minutes += minutes
            self.minutes = self.minutes % 1440
