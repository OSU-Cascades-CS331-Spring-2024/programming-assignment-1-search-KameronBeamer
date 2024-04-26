# tracks a given search's metrics and can generate reports on those metrics
class ScoreTracker():
    def __init__(self):
        self.path = []
        self.path_cost = 0
        self.visited = 0
        self.expanded = 0
        self.maintained = 0

    # generates a report on the stored metrics
    def generate_report(self):
        report = f"Path: {self.path}\nCost: {self.path_cost}\nVisited: {self.visited}\nExpanded: {self.expanded}\nMaintained: {self.maintained}"
        return report
    
    def set_path(self, path):
        self.path = path

    def add_path(self, city):
        self.path.append(city)
    
    def remove_path(self, city):
        self.path.remove(city)