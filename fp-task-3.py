import heapq


class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = dict()

    def add_vertex(self, value):
        self.vertices.add(value)
        self.edges[value] = []

    def add_edge(self, from_vertex, to_vertex, weight):
        self.edges[from_vertex].append((to_vertex, weight))
        self.edges[to_vertex].append((from_vertex, weight))


def dijkstra(graph, start_vertex):
    # Ініціалізація відстаней до всіх вершин як нескінченні
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start_vertex] = 0

    # Використання бінарної купи для оптимізації вибору вершин
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо знайдено коротший шлях до поточної вершини, оновити відстань
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.edges[current_vertex]:
            distance = current_distance + weight

            # Якщо нова відстань менша за поточну, оновити відстань та додати вершину в чергу
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Створення графа
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B', 1)
my_graph.add_edge('A', 'C', 4)
my_graph.add_edge('B', 'C', 2)
my_graph.add_edge('B', 'D', 5)
my_graph.add_edge('C', 'D', 3)

# Знаходження найкоротших шляхів від початкової вершини 'A'
start_vertex = 'A'
shortest_paths = dijkstra(my_graph, start_vertex)

# Виведення результатів
for vertex, distance in shortest_paths.items():
    print(f"Найкоротший шлях від {start_vertex} до {vertex}: {distance}")
