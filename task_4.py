import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Additional argument to store the color of the node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.val, color=node.color)  # Saving a node color in a graph
        if node.left:
            graph.add_edge(node.val, node.left.val)
            l = x - 1 / 2 ** layer
            pos[node.left.val] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.val, node.right.val)
            r = x + 1 / 2 ** layer
            pos[node.right.val] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {(tree_root.val): (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]  # Collect node colors to display

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, with_labels=True, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def heap_binary_tree(heap):
    if not heap:
        return None

    nodes = [Node(val) for val in heap]

    for i in range(len(nodes)):
        index_left = 2 * i + 1
        index_right = 2 * i + 2

        if index_left < len(nodes):
            nodes[i].left = nodes[index_left]
        if index_right < len(nodes):
            nodes[i].right = nodes[index_right]

    return nodes[0] if nodes else None

def visualize_heap_tree(heap):
    root = heap_binary_tree(heap)
    draw_tree(root)

# Example usage
heap = [int(input("Enter the number 1 in range 0-99: ")), 
        int(input("Enter the number 2 in range 0-99: ")), 
        int(input("Enter the number 3 in range 0-99: ")), 
        int(input("Enter the number 4 in range 0-99: ")), 
        int(input("Enter the number 5 in range 0-99: ")), 
        int(input("Enter the number 6 in range 0-99: ")),
        int(input("Enter the number 7 in range 0-99: "))]

visualize_heap_tree(heap)