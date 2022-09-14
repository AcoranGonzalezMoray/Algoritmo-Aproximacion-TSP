from collections import namedtuple
import networkx as nx
import math
import os

Point = namedtuple("Point", ['x', 'y'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
    
def complete_graph(points):
    """ Creates a complete graph """
    G = nx.Graph()
    for x in range(len(points)-1):
        G.add_node(x)
        G.add_edge(x, x+1, weight = length(points[x], points[x+1]))#next x+1, points[x+1]
    return G


def solve_2_approx(points):
    """ implements the Tree 2-approximate algorithm for TSP """
    G = complete_graph(points)
    min =nx.minimum_spanning_tree(G) #Árbol recubridor mínimo
    mul = nx.MultiGraph(min)
    mul.add_edges_from(min.edges())
    R= []
    for i in nx.eulerian_circuit(mul):
        if i[0] not in R:
            R.append(i[0])

    return R
