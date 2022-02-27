from BST import BST

def print_bst_in_order(T: BST):
    size = T.size
    node = T.root
    current_max = None

    while (node is not None) and (size > 0):
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

        if (node.left is not None) and not no_descend_left:
            # print('GO LEFT', node, current_max)
            node = node.left
            continue

        if (node.right is not None) and not no_descend_right:
            # print('GO RIGHT', node, current_max)
            print(node.value)

            current_max = node.value
            node = node.right
            size -= 1
            continue

        if (node.left is None) and (node.right is None):
            # print('PARENT JUMP', node, current_max)

            if parent.right != node:
                # print('PARENT MAX', node, current_max)
                print(node.value)
                current_max = node.value
                size -= 1

            elif node.parent.value >= current_max:
                # print('LAST RIGHT CHILD', node)
                print(node.value)
                current_max = node.value
                size -= 1

        elif (current_max is not None) and (node.value > current_max):
            # print('UNKNOWN', node, current_max)
            current_max = node.value
            print(node.value)
            size -= 1

        node = parent


if __name__ == '__main__':
    a = BST([8, 3, 10, 1, 6, 14, 4, 7, 13])
    a.show()
    print_bst_in_order(a)
