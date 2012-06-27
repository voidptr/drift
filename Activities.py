import re


class Activity(object):
    def __init__(self, ModelManager, debughook):
        self.mm = ModelManager
        self.dh = debughook

    def try_match(self, input):
        self.dh("try_match: %s" % input)
        input = input.strip()
        for regexp_object in self.regexps:
            result = regexp_object.match(input)
            if result:
                params = result.groupdict()
                return self.activity_function(params)
        return (False, 2, "No Match")

    def prepare_command_string_parser(self):
        self.regexps = []
        self.dh(self)
        for regexp in self.regexp_strings:
            self.regexps.append(re.compile(regexp))


class Travel(Activity):
    def __init__(self, ModelManager, debughook):
        super(Travel, self).__init__(ModelManager, debughook)

        self.regexp_strings = ["(?P<direction>northeast|northwest|southeast|southwest|north|south|east|west|up|down|ne|nw|se|sw|n|s|e|w|u|d)$"]
        self.prepare_command_string_parser()

        self.directions = {
                "north": "n",
                "n": "n",
                "south": "s",
                "s": "s",
                "east": "e",
                "e": "e",
                "west": "w",
                "w": "w",
                "northeast": "ne",
                "ne": "ne",
                "northwest": "nw",
                "nw": "nw",
                "southeast": "se",
                "se": "se",
                "southwest": "sw",
                "sw": "sw"}

    def activity_function(self, parameters):
        direction = self.directions[parameters["direction"]]

        (x, y) = self.mm.get_coordinates(self.mm.state.x, self.mm.state.y, direction)

        if self.mm.is_travelable(x, y):
            if direction == "n" or direction == "s" or direction == "e" or direction == "w":
                distance = 1
            else:
                distance = 1.4

            self.mm.state.clock.advance(self.mm.get_travel_time() * distance)
            if direction != self.mm.state.last_direction:
                self.mm.state.odometer = distance
            else:
                self.mm.state.odometer += distance
            self.mm.state.last_direction = direction

            self.mm.state.x = x
            self.mm.state.y = y

            return (True, None, "")
        else:
            return (False, None, "Can't travel in that direction.")

        #return(True, None, "TRAVELING: %s" % direction)


class RepeatTravel(Activity):
    def __init__(self, ModelManager, debughook):
        super(RepeatTravel, self).__init__(ModelManager, debughook)

        self.regexp_strings = ["(?P<command>forward|f) (?P<count>\d*)$",
                               "(?P<command>forward|f)$"]
        self.prepare_command_string_parser()

    def activity_function(self, parameters):
        count = 1  # default
        if "count" in parameters:
            count = parameters["count"]
        return(True, None, "Repeat Traveling! %s -- %s" % (count, parameters))


class ReverseTravel(Activity):
    def __init__(self, ModelManager, debughook):
        super(ReverseTravel, self).__init__(ModelManager, debughook)

        self.regexp_strings = ["back|b$"]
        self.prepare_command_string_parser()

    def activity_function(self, parameters):
        return (True, None, "Reverse Traveling!")


class EnterLocation(Activity):
    def __init__(self, ModelManager, debughook):
        super(EnterLocation, self).__init__(ModelManager, debughook)

        self.regexp_strings = ["enter|ent$"]
        self.prepare_command_string_parser()

    def activity_function(self, parameters):
        return (True, None, "Enter a Location!")


class ObjectMovement(Activity):
    def __init__(self, ModelManager, debughook):
        super(ObjectMovement, self).__init__(ModelManager, debughook)

    def activity_function(self, parameters):
        stuff = parameters["stuff"]
        if "target" in parameters:
            self.target = parameters["target"]
        if "source" in parameters:
            self.source = parameters["source"]
        return(True, None, "Object Movement! from %s to %s. stuff:%s -- params:%s" % (self.source, self.target, stuff, parameters))


class TakeStuff(ObjectMovement):
    def __init__(self, ModelManager, debughook):
        super(TakeStuff, self).__init__(ModelManager, debughook)

        self.target = "hand"
        self.source = "here"
        self.regexp_strings = ["(?P<command>take|tk|pick up) (?P<stuff>all)",
                               "(?P<command>take|tk|pick up) (?P<stuff>(.*?))$"]
        self.prepare_command_string_parser()


class DropStuff(ObjectMovement):
    def __init__(self, ModelManager, debughook):
        super(DropStuff, self).__init__(ModelManager, debughook)

        self.target = "here"
        self.source = "hand"
        self.regexp_strings = ["(?P<command>drop|lay down|lay|put down|put|dp) (?P<stuff>all)",
                               "(?P<command>drop|lay down|lay|put down|put|dp) (?P<stuff>(.*?))$"]
        self.prepare_command_string_parser()


class MoveStuff(ObjectMovement):
    def __init__(self, ModelManager, debughook):
        super(MoveStuff, self).__init__(ModelManager, debughook)

        self.regexp_strings = ["(?P<command>move|mv) (from|fr) (?P<source>.+?) (to) (?P<target>.+?) (?P<stuff>(.*?))$"]
        self.prepare_command_string_parser()
