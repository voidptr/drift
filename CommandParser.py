import Activities


class CommandParser:
    def __init__(self, debughook, ModelManager):

        self.dh = debughook
        self.mm = ModelManager

        self.activities = self.register_activities()

    def register_activities(self):
        activities = []
        activities.append(Activities.Travel(self.mm, self.dh))
        activities.append(Activities.RepeatTravel(self.mm, self.dh))
        activities.append(Activities.ReverseTravel(self.mm, self.dh))
        activities.append(Activities.EnterLocation(self.mm, self.dh))
        activities.append(Activities.TakeStuff(self.mm, self.dh))
        activities.append(Activities.DropStuff(self.mm, self.dh))
        activities.append(Activities.MoveStuff(self.mm, self.dh))

        return activities

    def parse_commands(self, input):
        for activity in self.activities:
            (success, error_code, message) = activity.try_match(input)
            if success:
                return (success, error_code, message)
            elif error_code == 1:  # if there was a genuine error, then stop trying and return it.
                return (success, error_code, message)
        return (False, 2, "I don't understand, %s" % input)


## deprecated -- DELETE ME
class CommandParser__old:

    quantifiers = ["lbs", "lb", "oz", "qt", "pint", "stick", "stk"]
    identifiers = ["c%02d" % num for num in range(100)] + \
            ["s%02d" % num for num in range(100)] + \
            ["p%02d" % num for num in range(100)] + \
            ["b%02d" % num for num in range(100)] + \
            ["pecos", "cactus", "scrub", "ipecac", "tailwind", "snort"] + \
            ["drifter", "vagrant"]

    generic_containers = ["pack", "backpack", "sack", "burro", "boat", "canteen", "bottle", "lamp"]

    infoable_nouns = ["oasis", "slavhos", "cove", "dome"]

    accessories = ["cape", "coat", "navaid", "brz ring", "sil ring", "gld ring", "talisman",
                   "flyr", "brz amulet", "sil amulet", "gld amulet", "lamp"]

    encounter_targets = ["devi", "squir", "berven", "griven", "demon", "renegade", "squal", "rabir", "wolven"]

    addressable_nouns = ["wood", "food", "ruby", "rock", "salve", "rall", "em",
                         "arrow", "sand", "water", "oil", "grain", "armor", "axe",
                         "blanket", "sil amulet", "cape", "coat", "stone ikon", "gld key", "diamond",
                         "emerald", "brz amulet", "kalard", "gld amulet", "knife", "melon", "mace",
                         "pamphlet", "navaid", "talisman", "gld ring", "wherstone", "locatrix", "shovel",
                         "spear", "sword", "sil ring", "brz ring", "flyr", "weyring", "brz ikon",
                         "sil key", "brz key", "sil ikon", "gld ikon", "scimitar", "hide", "bow",
                         "flint", "pecos", "cactus", "scrub", "ipecac", "tailwind", "snort",
                         "drifter", "vagrant", "burro", "sack", "canteen", "lamp", "pack",
                         "bottle"]

    verbs = ["yes", "cut", "dig", "eat", "ent", "put", "run", "back",
             "bend", "down", "drop", "east", "fill", "give", "hunt", "info",
             "kill", "look", "move", "open", "pick", "quit", "rest", "read",
             "save", "sell", "take", "turn", "west", "agree", "apply", "attack",
             "break", "climb", "collect", "drink", "empty", "enter", "extinguish", "fight",
             "forward", "gather", "hello", "inventory", "light", "level", "north", "northeast",
             "northwest", "order", "prepare", "render", "repeat", "load", "shoot", "sling", "south",
             "southeast", "southwest", "steal", "strike", "surrender", "throw", "trade",
             "twist", "untie", "yield"]

    #connectives = ["the"

    numbers = [str(val) for val in range(11)] + ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

    compound_starters = ["stone", "sil", "silver", "gld", "gold", "brz", "bronze"]

    @staticmethod
    def is_num(val):
        try:
            int(val)
        except:
            return False
        return True

    @staticmethod
    def is_quantifier(val):
        return val in CommandParser.quantifiers

    @staticmethod
    def is_object(val):
        return (val in CommandParser.addressable_nouns or val in CommandParser.compound_starters)

    @staticmethod
    def is_identifier(val):
        return val in CommandParser.identifiers

    @staticmethod
    def is_compound(val):
        return val in CommandParser.compound_starters

    @staticmethod
    def is_verb(val):
        return val in CommandParser.verbs

    @staticmethod
    def extract_object_tokens(reversed_token_list):
        objects = []
        try:
            while True:  # the rest of the items
                token = reversed_token_list.pop()
                if token == "all":
                    objects.append(("all", 0))
                elif CommandParser.is_num(token):
                    count = float(token)
                    obj = reversed_token_list.pop()
                    if CommandParser.is_quantifier(obj):
                        obj = reversed_token_list.pop()  # drop the old quantifier
                        if CommandParser.is_compound(obj):
                            obj = "%s %s" % (obj, reversed_token_list.pop())
                    objects.append((obj, count))
                elif CommandParser.is_object(token) or CommandParser.is_identifier(token):
                    if CommandParser.is_compound(token):
                        token = "%s %s" % (token, reversed_token_list.pop())

                    objects.append((token, 1))
        except:
            return None
        return objects

    @staticmethod
    def parse_commands(input):
        """
        This has to be the stupidest possible way to do this. :(
        """

        input = input.lower()
        input_tokens = input.split()
        input_tokens.reverse()  # for faster popping

        command = input_tokens.pop()  # the root command
        if not CommandParser.is_verb(command):
            return ("command", ())

        ## directional commands
        if command == "n" or command == "north" or command == "s" or command == "south" or \
           command == "e" or command == "east" or command == "w" or command == "west" or \
           command == "ne" or command == "northeast" or command == "se" or command == "southeast" or \
           command == "nw" or command == "northwest" or command == "sw" or command == "southwest" or \
           command == "u" or command == "up" or command == "d" or command == "down":
            print "hai"
            return ("travel", (command))
        elif command == "f" or command == "forward":
            print "hei"
            return ("travel_repeat", (1))
        elif command == "f" or command == "forward":
            print "hei"
            return ("travel_repeat", (10))
        elif command == "b" or command == "back":
            print "hei"
            return ("travel_backward", ())
        elif command == "ent" or command == "enter":
            print "hei"
            return ("enter", ())

        ## material handling commands
        elif command == "tk" or command == "take" or command == "pick":
            if command == "pick" and input_tokens[-1] == "up":
                input_tokens.pop()  # pop the superfluous
            objects = CommandParser.extract_object_tokens(input_tokens)
            source = "here"
            target = "hand"
            return ("move", (source, target, objects))
        elif command == "drop" or command == "dp" or command == "put" or command == "lay":
            if (command == "put" or command == "lay") and input_tokens[-1] == "down":
                input_tokens.pop()  # pop the superfluous
            objects = CommandParser.extract_object_tokens(input_tokens)
            return ("move", (source, target, objects))
        elif command == "move" or command == "mv":
            input_tokens.pop()  # drop the "from"
            source = input_tokens.pop()
            input_tokens.pop()  # drop the "to"
            target = input_tokens.pop()
            objects = CommandParser.extract_object_tokens(input_tokens)
            return ("move", (source, target, objects))
        elif command == "fill":
            target = input_tokens.pop()
            if len(input_tokens) > 0 and input_tokens[-1] == "with":
                input_tokens.pop()

            substance = "water"
            if len(input_tokens > 0):
                substance = input_tokens.pop()
            return ("fill", (target, substance))
        elif command == "empty":
            target = input_tokens.pop()
            return ("empty", (target))
        elif command == "gather" or command == "collect":
            objects = CommandParser.extract_object_tokens(input_tokens)
            return ("gather", (input_tokens))

        ## attack commands
        elif command == "sh" or command == "shoot":
            target = ""
            if len(input_tokens) > 0:
                target = input_tokens[0]
            return ("shoot", (target))  # always an arrow
        elif command == "sling":
            target = ""
            if len(input_tokens) > 0:
                target = input_tokens[0]
            return ("sling", (target))  # always a rock
        elif command == "throw":
            subject = input_tokens.pop()
            target = ""
            if len(input_tokens) > 0:
                target = input_tokens[0]
            return ("throw", (subject, target))  # throw some arbitrary thing)
        elif command == "fight" or command == "attack" or command == "kill":
            print "hoi"
            return ("fight", ())
        elif command == "steal":
            print "huia"
            return ("steal", ())
        elif command == "yield" or command == "surrender":
            print "hui"
            return ("yield", ())
        elif command == "agree" or command == "yes":
            print "hyi"
            return ("agree_to_pay", ())
        elif command == "run" or command == "retreat":
            print "hii"
            return ("run", ())

        ## commerce
        elif command == "buy":
            objects = CommandParser.extract_object_tokens(input_tokens)
            return ("buy", (objects))
        elif command == "sell":
            objects = CommandParser.extract_object_tokens(input_tokens)
            return ("sell", (objects))
        elif command == "trade":
            objects = CommandParser.extract_object_tokens(input_tokens)
            return ("trade", (objects))

        ## info
        elif command == "info":
            subject = input_tokens.pop()
            return ("info", (subject))
        elif command == "i" or command == "inventory":
            print "hii"
            return ("inventory", ("hand", ()))
        elif command == "read":
            subject = input_tokens.pop()
            return ("read", (subject))
        elif command == "look":
            specific = input_tokens.pop()
            subject = input_tokens.pop()
            if specific == "at":
                print "hii"
                return ("read", (subject))
            elif specific == "in" or specific == "on":
                print "hii"
                return ("inventory", (subject))
            elif specific == "here":
                print "hii"
                return ("look_around", ())
        elif command == "hi" or command == "hello":
            print "hei"
            return ("hello", ())

        ## miscellaneous
        elif command == "t" or command == "eat":
            count = 1
            if len(input_tokens) > 1:
                count = input_tokens.pop()
            return ("eat", (count))
        elif command == "k" or command == "drink":
            count = 1
            if len(input_tokens) > 1:
                count = input_tokens.pop()
            return ("drink", (count))
        elif command == "z" or command == "rest":
            count = 1
            if len(input_tokens) > 1:
                count = input_tokens.pop()
            return ("rest", (count))
        elif command == "h" or command == "hunt":
            print "hei"
            return ("hunt", ())
        elif command == "dig":
            print "hei"
            return ("dig", ())
        elif command == "skin" or command == "prepare":
            count = 1
            if len(input_tokens) > 1:
                count = input_tokens.pop()
            target = ""
            if len(input_tokens) > 1:
                target = input_tokens.pop()
            return ("skin", (count, target))
        elif command == "l" or command == "light":
            target = ""
            if len(input_tokens) > 1:
                target = input_tokens.pop()
            return ("light", (target))
        elif command == "x" or command == "extinguish":
            target = ""
            if len(input_tokens) > 1:
                target = input_tokens.pop()
            return ("extinguish", (target))
        elif command == "apply":
            print "hei"
            return ("apply_salve", ())
        elif command == "order":
            specific = input_tokens.pop()
            if specific == "meal":
                print "hii"
                return ("order_meal", ())
            elif specific == "food":
                print "hii"
                return ("buy", ("food", 1))
            elif CommandParser.is_num(specific):
                print "hii"
                return ("buy", ("food", specific))
        elif command == "where":
            subject = input_tokens[-1]
            return ("weyring", (subject))
        elif command == "level":
            print "hei"
            return ("level", ())
        elif command == "unlock" or command == "open" or command == "turn" or command == "cut":
            target = ""
            if len(input_tokens) > 1:
                target = input_tokens.pop()
            return ("open", (target))

        ## charity
        elif command == "give":
            count = 1
            currency = input_tokens[0]
            if len(input_tokens) > 2:
                count = input_tokens.pop()
            return ("charity", (count, currency))

        ## game shit
        elif command == "reset":
            print "hei"
            return ("reset_odometer", ())
        elif command == "help":
            print "hei"
            return ("show_help", ())
        elif command == "save":
            print "hei"
            return ("save_game", ())
        elif command == "load":
            print "hei"
            return ("load_game", ())
        elif command == "quit":
            print "hei"
            return ("quit", ())
        else:
            return (command, ())
