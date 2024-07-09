class Graph:
    def __init__(self):
        self.vertices = {}
        
    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.vertices:
            self.vertices[from_vertex] = []
        if to_vertex not in self.vertices:
            self.vertices[to_vertex] = []
        self.vertices[from_vertex].append((to_vertex, weight))
        self.vertices[to_vertex].append((from_vertex, weight))  # Assuming undirected graph

    def get_neighbors(self, vertex):
        return self.vertices[vertex]

import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))
    
    def pop(self):
        return heapq.heappop(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0

def dijkstra(graph, start_vertex):
    # Initialize distances and predecessors
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start_vertex] = 0
    predecessors = {vertex: None for vertex in graph.vertices}
    
    # Initialize the priority queue
    min_heap = MinHeap()
    min_heap.push(start_vertex, 0)
    
    while not min_heap.is_empty():
        # Get the vertex with the smallest distance
        current_distance, current_vertex = min_heap.pop()
        
        # Process each neighbor of the current vertex
        for neighbor, weight in graph.get_neighbors(current_vertex):
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                min_heap.push(neighbor, distance)
    
    return distances, predecessors

# Create a graph
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

# Find the shortest paths from vertex 'A'
distances, predecessors = dijkstra(graph, 'A')

print("Shortest distances:", distances)
print("Predecessors:", predecessors)