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