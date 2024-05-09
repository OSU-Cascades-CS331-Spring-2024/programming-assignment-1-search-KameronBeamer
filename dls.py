from search import Search

class DepthLimitedSearch(Search):
    def __init__(self, map, start = None, goal = None, score_tracker = None):
        super().__init__(map, start, goal, score_tracker)

    def set_new_search(self, start, goal, score_tracker):
        self.set_trip(start, goal)
        self.set_score_tracker(score_tracker)

    def set_trip(self, start, goal):
        self.start = start
        self.goal = goal

    def set_score_tracker(self, score_tracker):
        self.score_tracker = score_tracker

    def get_score_report(self):
        return self.score_tracker.generate_report()
    
    def run(self):
        pass