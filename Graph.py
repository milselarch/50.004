
class WeightedGraph(object):
    def __init__(self, edge_weights: dict, nodes=None):
        if nodes is None:
            nodes, added_edges = [], []

            for edge in edge_weights:
                assert edge not in added_edges
                added_edges.append(edge)
                v1, v2 = edge

                if v1 not in nodes:
                    nodes.append(v1)
                if v2 not in nodes:
                    nodes.append(v2)

        self.nodes = nodes
        self.edge_weights = edge_weights

    def get_weight(self, vertex1, vertex2):
        edge = vertex1, vertex2
        return self.edge_weights[edge]

    def bellman_ford(self, source, edge_order=None):
        edges = sorted(list(self.edge_weights.keys()))
        if edge_order is None:
            edge_order = edges

        try:
            # ensure edge traversal order contains all edges
            assert sorted(edges) == sorted(edge_order)
        except AssertionError as e:
            print('BAD EDGES', sorted(edges), sorted(edge_order))
            raise e

        distances = {node: (float('inf'), None) for node in self.nodes}
        distances[source] = (0, None)

        def show_distances(distance_map, turn=-1):
            data = ''
            print(f'turn {turn}')
            for node in self.nodes:
                info = distance_map[node]
                data += f'{node}={info}, '

            print(data)

        show_distances(distances, 'INIT')

        for k in range(len(self.nodes) + 1):
            for edge in self.edge_weights:
                start_node, end_node = edge
                distance, parent = distances[end_node]

                weight = self.edge_weights[edge]
                start_dist = distances[start_node][0]
                new_distance = start_dist + weight

                if new_distance < distance:
                    dist_info = (new_distance, start_node)
                    distances[end_node] = dist_info

            show_distances(distances, k + 1)

        show_distances(distances, 'END')


if __name__ == '__main__':
    graph = WeightedGraph(edge_weights={
        ('A', 'B'): 6,
        ('A', 'E'): 2,
        ('B', 'D'): 3,
        ('B', 'E'): -2,
        ('C', 'B'): -1,  # 2
        ('D', 'C'): -1,
        ('E', 'D'): 2
    })

    graph.bellman_ford('A', edge_order=[
        ('A', 'B'), ('A', 'E'), ('B', 'D'), ('B', 'E'),
        ('C', 'B'), ('D', 'C'), ('E', 'D')
    ])