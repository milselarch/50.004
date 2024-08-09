from typing import List, Tuple, Dict, Set, Deque
from collections import deque

OFFSETS = ((1, 0), (-1, 0), (0, 1), (0, -1))


class Solution:
    def BFS(
        self, coord, heights: List[List[int]],
        pacific_flows: List[List[int]], atlantic_flows: List[List[int]],
        explored: List[List[int]]
    ):
        flow_coords = set()
        breadth, width = len(heights), len(heights[0])
        is_pacific, is_atlantic = False, False
        queue = deque([coord])

        while len(queue) != 0:
            y, x = coord = queue.popleft()
            flow_coords.add(coord)
            height = heights[y][x]
            explored[y][x] = 1

            if (x == 0) or (y == 0):
                is_pacific = True
            if (x == width - 1) or (y == breadth - 1):
                is_atlantic = True

            for dy, dx in OFFSETS:
                y2, x2 = new_coord = (y + dy, x + dx)
                if (y2 < 0) or (y2 >= breadth):
                    continue
                if (x2 < 0) or (x2 >= width):
                    continue

                if explored[y2][x2] == 1:
                    is_pacific |= pacific_flows[y2][x2]
                    is_atlantic |= atlantic_flows[y2][x2]
                    continue

                new_height = heights[y2][x2]
                if new_height <= height:
                    queue.append(new_coord)

        return flow_coords, is_pacific, is_atlantic

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        breadth, width = len(heights), len(heights[0])

        explored = [[0 for x in range(width)] for y in range(breadth)]
        flows_pacific = [[0 for x in range(width)] for y in range(breadth)]
        flows_atlantic = [[0 for x in range(width)] for y in range(breadth)]
        coords = []

        for y in range(breadth):
            for x in range(width):
                coords.append((y, x))

        # sort coords from lowest to highest
        coords = sorted(coords, key=lambda pos: heights[pos[0]][pos[1]])
        queue = deque(coords)

        while len(queue) > 0:
            y, x = coord = queue.popleft()
            # print('COORD', coord)
            if explored[y][x] == 1:
                continue

            flow_coords, is_pacific, is_atlantic = self.BFS(
                coord, heights, pacific_flows=flows_pacific,
                atlantic_flows=flows_atlantic, explored=explored
            )

            # print('FLOW_COORDS', coord, flow_coords, is_pacific, is_atlantic)
            # all flow coordinates here are at the same height
            for fy, fx in flow_coords:
                flows_pacific[fy][fx] = is_pacific
                flows_atlantic[fy][fx] = is_atlantic
                explored[fy][fx] = 1

        both_grid_coords = []
        for y in range(breadth):
            for x in range(width):
                if flows_pacific[y][x] and flows_atlantic[y][x]:
                    both_grid_coords.append([y, x])

        return both_grid_coords


if __name__ == '__main__':
    # expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    test_heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    solution = Solution()
    result = solution.pacificAtlantic(test_heights)
    print('RESULT', result)
