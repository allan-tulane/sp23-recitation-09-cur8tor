from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    # Create an empty list to represent the frontier of nodes to explore
    frontier = []
    
    # Create an empty dictionary to keep track of visited nodes
    visited = dict()
    
    # Add a tuple representing the source node to the frontier using priority queue logic
    # The tuple contains 3 values - the cost from start, the current node and the previous node 
    heappush(frontier, (0, source, 0))
    
    # Call the function shortest_path with the created visited dictionary, frontier list and graph as arguments
    return shortest_path(visited, frontier, graph)
    

def shortest_path(visited, frontier, graph):
    if len(frontier) == 0:
        return visited
    else:
        distance, node, edge_count = heappop(frontier)
        if node in visited:
            return shortest_path(visited, frontier, graph)
        else:
            visited[node] = (distance, edge_count)
            for neighbor, weight in graph[node]:
              print(distance + weight, neighbor, edge_count)
              heappush(frontier, (distance + weight, neighbor, edge_count + 1))                
        return shortest_path(visited, frontier, graph)
    
def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    # result has both the weight and number of edges in the shortest shortest path
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)
    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    # Create an empty dictionary to store the resulting shortest path
    result = dict()
    
    # Add the source node to the frontier set
    frontier = set([source])
    
    # Keep looping until all nodes have been explored
    while len(frontier) != 0:
        # Pop a node from the frontier set
        source = frontier.pop()
        
        # Get neighbors of the popped node
        neighbors = graph[source]
        
        # Explore each neighbor of the popped node, and update result dictionary accordingly
        for leaf in neighbors: 
          if leaf not in result.keys():
            frontier.add(leaf)
            result[leaf] = source
        
    # Return the final resulting dictionary containing the shortest path to each node from the source
    return result
    

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert parents['a'] == 's'
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'
    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    # Get the source node from the parents dictionary by using the first value as a list and selecting the first item from that list
    source = list(parents.values())[0]
    
    # Initialize the path with the source node
    path = str(source)
    
    # Get the neighbors of the source node (nodes directly connected to the source)
    neighbors = [k for k, v in parents.items() if v == path[-1]]
    
    # Keep exploring until we find the destination node
    while destination not in neighbors:
        # If any of the neighbors is already in path, then it's a loop. Thus, we don't want to extend the path further.
        # Otherwise, we add the last character (node) of each neighbor to the path, and update neighbors accordingly.
        for leaf in neighbors:
          if leaf in parents.values():
            path += leaf
            neighbors = [k for k, v in parents.items() if v == path[-1]]
    
    # Return the final resulting path from source to destination
    return path
    

def test_get_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert get_path(parents, 'd') == 'sbc'

graph = {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

# test_shortest_shortest_path()
# test_bfs_path()
# test_get_path()