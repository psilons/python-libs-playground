import networkx as nx

# https://epubs.siam.org/doi/10.1137/0201008
G = nx.DiGraph()
G.add_edges_from([(0,1),(0,2),(0,3),(0,4),(1,2),(1,4),(1,4),(3,4)])
H = nx.transitive_reduction(G)  # remove redundent edges
print(H.edges)
# [(0, 1), (0, 3), (1, 2), (1, 4), (3, 4)]
