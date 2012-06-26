class Player:
    """
    The player, including where he is, and what he's carrying
    (model)
    """
    def __init__(self, name, hunger=8, thirst=8, fatigue=8, injury=8):
        self.name = name

        self.hunger = hunger  # min hunger
        self.thirst = thirst  # min thirst
        self.fatigue = fatigue  # max rest
        self.injury = injury  # max health

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
