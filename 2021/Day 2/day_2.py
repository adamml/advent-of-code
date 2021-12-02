with open('input.txt', 'r') as f:
    data = [x.replace('\n', '').split() for x in f.readlines()]
    x_position = [int(x[1]) if x[0] == 'forward' else 0 for x in data]
    z_position = [-int(x[1]) if x[0] == 'up' else int(x[1]) if x[0] == 'down' else 0 for x in data]

    print(sum(x_position) * sum(z_position))

    aim = 0
    depth = 0
    forward = 0
    for x in data:
        if x[0] == 'forward':
            forward += int(x[1])
            depth += aim * int(x[1])
        elif x[0] == 'down':
            aim += int(x[1])
        else:
            aim += -int(x[1])

    print(forward * depth)
