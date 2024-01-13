from PriorityQueue import MinHeapPriorityQueue as PriorityQueue
from CustomQueue import Queue


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

    def get_neighbors(self, node):
        neighbors = []
        for edge in self.edge_weights:
            v1, v2 = edge
            if v1 == node:
                neighbors.append(v2)

        return neighbors

    def show_distances(self, distance_map, turn=-1, node_order=None):
        if node_order is None:
            node_order = self.nodes

        data = ''
        if turn is not False:
            print(f'turn {turn}')

        for node in node_order:
            info = distance_map[node]
            data += f'{node}={info}, '

        print(data)

    def bellman_ford(self, source, edge_order=None, node_order=None):
        nodes = sorted(self.nodes)
        edges = sorted(list(self.edge_weights.keys()))
        if edge_order is None: edge_order = edges
        if node_order is None: node_order = nodes

        try:
            # ensure edge traversal order contains all edges
            assert sorted(edges) == sorted(edge_order)
        except AssertionError as e:
            print('BAD EDGES', sorted(edges), sorted(edge_order))
            raise e

        try:
            assert sorted(node_order) == sorted(nodes)
        except AssertionError as e:
            print('BAD NODES', sorted(nodes), sorted(node_order))
            raise e

        distances = {node: (float('inf'), None) for node in self.nodes}
        distances[source] = (0, None)

        self.show_distances(distances, 'INIT', node_order)

        for k in range(len(self.nodes)):
            for edge in self.edge_weights:
                start_node, end_node = edge
                distance, parent = distances[end_node]

                weight = self.edge_weights[edge]
                start_dist = distances[start_node][0]
                new_distance = start_dist + weight

                if new_distance < distance:
                    self.show_distances(distances, False, node_order)
                    print(
                        f'NEW {end_node}={new_distance}<{distance} '
                        f'{start_node}={start_dist} edge={edge} '
                        f'weight={weight}'
                    )
                    dist_info = (new_distance, start_node)
                    distances[end_node] = dist_info

            turn_info = f'{k+1} END'
            self.show_distances(distances, turn_info, node_order)

        self.show_distances(distances, 'END', node_order)
        return distances

    def bellman_ford_neg_lazy(
        self, source, edge_order=None, node_order=None
    ):
        nodes = sorted(self.nodes)
        edges = sorted(list(self.edge_weights.keys()))
        if edge_order is None: edge_order = edges
        if node_order is None: node_order = nodes

        distances = self.bellman_ford(
            source, edge_order, node_order=node_order
        )

        for edge in edge_order:
            start_node, end_node = edge
            distance, parent = distances[end_node]

            weight = self.edge_weights[edge]
            start_dist = distances[start_node][0]
            new_distance = start_dist + weight

            if new_distance < distance:
                dist_info = (float('-inf'), start_node)
                distances[end_node] = dist_info

        self.show_distances(distances, 'CHECK', node_order)

    @staticmethod
    def insert_all(queue: Queue, neighbors):
        for node in neighbors:
            queue.insert(node)

    def bellman_ford_neg(
        self, source, edge_order=None, node_order=None
    ):
        nodes = sorted(self.nodes)
        edges = sorted(list(self.edge_weights.keys()))
        if edge_order is None: edge_order = edges
        if node_order is None: node_order = nodes

        distances = self.bellman_ford(source, edge_order, node_order)
        unchecked_nodes: Queue = Queue()

        for edge in edge_order:
            start_node, end_node = edge
            distance, parent = distances[end_node]

            weight = self.edge_weights[edge]
            start_dist = distances[start_node][0]
            new_distance = start_dist + weight

            if distance > new_distance:
                dist_info = (float('-inf'), start_node)
                distances[end_node] = dist_info
                neighbors = self.get_neighbors(end_node)
                self.insert_all(unchecked_nodes, neighbors)

        self.show_distances(distances, 'CHECK', node_order)
        print('QUEUE', unchecked_nodes)

        while not unchecked_nodes.empty():
            print('QUEUE-', unchecked_nodes)
            node = unchecked_nodes.pop()
            distance, parent = distances[node]
            if distance == float('-inf'): continue
            neighbors = self.get_neighbors(node)
            self.insert_all(unchecked_nodes, neighbors)
            distances[node] = (float('-inf'), parent)

        self.show_distances(distances, 'NEG', node_order)

    def dijkstras(self, source, edge_order=None, node_order=None):
        nodes = sorted(self.nodes)
        edges = sorted(list(self.edge_weights.keys()))
        if edge_order is None: edge_order = edges
        if node_order is None: node_order = nodes

        try:
            # ensure edge traversal order contains all edges
            assert sorted(edges) == sorted(edge_order)
        except AssertionError as e:
            print('BAD EDGES', sorted(edges), sorted(edge_order))
            raise e

        try:
            assert sorted(node_order) == sorted(nodes)
        except AssertionError as e:
            print('BAD NODES', sorted(nodes), sorted(node_order))
            raise e

        inf_source = (float('inf'), None)
        distances = {node: inf_source for node in self.nodes}
        distances[source] = (0, None)
        node_queue = PriorityQueue({
            node: distances[node][0] for node in node_order
        })

        print(node_queue)
        self.show_distances(distances, 'INIT', node_order)

        while not node_queue.empty():
            node = node_queue.extract_min()
            # print(f'node = {node}, {node_order}')
            neighbors = self.get_neighbors(node)
            start_dist = distances[node][0]
            print(neighbors)

            for neighbor in neighbors:
                edge = (node, neighbor)
                weight = self.edge_weights[edge]
                distance, parent = distances[neighbor]
                new_distance = start_dist + weight
                # print(edge, start_dist, new_distance)

                if new_distance < distance:
                    # print('NEW', new_distance, distance, node, neighbor)
                    dist_info = (new_distance, node)
                    distances[neighbor] = dist_info
                    node_queue.decrease_priority(
                        neighbor, new_distance
                    )

            print(node_queue)
            self.show_distances(distances, node, node_order)

        self.show_distances(distances, 'END', node_order)
        return distances


if __name__ == '__main__':
    graph = WeightedGraph(edge_weights={
        ('A', 'B'): 6,
        ('A', 'E'): 2,
        ('B', 'D'): 3,
        ('B', 'E'): -2,
        ('C', 'B'): 2,  # test (2, -1)
        ('D', 'C'): -1,
        ('E', 'D'): 2
    })

    graph.bellman_ford('A', edge_order=[
        ('A', 'B'), ('A', 'E'), ('B', 'D'), ('B', 'E'),
        ('C', 'B'), ('D', 'C'), ('E', 'D')
    ], node_order=[
        'A', 'B', 'C', 'D', 'E'
    ])