# Our graph nodes
# Contains their local information and verticies to connected nodes
class City:
    def __init__(self, name, lat, long, neighbors):
        self.name = name
        self.lat = lat
        self.long = long
        self.neighbors = neighbors

    def get_neighbors(self):
        return self.neighbors