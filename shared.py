def print_result(tupla,o ,d):
    pred = tupla[0][d]
    caminho = []
    caminho.insert(0, d)
    caminho.insert(0, pred)
    while pred != o:
        pred = tupla[0][pred]
        caminho.insert(0, pred)
    print(f"Caminho: {caminho}\nCusto: {tupla[1][d]}")


g = [[(2, 2), (1, 6)],
     [(4, 3), (2, 3), (3, 1)],
     [(1, 2), (3, 5)],
     [(4, 3)],
     [(0, 5)]
     ]

f = [[(1, 7), (2, 5), (4, 9)],
     [(3, 6)],
     [(1, 5), (3, 5), (4, 8)],
     [(4, 6)],
     []
     ]

h = [[(1, 5), (2, 3)],
     [(2, -3), (3, 2), (4, 5)],
     [(3, 4)],
     [(4, 4)],
     []
     ]

dota = [
    [(4, 4.8), (1, 1.5)],
    [(2, 1.9), (3, 1.2)],
    [(6, 4.4)],
    [(5, 2.1), (6, 3.9)],
    [(5, 0.9)],
    [(6, 1.7)],
    []
]
