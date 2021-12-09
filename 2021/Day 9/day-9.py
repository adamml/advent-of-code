test = [[2,1,9,9,9,4,3,2,1,0],
[3,9,8,7,8,9,4,9,2,1],
[9,8,5,6,7,8,9,8,9,2],
[8,7,6,7,8,9,6,7,8,9],
[9,8,9,9,9,6,5,6,7,8]]

def basin_points(data, x, y):
    points = [[x, y]]
    base = data[y][x]
    if y - 1 > -1:
        if data[y-1][x] > base and data[y-1][x] != 9:
            points.append([x, y-1])
            d_pts = basin_points(data, x, y-1)
            for pt in d_pts:
                points.append(pt)
    if x - 1 > -1:
        if data[y][x-1] > base and data[y][x-1] != 9:
            points.append([x-1, y])
            d_pts = basin_points(data, x-1, y)
            for pt in d_pts:
                points.append(pt)
    if y + 1 != len(data):
        if data[y+1][x] > base and data[y+1][x] != 9:
            d_pts = basin_points(data, x, y+1)
            for pt in d_pts:
                points.append(pt)
    if x + 1 != len(row):
        if data[y][x+1] > base and data[y][x+1] != 9:
            d_pts = basin_points(data, x+1, y)
            for pt in d_pts:
                points.append(pt)
    return [list(x) for x in set(tuple(pt) for pt in points)]
    
with open('input.txt', 'r') as f:
    data = [[(int(point)) for point in line if point is not "\n"] for line in f.readlines()]

ipt = data

neighbours = []
pos = []

for ir, row in enumerate(ipt):
    for ic, col in enumerate(row):
        n = []
        if ir - 1 > -1:  
            n.append(ipt[ir-1][ic])
        if ir + 1 != len(ipt):
            n.append(ipt[ir+1][ic])
        if ic - 1 > -1:
            n.append(ipt[ir][ic-1])
        if ic + 1 != len(row):
            n.append(ipt[ir][ic+1])
        neighbours.append(n)
        pos.append([ic, ir])

vect = []
for row in ipt:
    for x in row:
        vect.append(x)

for i, x in enumerate(vect):
    for n in neighbours[i]:
        if n - x <= 0:
            vect[i] = None

print(sum([x+1 if x is not None else 0 for x in vect]))

basin_sizes = []

for i, x in enumerate(vect):
    if x is not None:
        basin_sizes.append(len(basin_points(ipt, pos[i][0], pos[i][1])))

basin_sizes.sort()
print(basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1])
