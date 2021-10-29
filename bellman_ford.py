import math
import sys
import numpy as np

import shared as s


def homemsino_ford(grafo, vertice):
    v = len(grafo)
    dist = np.full(shape=v, fill_value=math.inf)
    pred = np.full(shape=v, fill_value=-1)
    dist[vertice] = 0
    for i in range(v):
        t = False
        for j, arestas in enumerate(grafo):
            for aresta in arestas:
                if dist[aresta[0]] > dist[j] + aresta[1]:
                    dist[aresta[0]] = dist[j] + aresta[1]
                    pred[aresta[0]] = j
                    t = True
        if not t:
            break
    return pred, dist


# s.print_result(homemsino_ford([
#     [(2, -2)],
#     [(0, 4), (2, 3)],
#     [(1, 5), (0, 2)]
# ], 2))
# s.print_result(homemsino_ford(s.g, 0))
# s.print_result(homemsino_ford(s.f, 0))
# s.print_result(homemsino_ford(s.f, 2))
# s.print_result(homemsino_ford(s.h, 0))
