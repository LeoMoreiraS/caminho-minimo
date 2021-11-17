import math
import numpy as np

def bellman_ford(grafo, vertice):
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
