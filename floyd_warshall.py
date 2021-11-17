import math
import numpy as np

def list_to_matrix(list):
    tam = len(list)
    matrix = np.zeros((tam, tam))
    for index, adjlist in enumerate(list, start=0):
        for item in adjlist:
            matrix[index][item[0]] = item[1]
    return matrix

def floyd_warshall(grafo):
    vertices = len(grafo)
    dist = np.zeros((vertices, vertices))
    pred = np.zeros((vertices, vertices))
    for i in range(vertices):
        for j in range(vertices):
            if i == j:
                dist[i][j] = 0
                pred[i][j] = None
            elif grafo[i][j] != 0:
                dist[i][j] = grafo[i][j]
                pred[i][j] = i
            else:
                dist[i][j] = math.inf
                pred[i][j] = -1
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
    return pred, dist