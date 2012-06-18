class DriftController:
"""
Handle Commands, Manage Encounters
"""
    def __init__(self, ViewManager, ModelManager):
        self.ViewManager = ViewManager
        self.ModelManager = ModelManager

    def process_command(self):
        command = self._get_input()
        first_word = command.split( )[0]

        self.commands[first_word](command)

    def process_attack(self,command):
        command_pieces = command.split()
        ct = len(command_pieces)

#        ## set weapon and target defaults
#        target = self.ModelManager.Encounter.get_opponent()
#        weapon = self.ModelManager.Player.get_equipped_weapon()

        ## defaults
        target = ""
        weapon = ""
        ## parse the command
        if command_pieces[0] == "attack": ## attack [opponent [[with] weapon]]
            if ct > 1:
                target = command_pieces[1]
            if ct > 2: ## possible "with"
                weapon = command_pieces[-1]
        elif command_pieces[0] == "throw": ## throw [weapon [[at] opponent]]
            if ct > 1:
                weapon = command_pieces[1]
            if ct > 2: ## possible "at"
                target = command_pieces[-1]
        elif command_pieces[0] == "shoot": ## could go either way
            
        ## perform the action    
        if target == None

        self.



