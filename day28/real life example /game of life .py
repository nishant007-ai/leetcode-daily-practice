class Solution:
    def gameOfLife(self, board):
        rows, cols = len(board), len(board[0])
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                        live_neighbors += 1
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0


#Initial state:
#0 1 0
#0 0 1
#1 1 1
#0 0 0

#Generation 1:
#0 0 0
#1 0 1
#0 1 1
#0 1 0
