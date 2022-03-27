from library import *


class NaivePriorityQueue(object):
    def __init__(self, priorities: dict):
        assert isinstance(priorities, dict)
        self.priorities = priorities

    def add_with_priority(self, node, priority):
        self.priorities[node] = priority

    def decrease_priority(self, node, priority):
        assert priority <= self.priorities[node]
        self.priorities[node] = priority

    def remove_node(self, node):
        del self.priorities[node]

    def __len__(self):
        return len(self.priorities)

    def __repr__(self):
        name = self.__class__.__name__
        return f'{name}({self.priorities})'

    def empty(self):
        return len(self) == 0

    def extract_min(self):
        min_node = list(self.priorities.keys())[0]
        min_priority = float('inf')

        for node in self.priorities:
            priority = self.priorities[node]
            if priority < min_priority:
                min_priority = priority
                min_node = node

        del self.priorities[min_node]
        return min_node


class MinHeapPriorityQueue(object):
    def __init__(self, priorities: dict):
        self.priorities = priorities
        self.node_index_map = {}
        self.index_node_map = {}
        self.heap = Array()

        self.heap.disable_negative_indexing()
        for node in priorities:
            assert type(node) is not int
            priority = priorities[node]
            self.heap_insert(node, priority)

    def __len__(self):
        return len(self.heap)

    def empty(self):
        return len(self) == 0

    def swap_index(self, index1, index2):
        node1 = self.index_node_map[index1]
        node2 = self.index_node_map[index2]

        self.index_node_map[index1] = node2
        self.index_node_map[index2] = node1
        self.node_index_map[node1] = index2
        self.node_index_map[node2] = index1
        self.heap[index1], self.heap[index2] = (
            self.heap[index2], self.heap[index1]
        )

    def heap_nodes(self):
        # print('II', self.index_node_map)
        keys = sorted(list(self.index_node_map.keys()))
        return [
            self.index_node_map[key] for key in keys
            if key <= len(self)
        ]

    def __repr__(self):
        name = self.__class__.__name__
        return f'{name}({self.heap_nodes()}, {self.priorities})'

    def __getitem__(self, index):
        if type(index) is int:
            node = self.index_node_map[index]
        else:
            node = index

        return self.priorities[node]

    def add_with_priority(self, name, priority):
        self.heap_insert(name, priority)

    def decrease_priority(self, node, priority):
        # print("PP", self.priorities)
        self.priorities[node] = priority
        index = self.node_index_map[node]
        if index <= len(self.heap):
            self.heap[index] = priority

        # print('E-PRE HEAPIFY', self.heap, self.heap_nodes())
        self.heap_shift_up(index)
        # print('E-POS HEAPIFY', self.heap, self.heap_nodes())

    def extract_min(self):
        index = len(self)
        self.swap_index(1, index)
        node = self.index_node_map[index]
        self.heap.pop()

        # del self.index_node_map[index]
        # del self.node_index_map[node]
        # print('PRE HEAPIFY', self.heap)
        self.min_heapify(1)
        # print('POST HEAPIFY', self.heap)
        return node

    def min_heapify(self, index):
        # print('HEAPIFY', index, self.index_node_map[index])

        while True:
            c1, c2 = self.children(index)
            min_child_index, min_value = None, self[index]
            """
            print(
                '~HEAPIFY', index, self.index_node_map[index],
                self.index_node_map.get(c1, None),
                self.index_node_map.get(c2, None),
                self.priorities
            )
            """

            if c1 <= len(self):
                if self[c1] < min_value:
                    min_value = self[c1]
                    min_child_index = c1

            if c2 <= len(self):
                if self[c2] < min_value:
                    min_value = self[c2]
                    min_child_index = c2

            if min_child_index is not None:
                self.swap_index(index, min_child_index)
                index = min_child_index
            else:
                break

    def heap_shift_up(self, index):
        priority = self[index]

        while index != 1:
            parent_index = self.parent(index)

            if priority < self[parent_index]:
                self.swap_index(index, parent_index)
                index = parent_index
            else:
                break

    def heap_insert(self, node, priority):
        self.priorities[node] = priority
        self.heap.append(priority)
        index = len(self.heap)

        assert node not in self.node_index_map
        assert index not in self.index_node_map
        self.node_index_map[node] = index
        self.index_node_map[index] = node
        self.heap_shift_up(index)

    @staticmethod
    def children(index):
        return index * 2, index * 2 + 1

    @staticmethod
    def parent(index):
        return index // 2