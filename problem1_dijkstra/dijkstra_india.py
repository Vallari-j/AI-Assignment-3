import csv
import heapq

def load_graph(filename):
    graph = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            src = row['source']
            dest = row['destination']
            dist = int(row['distance'])

            graph.setdefault(src, []).append((dest, dist))
            graph.setdefault(dest, []).append((src, dist))

    return graph


def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


if __name__ == "__main__":
    graph = load_graph("india_cities.csv")
    start = "Delhi"
    result = dijkstra(graph, start)

    print("Shortest distances from Delhi:")
    for city, dist in result.items():
        print(city, ":", dist)
