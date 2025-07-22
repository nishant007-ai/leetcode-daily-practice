class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # There are 9 boxes (3x3 grids)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                if val in rows[r]:
                    return False
                if val in cols[c]:
                    return False

                box_index = (r // 3) * 3 + (c // 3)
                if val in boxes[box_index]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        return True
