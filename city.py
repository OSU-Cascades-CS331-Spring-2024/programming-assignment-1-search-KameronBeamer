class City:
    def __init__(self, name, lat, long, neighbors):
        self.name = name
        self.lat = lat
        self.long = long
        self.neighbors = neighbors
        print(self.name, self.lat, self.long, self.neighbors)
