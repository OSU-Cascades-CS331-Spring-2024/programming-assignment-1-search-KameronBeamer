# Breadth first search, searches through all of the current nodes neighbors before moving on to the next
from search import Search
from queue import Queue
from node import Node

class BreadthFirstSearch(Search):
    def __init__(self, map, start = None, goal = None, score_tracker = None):
        super().__init__(map, start, goal, score_tracker)

    # Sets a new search goal, as well as a score tracker for computational purposes
    def set_new_search(self, start, goal, score_tracker):
        self.set_trip(start, goal)
        self.set_score_tracker(score_tracker)

    def set_trip(self, start, goal):
        self.start = start
        self.goal = goal

    def set_score_tracker(self, score_tracker):
        self.score_tracker = score_tracker

    # Returns the report from score_tracker
    def get_score_report(self):
        return self.score_tracker.generate_report()
    
    # runs the given search algorithm
    def run(self):
        q = Queue(255)
        q.put(self.start)
        visited = [self.start]
        first_node = Node(self.start)

        # while the queue is not empty
        while q != []:
            current_city = q.get()

            # if we found the goal
            if current_city == self.goal:
                return current_city
            # for every vertex of our current city
            for neighbor in self.map.get_city_neighbors(current_city):
                # if it's not visited
                if neighbor not in visited:
                    # add it to the queue
                    visited.append(neighbor)
                    q.put(neighbor)
                    