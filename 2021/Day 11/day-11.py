test = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

test = [[int(y) for y in x] for x in test.split("\n")]

with open("input.txt") as f:
    data = [[int (y) for y in x.replace("\n", "")] for x in f.readlines()]

ipt = data

flash_count = 0

for i in range(1,101):
    ipt = [[y+1 for y in x] for x in ipt]
    while 10 in [y for x in ipt for y in x]:
        for ir, r in enumerate(ipt):
            for ic,c in enumerate(r):
                if ipt[ir][ic] == 10:
                    ipt[ir][ic] = -100000000
                    flash_count += 1
                    if ir - 1 > -1:
                        if ipt[ir-1][ic] < 10:
                            ipt[ir-1][ic] += 1
                        if ic - 1 > -1:
                            if ipt[ir-1][ic-1] < 10:
                                ipt[ir-1][ic-1] += 1
                        if ic + 1 < len(r):
                            if ipt[ir-1][ic+1] < 10:
                                ipt[ir-1][ic+1] += 1
                    if ic - 1 > -1:
                        if ipt[ir][ic-1] < 10:
                            ipt[ir][ic-1] += 1
                    if ic + 1 < len(r):
                        if ipt[ir][ic+1] < 10:
                            ipt[ir][ic+1] += 1
                    if ir + 1 < len(ipt):
                        if ipt[ir+1][ic] < 10:
                            ipt[ir+1][ic] += 1
                        if ic - 1 > -1:
                            if ipt[ir+1][ic-1] < 10:
                                ipt[ir+1][ic-1] += 1
                        if ic + 1 < len(r):
                            if ipt[ir+1][ic+1] < 10:
                                ipt[ir+1][ic+1] += 1
    ipt = [[x if x > -1 else 0 for x in row] for row in ipt]

print(flash_count)

all_flash = False
i = 0

ipt = test

while not all_flash:
    ipt = [[y+1 for y in x] for x in ipt]
    while 10 in [y for x in ipt for y in x]:
        for ir, r in enumerate(ipt):
            for ic,c in enumerate(r):
                if ipt[ir][ic] == 10:
                    ipt[ir][ic] = -100000000
                    flash_count += 1
                    if ir - 1 > -1:
                        if ipt[ir-1][ic] < 10:
                            ipt[ir-1][ic] += 1
                        if ic - 1 > -1:
                            if ipt[ir-1][ic-1] < 10:
                                ipt[ir-1][ic-1] += 1
                        if ic + 1 < len(r):
                            if ipt[ir-1][ic+1] < 10:
                                ipt[ir-1][ic+1] += 1
                    if ic - 1 > -1:
                        if ipt[ir][ic-1] < 10:
                            ipt[ir][ic-1] += 1
                    if ic + 1 < len(r):
                        if ipt[ir][ic+1] < 10:
                            ipt[ir][ic+1] += 1
                    if ir + 1 < len(ipt):
                        if ipt[ir+1][ic] < 10:
                            ipt[ir+1][ic] += 1
                        if ic - 1 > -1:
                            if ipt[ir+1][ic-1] < 10:
                                ipt[ir+1][ic-1] += 1
                        if ic + 1 < len(r):
                            if ipt[ir+1][ic+1] < 10:
                                ipt[ir+1][ic+1] += 1
    i += 1
    if len([y for x in ipt for y in x if y < 0]) == len([y for x in ipt for y in x]):
            all_flash = True
    ipt = [[x if x > -1 else 0 for x in row] for row in ipt]

print(i)
