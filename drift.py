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
View = DriftViewManager(debug_handle.log, DataModels)

try:
    View.init()

    Controller = DriftController(debug_handle.log, View, DataModels)

    ######## Intro Screens -- TODO move this into the Controller
    View.display_intro_screen()
    selection = ""
    while selection != ord("S") and selection != ord("s") \
            and selection != ord("Q") and selection != ord("q"):  # selection "C" is not yet supported
        selection = View.get_input_ch()

    if selection == ord("Q") or selection == ord("q"):
        View.quit()
        exit(0)
    elif selection == ord("S") or selection == ord("s"):
        View.display_new_character_screen()
        name = View.get_input_string()

        DataModels.create_new_game(name)

        View.display_main_interface()
        View.refresh()

    ######### The Real Deal
    while True:
        ###### YOUR TURN
        ## Process any commands to move things, throw things, buy things,
        ## eat things, drink things, gather things,
        ## do things, look at things, move around, or wait
        Controller.process_command()  # time passes

        ###### THEIR TURN IN THIS PLACE
        ## Initiate encounter checks (are we having a new encounter?)
        ## If so, process any commands issued by the opponent in the encounter
        Controller.process_encounter()

        ## Refresh the window
        View.refresh()  # update status, clear the input window, show
                        # whatever queued up stuff needs showing
                        # grab the input cursor
except:
    View.quit()
    raise
