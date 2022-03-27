from Graph import WeightedGraph

graph = WeightedGraph(edge_weights={
    ('A', 'B'): -4,
    ('B', 'C'): 1,
    ('C', 'D'): 1,
    ('D', 'A'): 1,
    ('E', 'B'): 3
})

graph.bellman_ford('A', edge_order=[
    ('E', 'B'), ('C', 'D'), ('B', 'C'), ('A', 'B'),
    ('D', 'A')
])

graph.bellman_ford_neg_lazy('A', edge_order=[
    ('E', 'B'), ('C', 'D'), ('B', 'C'), ('A', 'B'),
    ('D', 'A')
])


graph.bellman_ford_neg('A', edge_order=[
    ('E', 'B'), ('C', 'D'), ('B', 'C'), ('A', 'B'),
    ('D', 'A')
])
