class Solution:
    def convert(self, s, numRows):

        rows = [''] * numRows
        current_row = 0
        going_down = False

        if numRows == 1 or numRows >= len(s):
            return s

        

        for i in s:
            rows[current_row] += i
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        return ''.join(rows)
