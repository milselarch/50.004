import random

from random import randint
from BST import BST

def print_if(cond, *args, **kwargs):
    if cond:
        print(*args, **kwargs)


def traverse_bst_in_order(T: BST, show=False):
    size = T.size
    node = T.root
    current_max = None
    values = []
    steps = 0

    while node is not None:
        steps += 1
        parent = node.parent
        is_leaf = (
            (node.left is None) and (node.right is None)
        )

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

        if is_leaf:
            print_if(show, 'LEAF REACH', node, current_max)
            print_if(show, node.value)
            values.append(node.value)

            if current_max is None:
                current_max = node.value
            else:
                current_max = max(node.value, current_max)

            size -= 1
            node = parent
            continue

        if (node.left is not None) and not no_descend_left:
            print_if(show, 'GO LEFT', node, current_max)
            node = node.left
            continue

        if (node.right is not None) and not no_descend_right:
            print_if(show, 'GO RIGHT', node, current_max)
            print_if(show, node.value)
            values.append(node.value)

            current_max = node.value
            node = node.right
            size -= 1
            continue

        if (current_max is not None) and (node.value > current_max):
            print_if(show, 'LEFT JUMP UP', node, current_max)
            print_if(show, node.value)
            current_max = node.value
            values.append(node.value)
            size -= 1
        else:
            print_if(show, 'RIGHT JUMP UP', node, current_max)
            # traversing up right
            pass

        node = parent

    print('steps taken', steps)
    return values


"""
In a Binary Search Tree (BST), all keys in left subtree of
a key must be smaller and all keys in right subtree must be greater. 
So a Binary Search Tree by definition has distinct keys and 
duplicates in binary search tree are not allowed
"""

if __name__ == '__main__':
    # a = BST([8, 3, 10, 1, 6, 14, 4, 7, 13])
    random.seed(234)
    elements = [randint(0, 100) for k in range(25)]
    elements = list(dict.fromkeys(elements))
    a = BST(elements)
    a.show()

    print('')
    vals = traverse_bst_in_order(a, show=True)
    print(vals)
    print(sorted(elements))

    assert vals == sorted(elements)
