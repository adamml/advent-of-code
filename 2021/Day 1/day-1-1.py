with open('input_day_1.txt', 'r') as f:
    data = list(map(lambda x: int(x.replace('\n', '')), f.readlines()))
    print(sum([int(sub1) < int(sub2) for sub1, sub2 in zip(data, data[1:])]))
