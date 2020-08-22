import random

from utilities import check_availability, show_board, solve_board, find_num_of_answer


def add(n):
    template = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    count = 0
    all = []
    for i in range(0, 9):
        for j in range(0, 9):
            all.append((i, j))
    while count != n:
        x = random.randint(0, len(all) - 1)
        i = all[x][0]
        j = all[x][1]
        # print(all)
        for num in range(1,10):

            if check_availability(template, i, j, num):
                template[i][j] = num
                all.remove(all[x])
                count += 1
                break

            if num == 9:
                print('num= ', num)
                all.remove(all[x])

    return template


def create_complete():

    complete_board = add(10)
    if solve_board(complete_board):
        return complete_board
    else:
        create_complete()


def create_sudoku(number_of_gaps):
    try:
        complete_board = create_complete()
        # show_board(complete_board)
        all = []
        count = 0
        for i in range(0, 9):
            for j in range(0, 9):
                all.append((i, j))

        while count != number_of_gaps:
            possibility = 0
            x = random.randint(0, len(all) - 1)
            i = all[x][0]
            j = all[x][1]

            backup = complete_board[i][j]
            complete_board[i][j] = 0

            for num in range(1, 10):
                if check_availability(complete_board, i, j, num):
                    possibility += 1

            if possibility == 1:
                count += 1
            else:
                complete_board[i][j] = backup

            all.remove(all[x])

            if len(all) == 0:
                create_sudoku(number_of_gaps)

        return complete_board
    except ValueError:
        create_sudoku(number_of_gaps)





