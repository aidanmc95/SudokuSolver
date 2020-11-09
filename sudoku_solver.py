class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def validBoard(self):
        rows  = [set() for _ in range(9)]
        cols  = [set() for _ in range(9)]
        dices = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                e = self.board[i][j]
                if e == 0: 
                    continue
                if e in rows[i] or e in cols[j] or e in dices[i//3][j//3]: 
                    return False
                rows[i].add(e)
                cols[j].add(e)
                dices[i//3][j//3].add(e)
        return True

    def checkValid(self,input_value,x,y):
        x_start = (x // 3) * 3
        y_start = (y // 3) * 3
        for i in range(9):
            x_axis = x_start + i % 3
            y_axis = y_start + i // 3
            if(x >= 9 or y >= 9 or input_value == self.board[y][i] or input_value == self.board[i][x] or input_value == self.board[y_axis][x_axis]):
                return False
        return True

    def printSolution(self):
        '''
            A utility function to print Chessboard matrix
        '''
        for i in range(9):
            for j in range(9):
                print(self.board[i][j], end=' ')
            print()

    def solveSudoku(self):
        if(not self.validBoard()):
            print('Not Valid Sudoku')
            return
        if(not self.solveSudokuUtil(0, 0)):
            print("Solution does not exist")
        else:
            self.printSolution()

    def solveSudokuUtil(curr_x, curr_y):
        if(curr_x > 8 or curr_y > 8):
            return True

        if(curr_x < 8):
            new_x = curr_x + 1
            new_y = curr_y
        else:
            new_x = 0
            new_y = curr_y + 1
        
        if(self.board[curr_y][curr_x] != 0):
            if(self.solveSudokuUtil(new_x, new_y)):
                return True
        else:
            for i in range(9):
                if(self.checkValid(i+1, curr_x, curr_y)):
                    self.board[curr_y][curr_x] = i+1
                    if(self.solveSudokuUtil(new_x, new_y)):
                        return True
                    self.board[curr_y][curr_x] = 0
        return False