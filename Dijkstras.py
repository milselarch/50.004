from Graph import WeightedGraph

graph = WeightedGraph(edge_weights={
    ('s', 't'): 7,
    ('t', 's'): 8,
    ('t', 'y'): 2,
    ('x', 'y'): 9,
    ('t', 'x'): 1,
    ('x', 'z'): 8,
    ('y', 'z'): 7,
    ('z', 's'): 4,
    ('s', 'x'): 9,
    ('s', 'y'): 5
})

graph.dijkstras('s', node_order=['s', 't', 'x', 'y', 'z'])