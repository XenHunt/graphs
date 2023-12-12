import matplotlib.pyplot as plt
import time
import networkx as nx

import genetic
import dsatur
import greedy

sizes = [10,20,30,40,50,60,70,80,90,100]
genetic_list = []
greedy_list = []
dsatur_list = []
genetic_colors = []
greedy_colors = []
dsatur_colors = []

for size in sizes:
    graph = nx.gnp_random_graph(size, 0.4)

    start_time = time.time()
    genetic_result = genetic.coloringGenetics(graph).values()
    genetic_list.append(time.time() - start_time)
    genetic_colors.append(len(set(genetic_result)))

    start_time = time.time()
    greedy_result = greedy.coloringGreedy(graph).values()
    greedy_list.append(time.time() - start_time)
    greedy_colors.append(len(set(greedy_result)))

    start_time = time.time()
    dsatur_result = dsatur.coloringDsatur(graph).values()
    dsatur_list.append(time.time() - start_time)
    dsatur_colors.append(len(set(dsatur_result)))
    
    print(f"Genertic colors: {len(set(genetic_result))}")
    print(f"Greedy colors: {len(set(greedy_result))}")
    print(f"DSATUR colors: {len(set(dsatur_result))}")
    print()

plt.plot(sizes, genetic_colors, label='Genetic')
plt.plot(sizes, dsatur_colors, label='DSATUR')
plt.plot(sizes, greedy_colors, label='Greedy')

plt.xlabel('Size')
plt.ylabel('Number of Colors')

plt.legend()
plt.show()