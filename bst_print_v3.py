import random

from BST import BST
from random import randint

# Question 4ii solution
def traverse_bst_in_order(T: BST):
    # require that T be a BST, and have no duplicate values
    size = T.size
    node = T.root
    current_max = None
    nodes = []

    while node is not None:
        no_descend_left = (
            (current_max is not None) and
            (node.left is not None) and
            (current_max >= node.left.value)
        )

        no_descend_right = (
            (current_max is not None) and
            (node.right is not None) and
            (current_max >= node.right.value)
        )

        parent = node.parent
        is_leaf = (
            (node.left is None) and (node.right is None)
        )

        if is_leaf:
            # print then ascend from leaf node
            print(node.value)
            nodes.append(node)

            if current_max is None:
                current_max = node.value
            else:
                current_max = max(node.value, current_max)

            size -= 1
            node = parent
            continue

        if (node.left is not None) and not no_descend_left:
            # go down to left child
            node = node.left
            continue

        if (node.right is not None) and not no_descend_right:
            # print then go down to right child
            print(node.value)
            nodes.append(node)

            current_max = node.value
            node = node.right
            size -= 1
            continue

        if (current_max is not None) and (node.value > current_max):
            # print then traverse up from left path
            print(node.value)
            nodes.append(node)

            current_max = node.value
            size -= 1
        else:
            # traverse up from right path
            pass

        node = parent

    return nodes


if __name__ == '__main__':
    # a = BST([8, 3, 10, 1, 6, 14, 4, 7, 13])
    random.seed(234)
    elements = [randint(0, 100) for k in range(25)]
    elements = list(dict.fromkeys(elements))
    a = BST(elements)
    a.show()

    print('')
    nodes = traverse_bst_in_order(a)
    vals = [node.value for node in nodes]
    print(nodes)
    print(vals)
    print(sorted(elements))

    assert vals == sorted(elements)
