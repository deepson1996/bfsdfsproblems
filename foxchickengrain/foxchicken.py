import sys
sys.path.append('../')
from search import Node, StackFrontier, QueueFrontier

def main():
    """
    positions
    0: boat
    1: fox
    2: chicken
    3: grain
    """
    start = [0, 0, 0, 0]
    target = [1, 1, 1, 1]
    
    # print(get_neighbors(start))
    path = get_path(start, target)
    
    for state, action in path:
        print(f"state:{state}, action:{action}")

def is_valid(state):
    """
    given state return if its valid or not. chicken and grain should not be together and so on
    """

def get_neighbors(state):
    """
    get input as state and returns combination of valid moves that state may have
    moves can be:
    1. boat only
    2. boat, fox if both are on same side
    3. boat, chicken if both are on same side
    4. boat, grain if both are on same side
    
    return array of arrays of neighbor states such as from [0, 0, 0, 0] => [[1, 0, 0, 0], [1, 1, 0, 0], ....]
    """
    
    
def get_path(start, target):
    """
    TODO: Your code goes here
    initialize frontier
    iterate until found or not found
        if empty frontier 
            no path found
        remove node
        if node state is target state
            return solution: list of tuples of state, action
            
        explore neighbors and add to frontier
        
    """
    

            
if __name__ == "__main__":
    main()
    
    