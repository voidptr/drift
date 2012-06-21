class FeatureTypes:
    """
    The types of features one may encounter on the map
    """
    def __init__(self, id, description, activities)
        self.id = id
        self.description = description
        self.activities = activities  # keywords that will trigger certain behaviors

    @staticmethod
    def feature_type_builder(file):
        features = []
        fh = open(file)
        for line in fh:
            line = line.strip()
            if len(line) == 0 or line[0] == "#":
                continue

            line = line.split()
            features.append(FeatureTypes(line[0], line[1], line[2:]))
        fh.close()
        return features

class LandTypes:
    """
    The types of landscapes available
    """

class DriftMap:
    """
    Holds and manages the world map
    (model) - static, for the most part... that is unless you've dug a hole or something.
    """
    class Level:
        """
        Individual Levels - stuff that is separated by entrances
        """
        class Area:
            """
            Area Squares
            """
            def __init__(self, name, border_coordinates, traversal_timestep, description_text, view_distance):
                self.border_coordinates = border_coordinates

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
                traversal_timestep = line[2]
                description_text = line[3]
                border_coordinates = line[4:]
                self.areas.append(self.Area(name, border_coordinates, traversal_timestep, description_text))

        def which_area(self):
            """
            Identify which Area a character is in
            """
            return []  # TODO http://alienryderflex.com/polygon/
    def __init__(self, level_files):
        self.levels = {}
        for (name, file) in level_files:
            self.levels[name] = DriftMap.Level(name, file)


