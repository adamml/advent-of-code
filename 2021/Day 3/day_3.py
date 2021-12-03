import statistics
with open('input.txt', 'r') as f:
    raw_data = [x.replace('\n', '').split() for x in f.readlines()]
    data = [[None] * len(raw_data) for x in raw_data[0][0]]
    
    for idx_row, row in enumerate(raw_data):
        for idx_bit, bit in enumerate(row[0]):
            data[idx_bit][idx_row] = int(bit)
    
    gamma = int(''.join([str(statistics.mode(x)) for x in data]), 2)
    epsilon = int(''.join(['1' if statistics.mode(x) == 0 else '0' for x in data]), 2)

    print(gamma * epsilon)
     
    oxygen_data = [x[0] for x in raw_data]
    for idx_bit, bit in enumerate(data):
        this_bit = str(max(statistics.multimode([int(x[idx_bit]) for x in oxygen_data])))
        oxygen_data = [x for x in oxygen_data if  x[idx_bit] == this_bit]
        if len(oxygen_data) == 1:
            break

    co2_data = [x[0] for x in raw_data]
    for idx_bit, bit in enumerate(data):
        this_bit = str(max(statistics.multimode([int(x[idx_bit]) for x in co2_data])))
        co2_data = [x for x in co2_data if x[idx_bit] != this_bit]
        if len(co2_data) == 1:
            break
        
    print(int(co2_data[0], 2) * int(oxygen_data[0], 2))
    
    
