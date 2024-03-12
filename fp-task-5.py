import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1, traversal_order=None):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val,
                       order=traversal_order[node.id])
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1,
                          layer=layer + 1, traversal_order=traversal_order)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1,
                          layer=layer + 1, traversal_order=traversal_order)
    return graph


def depth_first_traversal(node, traversal_order, color):
    if node is not None:
        traversal_order[node.id] = len(traversal_order)
        node.color = generate_color(color, len(traversal_order))
        depth_first_traversal(node.left, traversal_order, color)
        depth_first_traversal(node.right, traversal_order, color)


def breadth_first_traversal(root, traversal_order, color):
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        if current_node is not None:
            traversal_order[current_node.id] = len(traversal_order)
            current_node.color = generate_color(color, len(traversal_order))
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)


def generate_color(base_color, step):
    base_rgb = tuple(int(base_color[i:i + 2], 16) for i in (0, 2, 4))
    new_rgb = tuple(max(0, min(255, x - step * 20)) for x in base_rgb)
    return "#{:02X}{:02X}{:02X}".format(*new_rgb)


def draw_tree(tree_root, traversal_type):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}

    traversal_order = {}
    if traversal_type == "depth_first":
        depth_first_traversal(tree_root, traversal_order, "1296F0")
    elif traversal_type == "breadth_first":
        breadth_first_traversal(tree_root, traversal_order, "1296F0")

    tree = add_edges(tree, tree_root, pos, traversal_order=traversal_order)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


# Побудувати дерево
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обход дерева у глибину
draw_tree(root, "depth_first")

# Обход дерева у ширину
draw_tree(root, "breadth_first")
