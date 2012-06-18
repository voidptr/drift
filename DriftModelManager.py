## models
from DriftMap import DriftMap
from Player import Player

class DriftModelManager:
"""
Manages the data models
"""
    def __init__(self, debug_hook):
        self.debug_hook = debug_hook
        self.init = False

    def init(self):
        ## Load Map (model)
        self.levels = [ ('Level1','Level1.dat') ] ## TODO replace this
        self.world_map = DriftMap(levels)

        ## Load Player (model)
        self.player = Player("Yourname",0)

        self.init = True

