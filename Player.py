class Player:
    """
    The player, including where he is, and what he's carrying
    (model)
    """
    def __init__(self, name, starting_level):
        self.name = name

        self.hunger = 8  # min hunger
        self.thirst = 8  # min thirst
        self.fatigue = 8  # max rest
        self.injury = 8  # max health

#       self.time = 0 ## starting time
        self.x = 0  # x-coordinate
        self.y = 0  # y-coordinate
        self.world_level = starting_level

#       self.fighting_xp = 0 ## noob
#       self.knife_xp = 0
#       self.spear_xp = 0
#       self.sword_xp = 0
#       self.axe_xp = 0
#       self.bow_xp = 0

#       self.inventory = Container("Inventory")

#class Container:
#"""
#Generic containers, like bags or canteens.
#(model)
#"""
#    def __init__(self, name, weightlimit=0, type="solid")
#        self.name = name
#        self.weightlimit = weightlimit
#        self.type = type
#        self.content = []
