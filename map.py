# Acts as our graph, using the data for individual cities as our nodes
import re
from city import City

class Map:
    def __init__(self, map_file):
        self.cities = {}
        self.translate_map_with_regex(map_file)

    # Uses a regex to read a map file
    def translate_map_with_regex(self, map_file):
        #  and reading our map file
        map_file = open(map_file, "r")
        lines = map_file.readlines()

        # Using regex, seperate each item into groups
        # This approach, while rigid in form, allows us grab groups as long as they follow the provided file format
        map_regex = re.compile(r"(?P<name>.*)\s(?P<lat>\d*\s\d*\s\d*)\s(?P<lat_dir>.)\s(?P<long>\d*\s\d*\s\d*)\s(?P<long_dir>.)\s-->\s(?P<neighbors>.*)")
        for line in lines:
            matches = map_regex.match(line)

            # setting up our city parameters
            name = matches.group("name")
            lat = self.translate_coordinate_string_to_num(matches.group("lat"), matches.group("lat_dir"))
            long = self.translate_coordinate_string_to_num(matches.group("long"), matches.group("long_dir"))
            neighbors = self.translate_neighbor_string_to_dict(matches.group("neighbors"))

            city = City(name, lat, long, neighbors)
            self.cities[city.name] = city

        # cleaning up our mapfile
        map_file.close()

    # takes the coordinate string and direction and converts it to seconds (distance measurment)
    def translate_coordinate_string_to_num(self, coordinate_string, direction):
        coordinate_list = coordinate_string.split(" ")
        coordinate_num = 0

        # iterates through the coordinate backwards to use the minutes/hours multiplier
        multiplier_counter = 0
        for string in reversed(coordinate_list):
            temp_num = int(string)
            for i in range(multiplier_counter):
                temp_num *= 60
            multiplier_counter += 1
            coordinate_num += temp_num

        # returns possitive num for N and E coordinates, negative for S and W
        if direction == "N" or direction == "E":
            return coordinate_num
        else:
            return 0 - coordinate_num
        
    def translate_neighbor_string_to_dict(self, neighbor_string):
        # Iterates through our delimiters, applying them to the neighbor string
        delimiters = [" ", "va-"]
        neighbor_list = []
        for delimiter in delimiters:
            neighbor_string = " ".join(neighbor_string.split(delimiter))
        neighbor_list = neighbor_string.split()

        # iterates through every 2 items in our list and adds them as a key-value pair to our dict
        neighbor_dict = {}
        for name, distance in zip(neighbor_list[::2], neighbor_list[1::2]):
            neighbor_dict[name] = int(distance)

        return neighbor_dict
    
    def get_city(self, city):
        return self.cities[city]
    
    def get_city_neighbors(self, city):
        current_city = self.get_city(city)
        return current_city.get_neighbors()