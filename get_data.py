def get_data(file):
    data = open("tests/" + file)
    size = data.readline().split(" ")
    v = int(size[0])
    edges = int(size[1])
    g = [[] for i in range(v)]
    for edge in range(edges):
        e = data.readline().split()
        g[int(e[0])].append((int(e[1]), int(e[2])))
    return g