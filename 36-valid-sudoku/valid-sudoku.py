class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows=len(board)
        cols=len(board[0])

        for i in range(rows):
            store = dict()
            for j in range(cols):

                if board[i][j] == ".":
                    continue

                if board[i][j] in store:
                    return False

            
                store[board[i][j]] = 1  
        
        for i in range(cols):
            store2=dict()
            for j in range(rows):

                if board[j][i] == ".":
                    continue

                if board[j][i] in store2:
                    return False

                
                store2[board[j][i]] = 1

        for i in range(0,9,3):
            for j in range(0,9,3):

                store3={}

                for x in range(i,i+3):
                    for y in range(j,j+3):
                        if board[x][y] == ".":
                            continue

                        if board[x][y] in store3:
                            return False

                        store3[board[x][y]]=1

        return True