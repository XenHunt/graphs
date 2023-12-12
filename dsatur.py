import heapq
from typing import Dict

import matplotlib.pyplot as plt
import networkx as nx

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


# Функция раскрашивающая граф по алгоритму DSATUR
def coloringDsatur(graph: nx.Graph) -> Dict:
    """
    Функция, реализующая расскраску по методу DSATUR

    Args:
        graph: граф

    Returns:
        Расскраску графа - словарь, где ключ - вершина, а значение - цвет
    """
    # Степень насыщения и степень каждой вершины
    saturation = {node: 0 for node in graph.nodes()}
    degree = {node: len(list(graph.neighbors(node))) for node in graph.nodes()}

    # Максимальное количество цветов
    color = {node: -1 for node in graph.nodes()}

    # Очередь приоритетов для выбора вершин (сначала с наибольшей степенью насыщения, затем с наибольшей степенью)
    queue = []
    for node in graph.nodes():
        heapq.heappush(queue, (-saturation[node], -degree[node], node))

    while queue:
        _, _, node = heapq.heappop(queue)

        # Выбор цвета для выбранной вершины
        used_colors = set(
            color[neigh] for neigh in graph.neighbors(node) if color[neigh] != -1
        )
        for i in range(len(graph)):
            if i not in used_colors:
                color[node] = i
                break

        # Обновление степени насыщения соседних вершин и обновление очереди
        for neighbor in graph.neighbors(node):
            if color[neighbor] == -1:
                saturation[neighbor] += 1
                queue.remove((-saturation[neighbor] + 1, -degree[neighbor], neighbor))
                heapq.heappush(
                    queue, (-saturation[neighbor], -degree[neighbor], neighbor)
                )

    return color


# Функция по заданным цветам расскрашивает граф и выводи на экран
def showColoring(graph: nx.Graph, colors: Dict):
    """
    Функция расскраски графа по цветам

    :param graph: граф
    :param colors: цвета
    """

    nx.draw(graph, node_color=[COLORS[colors[node]] for node in graph.nodes])
    plt.show()


graph = nx.gnp_random_graph(20, 0.3)
showColoring(graph, coloringDsatur(graph))
