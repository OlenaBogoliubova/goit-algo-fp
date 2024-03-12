import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq


# Вузол бінарного дерева

class Node:
    def __init__(self, key, color="skyblue"):
      # Лівий нащадок
        self.left = None
      # Правий нащадок
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())


# Додаємо ребра та вузли бінарного дерева до графу graph за допомогою рекурсивного підходу
# Функція обходить дерево та додає кожен вузол та ребро до графу. Координати вузлів використовуються для відображення графу в Matplotlib.

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


# Створюється корінь дерева root зі значенням 0. Додаються лівий та правий нащадки для кореня зі значеннями 4, 5, 10, 1, 3. Викликається функція draw_tree для відображення створеного дерева.
# Цей код створює бінарне дерево та відображає його графічно з використанням бібліотек networkx та matplotlib.
# Графічне представлення має вигляд дерева з вузлами різного кольору та значеннями.

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(
        data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
draw_tree(root)


class MaxHeapNode:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_heap_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_heap_edges(graph, node.left, pos, x=l,
                               y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_heap_edges(graph, node.right, pos, x=r,
                               y=y - 1, layer=layer + 1)
    return graph


def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_heap_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


# Створення бінарної купи
heap_root = MaxHeapNode(15)
heap_root.left = MaxHeapNode(13)
heap_root.right = MaxHeapNode(12)
heap_root.left.left = MaxHeapNode(8)
heap_root.left.right = MaxHeapNode(5)
heap_root.right.left = MaxHeapNode(3)
heap_root.right.right = MaxHeapNode(10)

# Відображення бінарної купи
draw_heap(heap_root)
