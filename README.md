# Implimentation-of-Depth-First-Search-DFS-
A Python implementation of the Depth-First Search (DFS) algorithm using an undirected adjacency matrix.

## What this project does

The dfs() function takes: An undirected adjacency matrix representing the graph.
A starting node label. It traverses the graph using DFS and returns a list containing all nodes that are reachable from the starting node.

## Key concepts
Depth-First Search
Graph traversal
Adjacency matrices
Recursion
Tracking visited nodes

# Example usage 
graph = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

print(dfs(graph, 1))

The function starts at node 1, explores as deeply as possible, and returns the nodes it can reach.

Learning
This exercise helped me practice implementing graph traversal with recursion, working with adjacency matrices, and preventing repeated visits using a visited list.
