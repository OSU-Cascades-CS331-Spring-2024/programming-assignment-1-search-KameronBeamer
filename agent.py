# Oue decision maker
# can set new searches, new trips, and make reports
from scoreTracker import ScoreTracker
from bfs import BreadthFirstSearch
from dls import DepthLimitedSearch
from ucs import UniformCostSearch
from astar import AStar

class Agent:
    # creates and stores searches with the provided args
    def __init__(self):
        self.map = map
        self.search = None

    # replaces the current search object
    def set_search(self, search):
        self.search = search

    def set_new_search_trip(self, start, goal, score_tracker):
        self.search.set_new_search(start, goal, score_tracker)

    def run_search(self):
        self.search.run()
        return self.search.get_score_report()