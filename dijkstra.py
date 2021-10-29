import math
import sys

import numpy as np
import shared as s

def min_value(vertices, dist):
    u = [math.inf, -1, -1]
    for i, v in enumerate(vertices):
        if dist[v] < u[0]:
            u[0] = dist[v]
            u[1] = v
            u[2] = i
    return u
def dijkstra(grafo, vertice):
    dist = np.full(shape=len(grafo), fill_value=math.inf)
    pred = np.full(shape=len(grafo), fill_value=-1)
    dist[vertice] = 0
    vertices = np.array(range(len(grafo)))
    for i in range(0, len(vertices)):
        u = min_value(vertices, dist)
        vertices = np.delete(vertices, int(u[2]))
        for aresta in grafo[u[1]]:
            if dist[aresta[0]] > dist[u[1]] + aresta[1]:
                dist[aresta[0]] = dist[u[1]] + aresta[1]
                pred[aresta[0]] = u[1]
    return pred, dist


# tupla = dijkstra(s.g, 0)
# s.print_result(tupla)
# tupla2 = dijkstra(s.f, 0)
# s.print_result(tupla2)
# tupla2 = dijkstra(s.f, 1)
# s.print_result(tupla2)
#
#
# tupla2 = dijkstra(s.dota, 0)
# s.print_result(tupla2)
