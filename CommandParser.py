class Command:
"""
The structure of the commands
"""

    def __init__(self, verb, subject=None, source=None, target=None, count=None):
        self.verb = verb
        self.subject = subject
        self.source = source
        self.target = target
        self.count = count

class CommandParser:
"""
Parses commands into "verb" "subject" "source" "target" and "count"
"""
    verbs = dict()

    ## command_subject - take knife
    verbs['take'] = parse_command_subject
    verbs['tk'] = parse_command_subject

    verbs['climb'] = parse_command_subject
    verbs['light'] = parse_command_subject

    ## command_subject_count - gather [rocks [20]]
    verbs['gather'] = parse_command_subject_count
    verbs['buy'] = parse_command_subject_count
    verbs['sell'] = parse_command_subject_count

    ## command - hunt
    verbs['hunt'] = parse_command
    verbs['hello'] = parse_command



    ## command_count -- eat [5]
    verbs['eat'] = parse_command_count 
    verbs['t'] = parse_command_count
    verbs['dig'] = parse_command_count
    verbs['rest'] = parse_command_count
    verbs['wait'] = parse_command_count
    verbs['z'] = parse_command_count
    verbs['n'] = parse_command_count
    verbs['s'] = parse_command_count
    verbs['e'] = parse_command_count
    verbs['w'] = parse_command_count
    verbs['nw'] = parse_command_count
    verbs['sw'] = parse_command_count
    verbs['ne'] = parse_command_count
    verbs['se'] = parse_command_count
    verbs['u'] = parse_command_count
    verbs['d'] = parse_command_count
    verbs['north'] = parse_command_count
    verbs['south'] = parse_command_count
    verbs['east'] = parse_command_count
    verbs['west'] = parse_command_count
    verbs['northwest'] = parse_command_count
    verbs['southwest'] = parse_command_count
    verbs['northeast'] = parse_command_count
    verbs['southeast'] = parse_command_count
    verbs['up'] = parse_command_count
    verbs['down'] = parse_command_count

    ## command_source - look [[in] S01]
    verbs['look'] = parse_command_source
    verbs['i'] = parse_command_source

    ## command_source_count - drink [from C01 [2]]
    verbs['drink'] = parse_command_source_count
    verbs['k'] = parse_command_source_count

    ## command_subject_target - throw [Knife [[at] IYO]]
    verbs['throw'] = parse_command_subject_target

    ## command_target_subject - attack [IYO [[with] Knife]]
    verbs['attack'] = parse_command_subject_target
    verbs['fight'] = parse_command_subject_target
    verbs['stab'] = parse_command_subject_target

    ## ambiguous - depends on usage of with at and whether target or weapon
    ## is named first :/ -- WILL HAVE TO SEE HOW THE GAME DOES IT :(
    verbs['shoot'] = parse_command_with_at
 

    ## DON'T REMEMBER HOW IT GOES :( ???
    ## command_source_target_subject_count ???
    verbs['move'] = parse_command_source_target_subject_count
    verbs['mv'] = parse_command_source_target_subject_count
       

    def parse(command):
        command_pieces = command.split( )

        verb = command_pieces[0]

        return verbs[verb](command_pieces)

    def parse_command_subject(command_pieces):
        verb = command_pieces[0]
        subject = None
        if len(command_pieces) > 1:
            subject = command_pieces[1]

        return Command(verb, subject)
        
    def parse_command_subject_count(command_pieces):
        verb = command_pieces[0]
        subject = None
        count = None
        if len(command_pieces) > 1:
            subject = command_pieces[1]
        if len(command_pieces) > 2:
            count = command_pieces[2]

        return Command(verb, subject, count=count)

   
    

