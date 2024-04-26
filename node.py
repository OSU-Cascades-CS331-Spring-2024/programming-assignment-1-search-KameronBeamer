class Node():
    def __init__(self, city, last_city = None):
        self.parent = last_city
        self.city = city