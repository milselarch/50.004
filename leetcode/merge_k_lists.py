"""
sort by linked list index to get sort indices
map sort_indices 
"""

from collections import deque
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_str(self):
        next_str = None if self.next is None else self.next.to_str()
        pair = f'({self.val}, {next_str})'
        return self.__class__.__name__ + pair

    def __repr__(self):
        return self.__class__.__name__ + f'({self.val})'

    def to_list(self):
        items = []
        head = self

        while head is not None:
            items.append(head.val)
            head = head.next

        return items


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merge_nodes = []

        multi_links = []
        for linked_list in lists:
            if linked_list is None:
                continue

            multi_links.append(linked_list)

        sort_links = sorted(multi_links, key=lambda x: x.val)
        sort_links = deque(sort_links)

        while len(sort_links) > 0:
            lowest_node = sort_links.popleft()
            merge_nodes.append(lowest_node)
            next_node = lowest_node.next

            if next_node is not None:
                l_index, r_index = 0, len(sort_links) - 1

                if len(sort_links) == 0:
                    sort_links.append(next_node)
                elif next_node.val < sort_links[0].val:
                    sort_links.insert(0, next_node)
                elif next_node.val > sort_links[-1].val:
                    sort_links.append(next_node)
                else:
                    while l_index < r_index - 1:
                        mid = (l_index + r_index) // 2

                        if sort_links[mid].val < next_node.val:
                            l_index = mid
                        else:
                            r_index = mid

                    sort_links.insert(r_index, next_node)

        for k in range(len(merge_nodes) - 1):
            merge_nodes[k].next = merge_nodes[k + 1]

        if len(merge_nodes) > 0:
            merge_nodes[-1].next = None
            return merge_nodes[0]
        else:
            return None


if __name__ == '__main__':
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

    linked_lists = []
    for list_data in lists:
        start_head = ListNode(list_data[0])
        head = start_head

        for k in range(1, len(list_data)):
            element = list_data[k]
            print(element)
            node = ListNode(element)
            head.next = node
            head = node

        linked_lists.append(start_head)

    soln = Solution()
    merged_list = soln.mergeKLists(linked_lists)

    print(merged_list.to_list())
    # print(linked_lists)
