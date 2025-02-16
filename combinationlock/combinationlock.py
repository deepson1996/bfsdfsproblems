import sys
sys.path.append('../')
from search import Node, StackFrontier, QueueFrontier
def main():
    initial_state = [0, 0, 0, 0]
    target = [0, 5, 6, 2]
    
    # print(get_neighbors(initial_state))
    
    path = find_path(initial_state, target)
    for state, action in path:
        print(f"increment {action} index => {state}")
 
def get_neighbors(state):
    """
    provided with current state, return what the neighbors are as list of lists. eg [0, 0, 0, 0] => [[0, 0, 0, 1], [0, 0, 1, 0], ....] check for the boundary of 9 as its the max number on the wheel
    """
    neighbors = []
    max_num = 9
    
    for i in range(len(state)):
        new_val = state[i] + 1
        if new_val <= max_num:
            copy_state = state.copy()
            copy_state[i] += 1
            
            neighbors.append((copy_state, f"Incremented index {i}"))
            
    return neighbors
    
    

def find_path(start, target):
    """
    Complete the find path function
    
    """
    node = Node(state=start, parent=None, action = None)
    frontier = QueueFrontier()
    frontier.add(node)
    explored = set()
    count = 0
    while True:
        if frontier.empty():
            raise Exception("No path found")
        node = frontier.remove()
        if node.state == target:
            paths = []
            while node.parent is not None:
                paths.append((node.state, node.action))
                node = node.parent
            paths.reverse()
            print("Explored steps:", count)
            return paths
        explored.add(tuple(node.state))
        count += 1
        neighbors = get_neighbors(node.state)
        for neighbor, action in neighbors:
            if (tuple(neighbor) not in explored) and (not frontier.contains_state(node.state)):
                child = Node(state=neighbor, parent=node, action=action)
                frontier.add(child)
                
        
        
    
            
        
if __name__ == "__main__":
    main()