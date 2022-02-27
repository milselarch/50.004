from BST import BST, Node
from overrides import overrides

class AVL(BST):
    def __init__(self, values):
        super(AVL, self).__init__(values)

    @overrides
    def add_node(self, value):
        if self.root is None:
            super().add_node(value)
            assert self.root is not None
        else:
            # node = Node(value)
            print('add value', value)
            self.root = self.insert(value, self.root)

        self.show()
        print('')

    def rebalance(self, root, value):
        balance = root.balance
        # value = root.value
        # print('root balance', root, root.balance)

        if (balance > 1) and (value < root.left.value):
            print('rotate 1')
            self.show()
            print('')
            return self.right_rotate(root)
        if (balance < -1) and (value > root.right.value):
            print('rotate 2')
            self.show()
            print('')
            return self.left_rotate(root)
        if (balance > 1) and (value > root.left.value):
            print('rotate 3')
            self.show()
            print('')
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if (balance < -1) and (value < root.right.value):
            print('rotate 4')
            self.show()
            print('')
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        else:
            return root

    def insert(self, value, root=None):
        if root is None:
            return Node(value)
        elif value < root.value:
            new_node = self.insert(value, root.left)
            new_node.parent = root
            root.left = new_node
        else:
            new_node = self.insert(value, root.right)
            new_node.parent = root
            root.right = new_node

        return self.rebalance(root, value)

    def left_rotate(self, z: Node):
        print('left rotate start', z)
        self.show()

        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        print('left rotate end', z)
        self.show()
        return y

    def right_rotate(self, z: Node):
        print('right rotate start', z)
        self.show()

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        print('right rotate end', z)
        self.show()
        return y
