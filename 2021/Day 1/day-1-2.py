with open('input_day_1.txt', 'r') as f:
    data = list(map(lambda x: int(x.replace('\n', '')), f.readlines()))

    print(sum([int(sub1) < int(sub2) for sub1,
               sub2 in zip(list(map(lambda x: sum(data[x:x+3]), range(0, len(data)-2))),
                    list(map(lambda x: sum(data[x:x+3]), range(1, len(data)-2))))]))
