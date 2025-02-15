import sys
sys.path.append('../')
from search import Node, StackFrontier, QueueFrontier
def main():
    initial_state = [0, 0, 0, 0]
    target = [0, 5, 6, 2]
    
    path = find_path(initial_state, target)
    for state, action in path:
        print(f"increment {action} index => {state}")
 
def get_neighbors(state):
    """
    provided with current state, return what the neighbors are as list of lists. eg [0, 0, 0, 0] => [[0, 0, 0, 1], [0, 0, 1, 0], ....] check for the boundary of 9 as its the max number on the wheel
    """  
    
def find_path(start, target):
    """
    Complete the find path function
    """
            
        
if __name__ == "__main__":
    main()