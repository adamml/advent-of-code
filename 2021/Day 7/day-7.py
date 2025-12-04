with open('input.txt', 'r') as f:
    data = [int(x) for x in f.readlines()[0].split(',')]

ipt = data

cost = []

for x in range(min(ipt), max(ipt)+1):
    this_cost = 0
    for xx in ipt:
        this_cost += abs(x - xx)
    cost.append(this_cost)

print(min(cost))

cost = []

costs = range(min(ipt), max(ipt)+1)
print(costs)

for x in range(min(ipt), max(ipt)+1):
    this_cost = 0
    for xx in ipt:
        this_cost += sum(costs[0:abs(x - xx)+1])
    cost.append(this_cost)

print(min(cost))
