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
    # print(get_neighbors(maze, (0,1)))
    start, end = positions(maze, s, e)
    # print(start, end)
    paths = find_path(maze, start, end)
    
    res = maze.copy()
    for loc in paths:
        i, j = loc
        if res[i][j] not in [s, e]:
            res[i][j] = "*" 
    print(np.array(res))

def positions(maze, s, e):
    """
    provided with inputs maze: list, starting value:string and ending value:string return starting and ending position as tuples eg: (0, 0), (1, 1)
    """
    start = (0, 0)
    end = (len(maze)-1, len(maze[0])-1)
    
    for i, row in enumerate(maze):
        for j, elem in enumerate(row):
            if elem == s:
                start = (i, j)
            elif elem == e:
                end = (i, j)
    return start, end
    
            
def get_neighbors(maze,state):
    """
    provided with inputs maze: list and state: tuple(current position) return neighbors: return list of tuples for left, right, up, and down positions if valid. eg: [(1, 2), (1, 3), ..]
    """
    neighbors = []
    row, col = state
    # left (0, 0) => (0, -1) 
    new_col = col -1
    if new_col >= 0:
        if maze[row][new_col] != 0:
            neighbors.append((row, new_col))
    
    # right
    new_col = col + 1
    if new_col < len(maze[0]):
        if maze[row][new_col] != 0:
            neighbors.append((row, new_col))
    # up
    new_row = row - 1
    if new_row >= 0:
        if maze[new_row][col] != 0:
            neighbors.append((new_row, col))
    #down
    new_row = row + 1 
    if new_row < len(maze):
        if maze[new_row][col] != 0:
            neighbors.append((new_row, col))
        
    return neighbors
    
    

def find_path(maze, start, target):
    """
    Complete the function return list of tuple action and state if found
    """
    node = Node(state=start, parent=None, action=None)
    frontier = StackFrontier()
    frontier.add(node) 
    
    explored = set()
    count = 0
    
    while True:
        if frontier.empty():
            raise Exception("Path not found") 
        
        node = frontier.remove()
        
        if node.state == target:
            paths = []
            while node.parent is not None:
                paths.append(node.state)
                node = node.parent
            paths.reverse()
            print("explored: ", count)
            return paths
        
        explored.add(node.state) 
        count += 1
        
        neighbors = get_neighbors(maze, node.state)
        
        for state in neighbors:
            if (state not in explored) and (not frontier.contains_state(state)):
                child = Node(state=state, parent=node, action=None)
                frontier.add(child)
        
        
        
         
        
        


if __name__ == "__main__":
    main()