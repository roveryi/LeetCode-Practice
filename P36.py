'''
36. Valid Sudoku
Medium

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row = [int(j) for j in board[i] if j != '.']
            if len(row) == 0: continue
            if len(set(row)) != len(row) or max(row) > 9 or min(row) < 1: return False
            
        for i in range(9):
            col = [int(board[j][i]) for j in range(9) if board[j][i] != '.']
            if len(col) == 0: continue
            if len(set(col)) != len(col) or max(col) > 9 or min(col) < 1: return False
            
        for p in [1,4,7]:
            for q in [1,4,7]:
                s = [int(board[j][i]) for j in range(p-1,p+2) for i in range(q-1, q+2) if board[j][i] != '.']
                if len(s) == 0: continue
                if len(set(s)) != len(s) or max(s) > 9 or min(s) < 1: return False
        
        return True
            