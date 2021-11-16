# Bibliotecas e funções
import sys
# Bibliotecas e funções

# Leitura dos dados
archiveName = input("\nInforme o arquivo: ")
if (archiveName != 'facebook_combined.txt' and archiveName != 'rg300_4730.txt' and archiveName != 'rome99c.txt' and archiveName != 'toy.txt' and archiveName != 'USA-road-dt.DC.txt'):
    print("\nArquivo não encontrado. Finalizando a aplicação...\n")
    sys.exit()

algorithmSelected = int(input("\nAlgoritmo: \n  1 Dijkstra\n  2 Bellman-Ford\n  3 Floyd-Warshall\n"))
if (algorithmSelected != 1 and algorithmSelected != 2 and algorithmSelected != 3):
    print("\nAlgoritmo não encontrado. Finalizando a aplicação...\n")
    sys.exit()

origin = int(input("\nOrigem: "))
destiny = int(input("Destino: "))
# Leitura dos dados

# Chamada do algoritmo de acordo com as escolhas e atribuição de resultados nas variáveis

arrayResult = [0, 1, 2, 3]
cost = 5
time = 0.003

# Chamada do algoritmo de acordo com as escolhas e atribuição de resultados nas variáveis

print("\nProcessando...\n")
print("Caminho:", arrayResult)
print("Custo:", cost)
print("Tempo: %fs\n" % (time))