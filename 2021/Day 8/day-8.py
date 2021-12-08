test_data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

with open("input.txt", "r") as f:
    data = f.readlines()

#ipt = test_data.split("\n")
ipt = data

out = [len([len(x) for x in row.split("|")[1].strip().split(" ") if len(x) in (2, 3, 4, 7)]) for row in ipt]
print(sum(out))

summation = 0

numbers = [None] * 10
top = None
top_right = None
bottom_left = None

for row in ipt:
    decode_this = row.split("|")[0].strip().split(" ")
    out = row.split("|")[1].strip().split(" ")
    for x in decode_this:
        if len(x) == 2:
            numbers[1] = x
        elif len(x) == 4:
            numbers[4] = x
        elif len(x) == 3:
            numbers[7] = x
        elif len(x) == 7:
            numbers[8] = x
    top = list(set(numbers[7]).difference(set(numbers[1])))[0]
    for x in decode_this:
        if len(x) == 6:
            for s in numbers[1]:
                if s not in x:
                    numbers[6] = x
                    top_right = s
    for x in decode_this:
        if len(x) == 5:
            if top_right not in x:
                numbers[5] = x
    for s in numbers[6]:

        if s not in numbers[5]:
            bottom_left = s
    for x in decode_this:
        if len(x) == 5:
            if top_right not in x and bottom_left not in x:
                pass
            elif top_right in x and bottom_left in x:
                numbers[2] = x
            else:
                numbers[3] = x
        elif len(x) == 6:
            if top_right not in x and bottom_left in x:
                pass
            elif top_right in x and bottom_left not in x:
                numbers[9] = x
            else:
                numbers[0] = x
    summation += int("".join(["".join([str(i) for i, n in enumerate(numbers) if "".join(sorted(n))== "".join(sorted(x))]) for x in out]))
    numbers = [None] * 10
    top = None
    top_right = None
    bottom_left = None

print(summation)
