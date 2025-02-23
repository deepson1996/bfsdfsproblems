import pandas as pd
from search import Node, StackFrontier, QueueFrontier

df = pd.read_csv("data.csv")
data = df.to_records(index=False)


def main():
    start = "user_47"
    target = "user_7"

    print(find_path(start, target))
def get_neighbors(state):
    neighbors = []
    for record in data:
        p1, p2 = record
        if p1 == state:
            neighbors.append(p2)
        elif p2 == state:
            neighbors.append(p1)
    return neighbors

def find_path(start, target):
    node = Node(state=start, parent=None, action=None)
    frontier = QueueFrontier()
    frontier.add(node)
    
    explored = set()
    count = 0
    
    while True:
        if frontier.empty():
            raise Exception("No path found")
        
        node = frontier.remove()
        explored.add(node.state)
        count += 1
        
        if node.state == target:
            paths = []
            while node is not None:
                paths.append(node.state)
                node = node.parent
            paths.reverse()
            print(count)
            return paths
        
        for person in get_neighbors(node.state):
            if (person not in explored) and (not frontier.contains_state(person)):
                child = Node(state=person, parent=node, action=None)
                frontier.add(child)
                
if __name__ == "__main__":
    main()