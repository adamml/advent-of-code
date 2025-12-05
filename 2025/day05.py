test = """"""

do_test = False

if not do_test:
    with open("/input/day05.txt") as f:
        test = f.read()

ranges = []
ids = []

passed_break = False

fresh = 0
range_sum = 0

test_split = test.split("\n")
for line in test_split:
    if line == "":
        passed_break = True
    elif passed_break:
        for i in ranges:
            if int(line) >= i[0] and int(line) <= i[1]:
                fresh += 1
                break
    else:
        ranges.append([int(line.split("-")[0]), int(line.split("-")[1])])

keep_looping = True
while keep_looping:
    old_ranges = ranges.copy()
    for i, rng in enumerate(ranges):
        for rngg in ranges:
            if rngg[0] <= rng[0] and rngg[1] >= rng[1]:
                rng = rngg
            elif rngg[0] <= rng[0] and rngg[1] >= rng[0] and rngg[1] <= rng[1]:
                rng = [rngg[0], rng[1]]
            elif rngg[0] >= rng[0] and rngg[0] <= rng[1] and rngg[1] >= rng[1]:
                rng = [rng[0], rngg[1]]
        ranges[i] = rng
    if old_ranges == ranges:
        keep_looping = False

for i in [list(item) for item in set(tuple(row) for row in ranges)]:
    range_sum += i[1] - i[0] + 1

print(fresh, range_sum)
            
