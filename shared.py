def print_result(tupla, o, d):
    pred = tupla[0][d]
    caminho = []
    caminho.insert(0, d)
    caminho.insert(0, pred)
    while pred != o:
        pred = tupla[0][pred]
        caminho.insert(0, pred)
    print(f"Caminho: {caminho}\nCusto: {tupla[1][d]}")
