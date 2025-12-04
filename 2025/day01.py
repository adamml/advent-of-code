from math import floor

test = []

doTest = False
method = 2  # Method 1 = Step 1 method; Method 2 = Step 2 method

def processStep(point, password, method, step):
    thisPoint = int(step[1:]) % 100
    if method == 2:
        password = password + floor(int(step[1:]) / 100)
    if step[0] == 'L':
        if point == 0:
            password -= 1
        point = point - thisPoint
    else:
        point = point + thisPoint
    if point > 99:
        point = point - 100
        if method == 2:
            if point != 0:
                password += 1
    elif point < 0:
        point = 100 + point
        if method == 2:
            password += 1
    if point == 0:
        password += 1
    return [point, password]


point = 50
password = 0


if doTest != True:
    with open('./input/day01.txt') as f:
        for x in f:
            [point, password] = processStep(point, password, method, x)
        f.close()
else:
    for x in test:
        [point, password] = processStep(point, password, method, x)

print(password)
