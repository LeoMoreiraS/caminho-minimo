from dijkstra import dijkstra
from shared import print_result
from bellman_ford import homemsino_ford

def get_data(file):
    data = open(file)
    size = data.readline().split(" ")
    v = int(size[0])
    edges = int(size[1])
    g = [[] for i in range(v)]
    for edge in range(edges):
        e = data.readline().split()
        g[int(e[0])].append((int(e[1]), int(e[2])))
    return g

print("toy")
print_result(dijkstra(get_data("tests/toy.txt"), 0), 0, 1)
print_result(dijkstra(get_data("tests/toy.txt"), 0), 0, 2)
print_result(dijkstra(get_data("tests/toy.txt"), 0), 0, 3)
print_result(dijkstra(get_data("tests/toy.txt"), 0), 0, 4)
print("face Dijkstra")
print_result(dijkstra(get_data("tests/facebook_combined.txt"), 0), 0, 100)
print("face Bellman")
print_result(homemsino_ford(get_data("tests/facebook_combined.txt"), 0), 0, 100)
print("rome Dijkstra")
print_result(dijkstra(get_data("tests/rome99c.txt"), 0), 0, 100)
print("rome Bellman")
print_result(homemsino_ford(get_data("tests/rome99c.txt"), 0), 0, 100)
print("rg300 Dijkstra")
print_result(dijkstra(get_data("tests/rg300_4730.txt"), 0), 0, 100)
print("rg300 Bellman")
print_result(homemsino_ford(get_data("tests/rg300_4730.txt"), 0), 0, 100)
print("USA Dijkstra")
print_result(dijkstra(get_data("tests/USA-road-dt.DC.txt"), 0), 0, 100)
print("USA Bellman")
print_result(homemsino_ford(get_data("tests/USA-road-dt.DC.txt"), 0), 0, 100)