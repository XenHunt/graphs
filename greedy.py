from typing import Dict

import matplotlib.pyplot as plt
import networkx as nx

# Словарь цветов по числу
COLORS = {
    0: "red",
    1: "blue",
    2: "green",
    3: "orange",
    4: "purple",
    5: "brown",
    6: "pink",
    7: "gray",
    8: "olive",
    9: "cyan",
}


# Создадим функции генерирующую рандомный граф и выводяющую его на экран
def randomShow(nodes: int):
    """
    Функция генерирующая рандомный граф и выводяющая его на экран

    :param nodes: количество вершин
    """

    G = nx.gnp_random_graph(nodes, 0.5)
    nx.draw(G)
    plt.show()


# В этом файле будет реализован жадный алгоритм расскраски графов
def coloringGreedy(graph: nx.Graph):
    """
    Функция, реализующая расскраску графа жадным алгоритмом

    Args:
        graph: граф

    Returns:
        Расскраску - словарь, где ключ - вершина, а значение - цвет.
    """
    colors = {}
    for node in graph.nodes:
        colors[node] = 0

    for node in graph.nodes:
        neighbors = list(graph.neighbors(node))
        while any(colors.get(neighbor, 0) == colors[node] for neighbor in neighbors):
            colors[node] += 1

    return colors


# Функция по заданным цветам расскрашивает граф и выводи на экран
def showColoring(graph: nx.Graph, colors: Dict[int, int]):
    """
    Функция расскраски графа по цветам

    :param graph: граф
    :param colors: цвета
    """

    nx.draw(graph, node_color=[COLORS[colors[node]] for node in graph.nodes])
    plt.show()


graph = nx.gnp_random_graph(20, 0.3)
showColoring(graph, coloringGreedy(graph))
# randomShow(10)
