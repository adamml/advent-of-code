draw = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
boards = [[[22,13,17,11,0],
[8 , 2 ,23 , 4 ,24],
[21  ,9 ,14, 16 , 7],
[6 ,10 , 3, 18,  5],
[1 ,12, 20 ,15, 19]],
[[3 ,15,  0 , 2, 22],
[9, 18, 13 ,17 , 5],
[19 , 8,  7, 25, 23],
[20 ,11, 10, 24 , 4],
[14 ,21, 16 ,12 , 6]],
[[14 ,21, 17 ,24,  4],
[10 ,16, 15 , 9, 19],
[18  ,8, 23, 26, 20],
[22 ,11, 13 , 6 , 5],
[2 , 0, 12 , 3 , 7]]]

with open('input', 'r') as f:
    raw_data = [x.replace('\n', '').split() for x in f.readlines()]
    boards = []
    draw = []
    this_board = -1
    current_board = []

    
    for i,x in enumerate(raw_data):
        if i == 0:
            draw = [int(x) for x in x[0].split(',')]
        else:
            if len(x):
                current_board.append(x)
            else:
                boards.append(current_board)
                current_board = []
    del(boards[0])
    boards = [[[int(x) for x in row] for row in board] for board in boards]


    winning_board = None
    winning_draw = None
    final_board = None
    final_draw = None
    finished_boards = None
    
    for d in draw:
        boards = [[[-1 if x == d else x for x in row] for row in b]for b in boards]
        row_sum = [[sum(row) for row in b] for b in boards]
        col_sum = [[sum(col) for col in zip(*b)] for b in boards]
        for i, rs in enumerate(row_sum):
            if -5 in rs:
                if winning_board is None:
                    winning_board = boards[i]
                    winning_draw = d
                    finished_boards = [i]
                if i not in finished_boards:
                    finished_boards.append(i)
                if len(finished_boards) == len(boards):
                    if final_board is None:
                       final_board = boards[i]
                       final_draw = d
        for i, rs in enumerate(col_sum):
            if -5 in rs:
                if winning_board is None:
                    winning_board = boards[i]
                    winning_draw = d
                    finished_boards = [i]
                if i not in finished_boards:
                    finished_boards.append(i)
                if len(finished_boards) == len(boards):
                    if final_board is None:
                       final_board = boards[i]
                       final_draw = d
           
    print(sum([sum(row) for row in [[0 if x==-1 else x for x in row] for row in winning_board]]) * winning_draw)
    print(sum([sum(row) for row in [[0 if x==-1 else x for x in row] for row in final_board]]) * final_draw)           
