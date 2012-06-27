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

        if not success:
            self.vm.provide_command_feedback(message)

    def process_encounter(self):
        self.dh("PROCESS ENCOUNTER")
