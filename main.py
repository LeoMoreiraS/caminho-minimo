# Bibliotecas e funções
import sys
import time
from dijkstra import dijkstra
from bellman_ford import bellman_ford
import floyd_warshall
from get_data import get_data 
import shared
# Bibliotecas e funções

# Leitura dos dados
nomeDoArquivo = input("\nInforme o arquivo: ")
if (nomeDoArquivo != 'facebook_combined.txt' and nomeDoArquivo != 'rg300_4730.txt' and nomeDoArquivo != 'rome99c.txt' and nomeDoArquivo != 'toy.txt' and nomeDoArquivo != 'USA-road-dt.DC.txt'):
    print("\nArquivo não encontrado. Finalizando a aplicação...\n")
    sys.exit()

algoritmoSelecionado = int(input("\nAlgoritmo: \n  1 Dijkstra\n  2 Bellman-Ford\n  3 Floyd-Warshall\n"))
if (algoritmoSelecionado != 1 and algoritmoSelecionado != 2 and algoritmoSelecionado != 3):
    print("\nAlgoritmo não encontrado. Finalizando a aplicação...\n")
    sys.exit()

origem = int(input("\nOrigem: "))
destino = int(input("Destino: "))
# Leitura dos dados

# Chamada do algoritmo de acordo com as escolhas e atribuição de resultados nas variáveis
grafo = get_data(nomeDoArquivo)

if algoritmoSelecionado == 1:
    inicio = time.time()
    resultado = dijkstra(grafo, origem)
    final = time.time()
elif algoritmoSelecionado == 2:
    inicio = time.time()
    resultado = bellman_ford(grafo, origem)
    final = time.time()
else:
    grafo = floyd_warshall.list_to_matrix(grafo)
    inicio = time.time()
    resultado = floyd_warshall.floyd_warshall(grafo)
    final = time.time()
# Chamada do algoritmo de acordo com as escolhas e atribuição de resultados nas variáveis

print("\nProcessando...\n")

if algoritmoSelecionado == 3:
    shared.print_result_floyd(resultado, origem, destino)
else:
    shared.print_result(resultado, origem, destino)

print("Tempo: %fs\n" % (final - inicio))