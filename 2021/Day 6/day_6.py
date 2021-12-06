test_input = [3,4,3,1,2]

with open('input.txt', 'r') as f:
    data = [x.replace('\n', '') for x in f.readlines()]
data = [x.split(',') for x in data][0]
data = [int(x) for x in data]

ipt = data

for day in range(0, 80):
    for x in ipt:
        if x == 0:
            ipt.append(9)
    ipt = [7 if x == 0 else x for x in ipt]
    ipt = [x-1 for x in ipt]

print(len(ipt))

ipt = data

counts = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6,0], [7,0], [8,0]]

for i in ipt:
    counts[i][1] += 1

for day in range(0, 256):
    for d in counts:
        if d[0] == 0:
            counts.append([9, d[1]])
            counts[7][1] += d[1]
    counts = [[c[0]-1, c[1]] for c in counts]
    counts = counts[1:]   
i, total = zip(*counts)
print(sum(total))
