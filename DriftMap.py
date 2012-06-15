class DriftMap:
    """
    Holds and manages the world map
    """
    class Level:
        """
        Individual Levels - stuff that is separated by entrances
        """
        class Area:
            """
            Area Polygons
            """
# TODO Iteration 2
#            class Door:
#                """
#                A generic conduit between levels.
#                """
#                def __init__(self, name, coordinates, direction_of_travel=None, outgoing_level, outgoing_coordinates, description_text)
#                    self.name = name
#                    self.coordinates = coordinates
#                    self.direction_of_travel = direction_of_travel
#                    self.outgoing_level = outgoing_level
#                    self.outgoing_coordinates = outgoing_coordinates

            def __init__(self, name, border_coordinates, traversal_timestep, description_text, view_distance):
                self.name = name
                self.border_coordinates = border_coordinates
                self.traversal_timestep = traversal_timestep
                self.description_text = description_text
                self.view_distance = view_distance
#                self.doors = []  # TODO Iteration 2

        def __init__(self, name, datafile):
            self.name = name
            self.datafile = datafile
            self.areas = []

        def read_level(self):
            fh = open(self.datafile)

            for line in fh:
                line = line.strip()  # strip off the end of line crap
                if len(line) == 0 or line[0] == '#':  # if the line is blank or a comment
                    continue

                line = line.split(",")  # csv

                name = line[0]
#                type = line[1]
# TODO Iteration 2
#                if type == "Door"
#                    coordinates = line[2]
#                    direction_of_travel = line[3]
#                    outgoing_level = line[4]
#                    outgoing_coordinates = line[5]
#                    description_text = line[6]
#
#                    self.areas[-1].doors.append( self.Door( name, coordinates, direction_of_travel, outgoing_level, outgoing_coordinates, description_text ) )
#                else:
                traversal_timestep = line[2]
                description_text = line[3]
                border_coordinates = line[4:]
                self.areas.append(self.Area(name, border_coordinates, traversal_timestep, description_text))

        def which_area(self):
            """
            Identify which Area a character is in
            """
            return []  # TODO http://alienryderflex.com/polygon/
