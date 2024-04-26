import argparse
import sys
from map import Map
from agent import Agent
from scoreTracker import ScoreTracker
from bfs import BreadthFirstSearch
from dls import DepthLimitedSearch
from ucs import UniformCostSearch
from astar import AStar

# A dictionary of default searches to perform in multi_search
trips = {
    "brest": "nice",
    "montpellier": "calais",
    "strasbourg": "bordeaux",
    "paris": "grenoble",
    "grenoble": "paris",
    "brest": "grenoble",
    "grenoble": "brest",
    "nice": "nantes",
    "caen": "strasbourg"
}

# These structures allow us to instantiate classes by referencing a dict
def bfs(map):
    return BreadthFirstSearch(map)

def dls(map):
    return DepthLimitedSearch(map)

def ucs(map):
    return UniformCostSearch(map)

def astar(map):
    return AStar(map)

searches = {
    "bfs": bfs,
    "dls": dls,
    "ucs": ucs,
    "astar": astar
}

# runs every trip in trips with every search in searches
def multi_search(map, args, agent):
    for search in searches:
        # should I put this outside of this loop. If so, how?
        # use a list or dict oustide this loop and store values in it once they are calculated
        # average_explored = 0
        # average_score = 0
        # average_maintained = 0
        # times_optimal = 0
        current_search = searches[search](map)
        agent.set_search(current_search)

        for trip in trips:
            score_tracker = ScoreTracker()
            agent.set_new_search_trip(args.A, args.B, score_tracker)
            search_result = agent.run_search()
            print(f"Search: {search}\n{search_result}")

# Running only a single search algorithm
# Different enough from multi_search to warrant multiple functions
def single_search(map, args, agent):
        current_search = searches[args.S](map)
        agent.set_search(current_search)
        score_tracker = ScoreTracker()
        agent.set_new_search_trip(args.A, args.B, score_tracker)
        search_result = agent.run_search()
        print(f"Search: {args.S}\n{search_result}")


# Enables parse our arguments out of order and enforces requirments and actions where needed
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-A')
    parser.add_argument('-B')
    parser.add_argument('-F', required = True)
    parser.add_argument('-S', default = "bfs")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    map = Map(args.F)
    agent = Agent()

    if args.A == None or args.B == None:
        multi_search(map, args, agent)
    else:
        single_search(map, args, agent)

if __name__ == '__main__':
    main()
