# Python3 program to solve Soduku problem using Backtracking
 
# Sudoku board Size
n = 9

def checkValid(input_value,x,y,board):
    # # check spot
    # if(board[y][x] != 0):
    #     return False
    # # check row
    # for(i in range(9)):
    #     if(input_value == board[y][i]):
    #         return False
    # # check column
    # for(i in range(9)):
    #     if(input_value == board[i][x]):
    #         return False
    # # check 3x3 section
    #     # x spots
    #     # y spots
    # x_start = (x / 3) * 3
    # y_start = (y / 3) * 3
    # for(i in range(3)):
    #     x_axis = x_start + i % 3
    #     y_axis = y_start + i / 3
    #     if(input_value == board[y_axis][x_axis]):
    #         return False
    # combined solution
    # logger.debug("Input Value: {}, X Value: {}, Y Value: {}".format(input_value,x,y))
    x_start = (x // 3) * 3
    y_start = (y // 3) * 3
    for i in range(9):
        x_axis = x_start + i % 3
        y_axis = y_start + i // 3
        if(x >= 9 or y >= 9 or input_value == board[y][i] or input_value == board[i][x] or input_value == board[y_axis][x_axis]):
            return False
    return True

def printSolution(board):
    '''
        A utility function to print Chessboard matrix
    '''
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=' ')
        print()

def solveSudoku(board):
    if(not solveSudokuUtil(board, 0, 0)):
        print("Solution does not exist")
    else:
        printSolution(board)

def solveSudokuUtil(board, curr_x, curr_y):
    if(curr_x > 8 or curr_y > 8):
        return True

    if(curr_x < 8):
        new_x = curr_x + 1
        new_y = curr_y
    else:
        new_x = 0
        new_y = curr_y + 1
    
    if(board[curr_y][curr_x] != 0):
        if(solveSudokuUtil(board, new_x, new_y)):
            return True
    else:
        for i in range(9):
            if(checkValid(i+1, curr_x, curr_y, board)):
                board[curr_y][curr_x] = i+1
                if(solveSudokuUtil(board, new_x, new_y)):
                    return True
                board[curr_y][curr_x] = 0
    return False

# Driver Code
if __name__ == "__main__":
    board = [[0 for i in range(n)]for i in range(n)]
    board[0][0] = 1
    # Function Call
    printSolution(board)
    solveSudoku(board)