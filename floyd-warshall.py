import math

import numpy as np

import shared as s


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
        print(f"\n--------{k}-------")
        for i in range(vertices):
            print("")
            for j in range(vertices):
                print(f"{dist[i][j]} > {dist[i][k]} + {dist[k][j]}  |  ", end="")
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    #print(f"Troca {dist[i][j]} > {dist[i][k]}+{dist[k][j]} k,i,j={k, i, j}")
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
        print("")
    return pred, dist


# matriz = list_to_matrix(s.g)
matriz2 = list_to_matrix([
    [(2, -2)],
    [(0, 4), (2, 3)],
    [(1, 5), (0, 2)]
])
tupla = floyd_warshall(matriz2)
s.print_result(tupla)
