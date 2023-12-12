import random

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
    10: "magenta",
    11: "yellow",
    12: "black",
    13: "lightblue",
    14: "lightgreen",
    15: "lightorange",
    16: "lightpurple",
    17: "lightbrown",
    18: "lightpink",
    19: "lightgray",
    20: "lightolive",
    21: "lightcyan",
    22: "lightmagenta",
    23: "lightyellow",
    24: "lightblack",
}


def create_chromosome(graph: nx.Graph) -> list[int]:
    """
    Функция создаёт хромосому по заданному графу. Хромосома - случайная расскраска графа

    Args:
        graph: граф

    Returns:
        list - список, где каждому индексу соответствует вершина, а значению - цвет
    """
    return [
        random.randint(1, graph.number_of_nodes())
        for _ in range(graph.number_of_nodes())
    ]


def calculate_fitness(graph: nx.Graph, chromosome: list[int]) -> int:
    """
    Высчитывает приспособленность хромосомы как количество совпадающих цветов у соседствующих вершин.

    Args:
        graph: граф
        chromosome: хромосома

    Returns:
        Приспособленность - кол-во совпадающих цветов у соседствующих вершин
    """
    return sum(
        color == chromosome[j]
        for i, color in enumerate(chromosome)
        for j in graph.neighbors(i)
    )


def select_parents(population: list[list[int]]):
    """
    Функция, которая случайным образом достаёт двух родителей из популяции.

    Args:
        population: популяция - список хромосом

    Returns:
        Двух родителей - две хромосомы
    """
    return random.sample(population, 2)


def crossover(parent1: list[int], parent2: list[int]):
    """
    Функция, которая перемешивает "ДНК" двух родителей

    Args:
        parent1: родитель 1
        parent2: родитель 2

    Returns:
        Потомство (offspring) в кол-ве двух штук
    """
    point = random.randint(1, len(parent1) - 2)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]


def mutate(chromosome: list[int]):
    """
    Функция, которая заставляет хромосому мутировать (случайным образом выбирает
    элемент хромосомы и меняет его на случайную величингу)

    Args:
        chromosome: хромосома

    Returns:
        Мутировушую хромосому
    """
    index = random.randint(0, len(chromosome) - 1)
    chromosome[index] = random.randint(1, len(chromosome))
    return chromosome


def genetic_algorithm(graph: nx.Graph, max_generations=10000) -> list[int]:
    """
    Функция запускающая генетический алгоритм

    Args:
        max_generations (по умолчанию 1000): максимальное количество поколений
        graph: граф

    Returns:
        Расскраску - список, где индекс - номер вершины, а значение - цвет
    """
    population_size = 100
    population = [create_chromosome(graph) for _ in range(population_size)]

    for _ in range(max_generations):
        population = sorted(population, key=lambda c: calculate_fitness(graph, c))
        if calculate_fitness(graph, population[0]) == 0:
            return population[0]
        next_generation = population[:2]
        for _ in range(population_size - 2):
            parents = select_parents(population)
            offspring = crossover(*parents)
            offspring = [mutate(chrom) for chrom in offspring]
            next_generation += offspring
        population = next_generation

    return min(population, key=lambda c: calculate_fitness(graph, c))


def coloringGenetics(graph: nx.Graph) -> dict:
    colors = genetic_algorithm(graph)
    return dict(zip(graph.nodes, colors))


# Функция по заданным цветам расскрашивает граф и выводи на экран
def showColoring(graph: nx.Graph, colors: dict):
    """
    Функция расскраски графа по цветам

    :param graph: граф
    :param colors: цвета
    """

    nx.draw(graph, node_color=[COLORS[colors[node]] for node in graph.nodes])
    plt.show()


graph = nx.gnp_random_graph(10, 0.3)
showColoring(graph, coloringGenetics(graph))
