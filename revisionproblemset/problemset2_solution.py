from search import Node, QueueFrontier, StackFrontier, PriorityQueueFrontier

def main():
    graphs = [
        ([
            [0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]
        ], 0),
        ([
            [0, 20, 42, 35],
            [20, 0, 30, 34],
            [42, 30, 0, 12],
            [35, 34, 12, 0]
        ], 2),
        ([
            [0, 3, 0, 7, 9],
            [3, 0, 2, 0, 0],
            [0, 2, 0, 1, 0],
            [7, 0, 1, 0, 5],
            [9, 0, 0, 5, 0]
        ], 4)
    ]

    for cities, start in graphs:
        path, cost = tsp_greedy_dijkstra(cities, start)
        print(f"Start: {start}, Path: {path}, Total Cost: {cost}")
        
def dijkstra(cities, start):
    n = len(cities)
    distances = [float('inf')] * n
    distances[start] = 0
    visited = set()
    frontier = PriorityQueueFrontier()
    frontier.add(Node(state=start, parent=None, action=None, cost=0))
    
    while not frontier.empty():
        node = frontier.remove()
        current_node = node.state
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        for neighbor, cost in enumerate(cities[current_node]):
            if cost > 0 and neighbor not in visited:
                new_distance = distances[current_node] + cost
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    frontier.add(Node(state=neighbor, parent=node, action=None, cost=new_distance))
    return distances

def tsp_greedy_dijkstra(cities, start):
    node = Node(state=start, parent=None, action=None, cost=0)
    frontier = PriorityQueueFrontier()
    frontier.add(node)

    explored = set()
    path = []
    total_cost = 0
    count = 0

    while True:
        if frontier.empty():
            raise Exception("Path not found")

        node = frontier.remove()
        current_city = node.state

        if current_city in explored:
            continue

        explored.add(current_city)
        path.append(current_city)

        if len(explored) == len(cities):  # All cities visited
            break

        count += 1

        # Find the closest unvisited neighbor
        neighbors = [(city, cost) for city, cost in enumerate(cities[current_city]) if cost > 0 and city not in explored]

        for city, cost in sorted(neighbors, key=lambda x: x[1]):  # Sort by cost (greedy approach)
            if city not in explored and not frontier.contains_state(city):
                child = Node(state=city, parent=node, action=None, cost=node.cost + cost)
                frontier.add(child)

    # Return to the starting city
    path.append(start)
    total_cost = sum(cities[path[i]][path[i + 1]] for i in range(len(path) - 1))

    print("Explored:", count)
    return path, total_cost
if __name__ == "__main__":
    main()