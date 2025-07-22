class Solution:
    def isValidSudoku (self,boerd):

        rows = [set()for _in range (9)]
        cols = [set()for _in range(9)]
        boxes = [set()for _ in range(9)]


        for r in range(9):
            for c in range (9):
                val = board[r][c]


                if val == "":
                   
                   continue


                if val in rows[r]:
                    return False
                

                if val in cols[c]:
                    return False
                

                

                n = (r//3)*3+(c//3)
                for val in boxes[n]:
                    return False
                

                rows[r].add(val)
                cols[c].add(val)

                boxes[n].add(val)


        return true        
                

