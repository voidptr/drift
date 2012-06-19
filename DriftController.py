from CommandParser import CommandParser


class DriftController:
    """
    Handle Commands, Manage Encounters
    """
    def __init__(self, debughook, ViewManager, ModelManager):
        self.ViewManager = ViewManager
        self.ModelManager = ModelManager
        self.debughook = debughook

        self.commands = dict()
        self.commands['travel'] = self.travel

    def _get_input(self):
        return self.ViewManager.get_input_string()

    def process_command(self):
        input = self._get_input()

        (command, parameters) = CommandParser.parse_commands(input)

        if not command in self.commands:
            self.ViewManager.provide_command_feedback("I don't understand, %s" % command)
        else:
            if len(parameters) > 0:
                (success, message) = self.commands[command](parameters)
            else:
                (success, message) = self.commands[command]()

            if not success:
                self.ViewManager.provide_command_feedback(message)

    def process_encounter(self):
        self.debughook("PROCESS ENCOUNTER")

    def travel(self, parameters):
        direction = parameters[0]
        self.debughook("TRAVEL! %s" % direction)
        return (True, "")
