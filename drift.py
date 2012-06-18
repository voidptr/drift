"""
Drift: A Fallthru Clone
"""
from DebugLog import DebugLog
from DriftModelManager import DriftModelManager
from DriftViewManager import DriftViewManager
from DriftController import DriftController

debug_handle = DebugLog()
debug_handle.init()

DataModels = DriftModelManager(debug_handle.log)
DataModels.init()

View = DriftViewManager(debug_handle.log, DataModels)
View.init()

Controller = DriftController(View, DataModels)

while True:
    ###### YOUR TURN
    ## Process any commands to move things, throw things, buy things, 
    ## eat things, drink things, gather things,
    ## do things, look at things, move around, or wait
    Controller.process_command() ## time passes
    
    ###### THEIR TURN IN THIS PLACE
    ## Initiate encounter checks (are we having a new encounter?)
    ## If so, process any commands issued by the opponent in the encounter
    Controller.process_encounter()

    ## Refresh the window
    View.refresh() ## update status, clear the input window, show 
                   ## whatever queued up stuff needs showing
                   ## grab the input cursor








