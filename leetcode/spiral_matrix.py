import itertools

from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, r_start: int, c_start: int) -> List[List[int]]:
        direction = (0, 1)

        uncovered_coords = set()
        combinations = itertools.product(range(rows), range(cols))
        for row, col in combinations:
            uncovered_coords.add((row, col))

        path = []
        current_coord = (r_start, c_start)
        transitions = 1
        lifetime = 1

        while len(uncovered_coords) > 0:
            print('COORD', current_coord)
            if current_coord in uncovered_coords:
                uncovered_coords.remove(current_coord)
                path.append(current_coord)

            lifetime -= 1
            new_coord = (
                current_coord[0] + direction[0],
                current_coord[1] + direction[1]
            )

            if lifetime == 0:
                if direction == (0, 1):
                    new_dir = (1, 0)
                elif direction == (1, 0):
                    transitions += 1
                    new_dir = (0, -1)
                elif direction == (0, -1):
                    new_dir = (-1, 0)
                elif direction == (-1, 0):
                    transitions += 1
                    new_dir = (0, 1)
                else:
                    raise ValueError("Invalid direction")

                lifetime = transitions
                direction = new_dir

            current_coord = new_coord

        return path


if __name__ == '__main__':
    solution = Solution()
    rows = 5
    cols = 6
    r_start = 1
    c_start = 4
    ans = solution.spiralMatrixIII(rows, cols, r_start, c_start)
    print('ANS', ans)