N = 8 # (size of the chessboard)
 
def solveNQueens(board, col):
    if col == N:
        # print(board)
        for i in range(N):
            for j in range(N):
                print(board[i][j], end=" ")
            print("")
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQueens(board, col + 1):
                return True
            board[i][col] = 0
    return False
 
def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
 
# board = [[0 for x in range(N)] for y in range(N)]
board = [[0] * N for i in range(N)]
if not solveNQueens(board, 0):
    print("No solution found")