class FeatureType:
    """
    The types of features one may encounter on the map
    """
    def __init__(self, id, description, activities):
        self.id = id
        self.description = description
        self.activities = activities  # keywords that will trigger certain behaviors

    @staticmethod
    def feature_types_builder(file):
        feature_types = {}
        fh = open(file)
        for line in fh:
            line = line.strip()
            if len(line) == 0 or line[0] == "#":
                continue

            line = line.split(",")
            feature_types[line[0]] = FeatureType(line[0], line[1], line[2:])
        fh.close()
        return feature_types


class LandType:
    """
    The types of landscapes available
    """
    def __init__(self, id, traveltime, viewdistance, inside_description, edge_description, lighting_paradigm, noun, effects):
        self.id = id
        self.traveltime = traveltime
        self.viewdistance = viewdistance
        self.inside_description = inside_description
        self.edge_description = edge_description
        self.lighting_paradigm = lighting_paradigm
        self.noun = noun
        self.effects = effects

    def get_description(self):
        return self.inside_description

    def get_lighting_paradigm(self):
        return self.lighting_paradigm

    @staticmethod
    def land_types_builder(file):
        land_types = {}
        fh = open(file)
        for line in fh:
            line = line.strip()
            if len(line) == 0 or line[0] == "#":
                continue

            line = line.split(",")
            land_types[line[0]] = LandType(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7:])
        fh.close()
        return land_types


class Feature:
    """
    The types of features one may encounter on the map
    """
    def __init__(self, type, x, y):
        self.feature_type = type
        self.x = x
        self.y = y

    @staticmethod
    def features_builder(file, feature_types):
        features = {}
        fh = open(file)
        for line in fh:
            line = line.strip()
            if len(line) == 0 or line[0] == "#":
                continue

            line = line.split(",")
#            raise BaseException(line)

            id = line[0]
            x = int(line[1])
            y = int(line[2])

            if not x in features:
                features[x] = {}

            features[x][y] = Feature(feature_types[id], x, y)

        fh.close()
        return features


class Land:
    """
    The patchwork of land on the map

    WE ASSUME THE PATCHWORK IS PERFECTLY COMPLETE WITHOUT OVERLAPS
    If this is the case, the map can be minimally defined by top-left points,
    except for the bottom-right edges of the world (so we define them everywhere)
    """
    def __init__(self, id, type, tl_x, tl_y, br_x, br_y):
        self.land_id = id
        self.land_type = type
        self.tl_x = tl_x  # minimal ID
        self.tl_y = tl_y  # minimal ID
        self.br_x = br_x
        self.br_y = br_y

    def get_description(self):
        return self.land_type.get_description()

    def get_lighting_paradigm(self):
        return self.land_type.get_lighting_paradigm()

    @staticmethod
    def lands_builder(file, land_types):

        lands = {}
        lands_by_coordinate = {}
        borders_west_x = {}  # western borders
        borders_east_x = {}  # eastern borders
        borders_north_y = {}  # northern borders
        borders_south_y = {}  # southern borders

        borders_x = []
        borders_y = []

        fh = open(file)
        for line in fh:
            line = line.strip()
            if len(line) == 0 or line[0] == "#":
                continue

            line = line.split(",")

            land_id = line[0]
            land_type_id = line[1]
            tl_x = int(line[2])
            tl_y = int(line[3])
            br_x = int(line[4])
            br_y = int(line[5])

            borders_x.extend([tl_x, br_x])
            borders_y.extend([tl_y, br_y])

            lands[land_id] = Land(land_id, land_types[land_type_id], tl_x, tl_y, br_x, br_y)

            if not tl_x in lands_by_coordinate:
                lands_by_coordinate[tl_x] = {}

            lands_by_coordinate[tl_x][tl_y] = lands[land_id]

            def add_border(id, coord, border_set):
                if coord in border_set:
                    border_set[coord].append(land_id)
                else:
                    border_set[coord] = [land_id]

            add_border(land_id, tl_x, borders_west_x)
            add_border(land_id, tl_y, borders_north_y)
            add_border(land_id, br_x, borders_east_x)
            add_border(land_id, br_y, borders_south_y)

        fh.close()

        sorted_tl_x = sorted(set(borders_x))
        sorted_tl_y = sorted(set(borders_y))

        #raise BaseException(lands_by_coordinate)

        return (lands,
                lands_by_coordinate,
                borders_west_x,
                borders_east_x,
                borders_north_y,
                borders_south_y, sorted_tl_x, sorted_tl_y)


class Level:
    """
    Holds the interesting bits and pieces of the individual levels
    """

    def __init__(self, landscape_file, features_file, land_types_file, feature_types_file):
        self.FeatureTypes = FeatureType.feature_types_builder(feature_types_file)
        self.LandTypes = LandType.land_types_builder(land_types_file)

        self.Features = Feature.features_builder(features_file, self.FeatureTypes)

        (self.Lands, self.LandsByCoordinate, self.WesternBorders,
         self.EasternBorders, self.NorthernBorders,
         self.Southern_borders, self.SortedTLx,
         self.SortedTLy) = Land.lands_builder(landscape_file, self.LandTypes)

    def get_land_coordinates(self, x, y):

        ## we assume that x and y are in here somewhere, so they MUST be within the borders of the map

        #raise BaseException(self.SortedTLy)

        assert(y >= self.SortedTLy[0])
        assert(y < self.SortedTLy[-1])
        assert(x >= self.SortedTLx[0])
        assert(x < self.SortedTLx[-1])

        tl_y_index = 0
        while y > self.SortedTLy[tl_y_index + 1]:
            tl_y_index += 1

        tl_x_index = 0
        while x > self.SortedTLx[tl_x_index + 1]:
            tl_x_index += 1

        #raise BaseException((self.SortedTLy, self.SortedTLx))

        return (self.SortedTLx[tl_x_index], self.SortedTLy[tl_y_index])

    def get_land(self, x, y):
        #raise BaseException((x, y))
        (TLx, TLy) = self.get_land_coordinates(x, y)
        #raise BaseException((TLx, TLy))

        return self.LandsByCoordinate[TLx][TLy]

    def get_description(self, x, y):
        return self.get_land(x, y).get_description()

    def get_lighting_paradigm(self, x, y):
        return self.get_land(x, y).get_lighting_paradigm()


class DriftWorld:
    """
    Holds and manages the world, and all the maps in it
    (model) - static, for the most part... that is unless you've dug a hole or something.

    A few different functions

    There is a root map, which is the outer landscape. Additional maps are connected to the root map
    via entrances (tbd).
    """

    def __init__(self, world_map_filename):
        self.levels = {}

        self.starting_level = ""
        self.starting_x = 0
        self.starting_y = 0

        fh = open(world_map_filename)
        for line in fh:
            line = line.strip()
            if len(line) == 0 or line[0] == "#":
                continue

            line = line.split(",")

            level_id = line[0]
            landscape_file = line[1]
            features_file = line[2]
            land_types_file = line[3]
            feature_types_file = line[4]
            starting_level = line[5]
            starting_x = int(line[6])
            starting_y = int(line[7])

            self.levels[level_id] = Level(landscape_file, features_file, land_types_file, feature_types_file)

            if starting_level:
                self.starting_level = level_id
                self.starting_x = starting_x
                self.starting_y = starting_y

        fh.close()

    def get_description(self, level, x, y):
        return self.levels[level].get_description(x, y)

    def get_lighting_paradigm(self, level, x, y):
        return self.levels[level].get_lighting_paradigm(x, y)
