import copy

from typing import List, Tuple, Dict, Set, Deque

from collections import deque

OFFSETS = ((1, 0), (-1, 0), (0, 1), (0, -1))


class Solution:
    def solve(self, board: List[List[str]]):
        """
        Do not return anything, modify board in-place instead.
        """
        height, width = len(board), len(board[0])
        coords = []

        for y in range(height):
            for x in range(width):
                coord = (y, x)
                if board[y][x] == 'O':
                    coords.append(coord)

        coords = sorted(coords, key=lambda pos: min(
            pos[0], pos[1], width - pos[1] - 1, height - pos[0] - 1
        ))

        # print('COORDS', coords)
        protected_coords = set()
        queue = deque(coords)

        while len(queue) > 0:
            y, x = coord = queue.popleft()

            for offset in OFFSETS:
                fy, fx = neighbor_coord = (y + offset[0], x + offset[1])
                is_protected = (
                    (y == 0) or (x == 0) or
                    (y == height - 1) or (x == width - 1) or
                    neighbor_coord in protected_coords
                )

                if is_protected:
                    protected_coords.add(coord)

        for y in range(height):
            for x in range(width):
                coord = (y, x)
                if coord not in protected_coords:
                    board[y][x] = 'X'

        return board


if __name__ == '__main__':
    test_board = [
        ["O", "X", "X", "O", "X"], ["X", "O", "O", "X", "O"],
        ["X", "O", "X", "O", "X"], ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"]
    ]

    def print_board(board):
        print('\n'.join([''.join(row) for row in board]))

    print_board(test_board)
    print('START_SOLVE')

    solution = Solution()
    solved_board = copy.deepcopy(test_board)
    solution.solve(solved_board)
    print_board(solved_board)

