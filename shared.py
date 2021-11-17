def print_result(tupla, o, d):
    pred = tupla[0][d]
    caminho = []
    caminho.insert(0, d)
    caminho.insert(0, pred)
    while pred != o:
        pred = tupla[0][pred]
        caminho.insert(0, pred)
    print(f"Caminho: {caminho}\nCusto: {tupla[1][d]}")

def print_result_floyd(tupla, o, d):
    pred = int(tupla[0][o][d])
    caminho = []
    caminho.insert(0, d)
    caminho.insert(0, pred)
    while pred != o:
        pred = int(tupla[0][o][pred])
        caminho.insert(0, pred)
    print(f"Caminho: {caminho}\nCusto: {tupla[1][o][d]}")