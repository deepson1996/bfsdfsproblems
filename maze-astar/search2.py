import sys

class Node:
    def __init__(self, state, parent, action, h_cost, g_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.h_cost = h_cost
        self.g_cost = g_cost
class StackFrontier: # For dfs
    def __init__(self):
        self.frontier = []
        
    def add(self, node):
        self.frontier.append(node)
        
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[-1] # last in first out
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier): # inherits all other things from stack an
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[0] # last in first out
            self.frontier = self.frontier[1:]
            return node       
class AStarFrontier(QueueFrontier):
    def add(self, node):
        self.frontier.append(node)
        self.frontier.sort(key=lambda x: (x.h_cost + x.g_cost))
        
    