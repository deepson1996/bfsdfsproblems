import sys
sys.path.append('../')
from search import Node, StackFrontier, QueueFrontier
import numpy as np

           
def main():
    s = "s"
    e = "e"
    # maze = [[s, 1, 1, 0],
    #         [0, 0, 1, 1],
    #         [1, 1, 1, 0],
    #         [1, 0, 1, e]]

    maze = [
        [s, 1, 1, 0, 0, 0, 1, e],
        [1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 1, 1, 1, 0, 1],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 1]
    ]
    start, end = positions(maze, s, e)
    paths = find_path(maze, start, end)
    
    res = maze.copy()
    for loc, act in paths:
        i, j = loc
        if res[i][j] not in [s, e]:
            res[i][j] = "*" 
    print(np.array(res))

def positions(maze, s, e):
    """
    provided with inputs maze: list, starting value:string and ending value:string return starting and ending position as tuples eg: (0, 0), (1, 1)
    """
    pass
def get_neighbors(maze,state):
    """
    provided with inputs maze: list and state: tuple(current position) return neighbors: return list of tuples for left, right, up, and down positions if valid. eg: [(1, 2), (1, 3), ..]
    """
    pass
    

def find_path(maze, start, target):
    """
    Complete the function
    """
        


if __name__ == "__main__":
    main()