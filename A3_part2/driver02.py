'''
driver for graph search problem
'''

from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections
import time
import searchstrategies


class Timer:
    """Timer class
    Usage:
      t = Timer()
      # figure out how long it takes to do stuff...
      elapsed_s = t.elapsed_s() OR elapsed_min = t.elapsed_min()
    """
    
    def __init__(self):
        "Timer - Start a timer"
        self.s_per_min = 60.0  # Number seconds per minute
        self.start = time.time()

    def elapsed_s(self):
        "elapsed_s - Seconds elapsed since start (wall clock time)"
        return time.time() - self.start

    def elapsed_min(self):
        "elapsed_min - Minutes elapsed since start (wall clock time)"

        # Get elapsed seconds and convert to minutes
        return self.elapsed_s() / self.s_per_min
    
def driver() :

    numOfBoard = 10

    # dfs_nodes = []
    # dfs_elapsed = []
    # dfs_length = []

    bfs_nodes = []
    bfs_elapsed = []
    bfs_length = []

    # astar_nodes = []
    # astar_elapsed = []
    # astar_length = []

    for _ in range(numOfBoard):
        puzzle = NPuzzle(8,g=BreadthFirst.g, h = BreadthFirst.h)
        result = graph_search(puzzle)
        bfs_length.append(len(result[0]))
        bfs_nodes.append(result[1])
        bfs_elapsed.append(result[2])

    print('Length of plan')
    print('Mean: ',  '{:10}'.format(mean(bfs_length))  ,   ' STD: ', '{:10}'.format(stdev(bfs_length)))
    print('Number of nodes')
    print('Mean: ',  '{:10}'.format(mean(bfs_nodes))  ,   ' STD: ', '{:10}'.format(stdev(bfs_nodes)))
    print('Elapsed time in second')
    print('Mean: ',  '{:10}'.format(mean(bfs_elapsed))  ,   ' STD: ', '{:10}'.format(stdev(bfs_elapsed)))

    
    # raise NotImplemented

if __name__ == '__main__':
    driver()
