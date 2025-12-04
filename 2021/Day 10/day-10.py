import statistics

with open("input.txt", "r") as f:
    data = f.readlines()

data = [l.replace("\n", "") for l in data]

ipt = data

score = 0
autocomplete_score = []

for i, line in enumerate(ipt):
    line_emptied = False
    while not line_emptied:
        len_line = len(line)
        line = line.replace("()", "")
        line = line.replace("{}", "")
        line = line.replace("<>", "")
        line = line.replace("[]", "")
        if len_line == len(line):
            line_emptied = True
    bad_line = []
    try:
        bad_line.append(line.index(')'))
    except ValueError:
        pass
    try:
        bad_line.append(line.index('}'))
    except ValueError:
        pass
    try:
        bad_line.append(line.index(']'))
    except ValueError:
        pass
    try:
        bad_line.append(line.index('>'))
    except ValueError:
        pass
    if bad_line:
        if line[min(bad_line)] == ')':
            score += 3
        elif line[min(bad_line)] == ']':
            score += 57
        elif line[min(bad_line)] == '}':
            score += 1197
        elif line[min(bad_line)] == '>':
            score += 25137
    else:
        this_autocomplete_score = 0
        for x in line[::-1]:
            this_autocomplete_score = this_autocomplete_score * 5
            if x == "(":
                this_autocomplete_score += 1
            elif x == "[":
                this_autocomplete_score += 2
            elif x == "{":
                this_autocomplete_score += 3
            elif x == "<":
                this_autocomplete_score += 4
        autocomplete_score.append(this_autocomplete_score)
        
print(score)
print(statistics.median(autocomplete_score))
