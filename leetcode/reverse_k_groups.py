from typing import Optional

from merge_k_lists import ListNode

SHOW = True

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def mprint(*args, **kwargs) -> None:
    if SHOW is True:
        print(args, **kwargs)


def reverse_list(start_node, end_node):
    next_start = end_node.next

    node = start_node
    new_head = new_tail = node
    node_ids = set()
    # r_nodes = []
    prev_node = None

    while node is not end_node:
        node_id = id(node)
        assert node_id not in node_ids
        node_ids.add(node_id)

        next_node = node.next
        assert node.next is not node
        # r_nodes = [node] + r_nodes

        new_head = node
        new_head.next = prev_node

        prev_node = node
        node = next_node

    new_head = node
    new_head.next = prev_node
    # r_nodes = [node] + r_nodes

    new_tail.next = next_start
    assert new_head == end_node
    return new_head, new_tail


class Solution:
    def reverseKGroup(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        # node before first node that is being reversed in chain
        reverse_pre_head = None
        # first node that is being reversed in chain
        reverse_start_head = head
        iterations = 0

        prev_node = None
        node = head
        new_start_head = None
        node_ids = set()

        while node is not None:
            print_head = head if new_start_head is None else new_start_head
            # mprint(k, print_head.to_list(), reverse_start_head, node)

            iterations += 1
            freeze_node = node
            next_node = node.next

            node_id = id(node)
            assert node_id not in node_ids
            node_ids.add(node_id)

            if iterations == k:
                mprint('REVERSING', k, iterations)
                # prev_node.next = None
                new_head, new_tail = reverse_list(reverse_start_head, node)
                mprint('NEW-HEAD-TAIL', (prev_node, new_head, new_tail, next_node))

                if new_start_head is None:
                    new_start_head = new_head
                    mprint('NEW_START_HEAD', new_start_head)
                else:
                    reverse_pre_head.next = new_head
                    reverse_pre_head = new_tail

                reverse_pre_head = new_tail
                reverse_start_head = next_node
                new_tail.next = next_node
                iterations = 0

                # mprint('POST-REVERSE', new_start_head.to_list(), reverse_start_head, node)
                prev_node = new_tail
            else:
                prev_node = freeze_node

            node = next_node

        return new_start_head


if __name__ == "__main__":
    soln = Solution()
    raw_data = [1, 2, 3, 4, 5]
    reverse_length = 3

    start_head = head = ListNode(raw_data[0])
    for k in range(1, len(raw_data)):
        head.next = ListNode(raw_data[k])
        head = head.next

    result = soln.reverseKGroup(start_head, k=reverse_length)
    print('RESULT', result.to_list())
