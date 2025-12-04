with open('input', 'r') as f:
    data = [l.replace('\n', '') for l in f.readlines()]

lines = [[l.split('->')[0].split(','), l.split('->')[1].split(',')] for l in data]
lines = [[[int(x[0]), int(x[1])] for x in row] for row in lines]

coords = []
counts = []
for i, l in enumerate(lines):
        if(l[0][0] == l[1][0]):
            ymin = min(l[0][1], l[1][1])
            ymax = max(l[0][1], l[1][1])
            for y in range(ymin, ymax + 1):
                if '{},{}'.format(l[0][0], y) not in coords:
                   coords.append('{},{}'.format(l[0][0], y))
                   counts.append(0)
                else:
                    count_idx = coords.index('{},{}'.format(l[0][0], y))
                    counts[count_idx] += 1
        elif(l[0][1] == l[1][1]):
            xmin = min(l[0][0], l[1][0])
            xmax = max(l[0][0], l[1][0])
            for x in range(xmin, xmax + 1):
                if '{},{}'.format(x, l[0][1]) not in coords:
                   coords.append('{},{}'.format(x, l[0][1]))
                   counts.append(0)
                else:
                    count_idx = coords.index('{},{}'.format(x, l[0][1]))
                    counts[count_idx] += 1

print(len([x for x in counts if x>0]))

coords = ['None']
counts = [-1]
for i, l in enumerate(lines):
        if(l[0][0] == l[1][0]):
            ymin = min(l[0][1], l[1][1])
            ymax = max(l[0][1], l[1][1])
            for y in range(ymin, ymax + 1):
                if '{},{}'.format(l[0][0], y) not in coords:
                   coords.append('{},{}'.format(l[0][0], y))
                   counts.append(0)
                else:
                    count_idx = coords.index('{},{}'.format(l[0][0], y))
                    counts[count_idx] += 1
        elif(l[0][1] == l[1][1]):
            xmin = min(l[0][0], l[1][0])
            xmax = max(l[0][0], l[1][0])
            for x in range(xmin, xmax + 1):
                if '{},{}'.format(x, l[0][1]) not in coords:
                   coords.append('{},{}'.format(x, l[0][1]))
                   counts.append(0)
                else:
                    count_idx = coords.index('{},{}'.format(x, l[0][1]))
                    counts[count_idx] += 1
        else:
            if l[0][0] > l[1][0]:
                xstep = -1
            else:
                xstep = 1
            if l[0][1] > l[1][1]:
                ystep = -1
            else:
                ystep = 1
            x = l[0][0]
            y = l[0][1]
            for xx in range(min(l[0][0], l[1][0]), max(l[0][0], l[1][0]) + 1):
                if '{},{}'.format(x, y) not in coords:
                   coords.append('{},{}'.format(x, y))
                   counts.append(0)
                else:
                    count_idx = coords.index('{},{}'.format(x, y))
                    counts[count_idx] += 1
                x += xstep
                y += ystep

print(len([x for x in counts if x>0]))
