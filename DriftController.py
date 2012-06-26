from CommandParser import CommandParser
#import Activities


class DriftController:
    """
    Handle Commands, Manage Encounters
    """
    def __init__(self, debughook, ViewManager, ModelManager):
        self.vm = ViewManager
        self.mm = ModelManager
        self.dh = debughook

        self.cp = CommandParser(debughook, ModelManager)

    def _get_input(self):
        return self.vm.get_input_string()

    def process_command(self):
        input = self._get_input()
        self.dh(input)

        (success, error_code, message) = self.cp.parse_commands(input)

        #if not success:
        self.vm.provide_command_feedback(message)

    ## deprecated -- DELETE ME
    def process_command__old(self):
        input = self._get_input()

        (command, parameters) = CommandParser.parse_commands(input)

        if not command in self.commands:
            self.vm.provide_command_feedback("I don't understand, %s" % command)
        else:
            if len(parameters) > 0:
                (success, message) = self.commands[command](parameters)
            else:
                (success, message) = self.commands[command]()

            if not success:
                self.vm.provide_command_feedback(message)

    def process_encounter(self):
        self.dh("PROCESS ENCOUNTER")

    def travel(self, parameters):
        direction = parameters[0]
        self.dh("TRAVEL! %s" % direction)
        return (True, "")
