a = []

def show_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('-----------')

        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print('|', end='')
            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end='')

def solve_board(board):
    if find_space(board):
        x, y = find_space(board)
    else:
        return True

    for i in range(1,10):
        if check_availability(board, x, y, i):
            board[x][y] = i
            if solve_board(board):
                return True
            board[x][y] = 0
           
    return False

def check_availability(board, x, y, num):
    # Check row
    for a in range(len(board)):
        if num == board[x][a] and a != y:
            return False
    # Check column
    for b in range(len(board)):
        if num == board[b][y] and b != x:
            return False

    # Check block
    i = (y // 3) * 3
    j = (x // 3) * 3
    for d in range(i,i+3):
        for c in range(j, j+3):
            if num == board[c][d] and (c,d) != (i,j):
                # print(num, 'is in block', i,j)
                return False

    return True


def find_space(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i,j
    return False


def nums_of_answer(board):
    if find_space(board):
        x, y = find_space(board)
    else:
        a.append(1)
        return

    for i in range(1,10):
        if check_availability(board, x, y, i):
            board[x][y] = i
            nums_of_answer(board)
            board[x][y] = 0
          
    return False


def find_num_of_answer(board):
    nums_of_answer(board)
    answer = len(a)
    a.clear()
    return answer




