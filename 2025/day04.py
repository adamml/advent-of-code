do_test = False
part_one = False

test = []

if not do_test:
    file = open('/input/day04.txt')
    
    test = [line.rstrip() for line in file]
    print(test[0])
remove = 0
adj = 0

if part_one:

    for i, x in enumerate(test):
        for j, y in enumerate(x):
            if y == "@":
                adj = 0
                if i != 0:
                    if j!= 0:
                        if test[i-1][j-1] == '@':
                            adj += 1
                    if j != len(x)-1:
                        if test[i-1][j+1] == '@':
                          adj += 1
                    if test[i-1][j] == '@':
                        adj += 1
                if i != len(test)-1:
                    if j!= 0:
                        if test[i+1][j-1] == '@':
                            adj += 1
                    if j != len(x)-1:
                        if test[i+1][j+1] == '@':
                          adj += 1
                    if test[i+1][j] == '@':
                        adj += 1
                if j != 0:
                    if test[i][j-1] == '@':
                          adj += 1
                if j != len(x)-1:
                    if test[i][j+1] == '@':
                          adj += 1
                if adj < 4:
                    remove += 1

    print(remove)

else:
    tot_rem = 0
    remove = -1
    while remove !=0:
        remove = 0
        idc = []
        for i, x in enumerate(test):
            for j, y in enumerate(x):
                if y == "@":
                    adj = 0
                    if i != 0:
                        if j!= 0:
                            if test[i-1][j-1] == '@':
                                adj += 1
                        if j != len(x)-1:
                            if test[i-1][j+1] == '@':
                              adj += 1
                        if test[i-1][j] == '@':
                            adj += 1
                    if i != len(test)-1:
                        if j!= 0:
                            if test[i+1][j-1] == '@':
                                adj += 1
                        if j != len(x)-1:
                            if test[i+1][j+1] == '@':
                              adj += 1
                        if test[i+1][j] == '@':
                            adj += 1
                    if j != 0:
                        if test[i][j-1] == '@':
                              adj += 1
                    if j != len(x)-1:
                        if test[i][j+1] == '@':
                          adj += 1
                    if adj < 4:
                        remove += 1
                        idc.append([i, j])

        tot_rem += remove
        for ii in idc:
            test[ii[0]] = test[ii[0]][:ii[1]] + '.' + test[ii[0]][ii[1]+1:]
    print(tot_rem)
