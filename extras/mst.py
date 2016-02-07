from unionfind import UnionFind
from graph import WeightedGraph


def kruskal (graph, cost):

    edges = [(u, v) for u in graph.vertices() for v in graph.neighbours(u)]
    # Equivalent to following code:
    # for u in graph.vertices():
    #     for v in graph.neighbours(u):
    #         edges.append((u, v))

    # def sort_key (edge):
    #     return cost(edge[0], edge[1])

    # sort_key = lambda edge: cost(edge[0], edge[1])

    edges.sort(key=lambda edge: cost(edge[0], edge[1]))

    tree = []
    uf = UnionFind(graph.vertices())

    for (u, v) in edges:
        if uf.union(u, v):
            tree.append((u, v))

    return tree


def find_cost (edges, cost):
    return sum([cost(u, v) for (u, v) in edges])

if __name__ == '__main__':
    # Graph from worksheet
    wg = WeightedGraph()
    edges = [(1, 2, 2), (1, 3, 3), (2, 3, 3),
             (2, 4, 3), (2, 5, 1), (3, 6, 2),
             (4, 5, 4), (5, 6, 4), (4, 7, 2), (5, 8, 3), (6, 8, 1), (6, 9, 5),
             (4, 10, 1), (7, 10, 2), (8, 9, 3), (8, 10, 4), (10, 9, 2)]
    for (u, v, weight) in edges:
        wg.add_edge(u, v, weight)

    mst = kruskal(wg, wg.get_weight)
    assert find_cost(mst, wg.get_weight) == 17
