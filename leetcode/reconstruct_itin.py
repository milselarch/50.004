from typing import List, Dict
from collections import defaultdict

class Solution:
    def build_itin(
        self, tickets, src_ticket_map, path=None, taken_indices=None
    ):
        path = [] if path is None else path
        taken_indices = set() if taken_indices is None else taken_indices

        # print(path, len(tickets) + 1)
        if len(path) == len(tickets) + 1:
            # print('SOLVED', path)
            return path

        if len(path) == 0:
            dest_indices = src_ticket_map['JFK']

            for dest_idx in dest_indices:
                dest = tickets[dest_idx][1]
                result = self.build_itin(
                    tickets=tickets, src_ticket_map=src_ticket_map,
                    path=['JFK', dest], taken_indices={dest_idx}
                )

                if result is not None:
                    return result
        else:
            src = path[-1]
            dest_indices = src_ticket_map[src]

            for dest_idx in dest_indices:
                if dest_idx in taken_indices:
                    continue

                dest = tickets[dest_idx][1]

                path.append(dest)
                taken_indices.add(dest_idx)

                result = self.build_itin(
                    tickets=tickets, src_ticket_map=src_ticket_map,
                    path=path, taken_indices=taken_indices
                )

                if result is not None:
                    return result

                path.pop()
                taken_indices.remove(dest_idx)

        return None

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets = sorted(tickets, key=lambda ticket: ticket[1])
        src_ticket_map = defaultdict(list)

        for k, ticket in enumerate(tickets):
            src, dest = ticket
            src_ticket_map[src].append(k)

        for ticket in src_ticket_map:
           src_ticket_map[ticket] = src_ticket_map[ticket][::-1]

        return self.build_itin(
            tickets=tickets, src_ticket_map=src_ticket_map
        )


if __name__ == '__main__':
    solution = Solution()
    input_tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    ans = solution.findItinerary(input_tickets)
    print('RESULT', ans)
