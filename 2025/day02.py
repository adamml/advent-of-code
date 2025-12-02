test = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

do_Test = False

part_one = False

def tokenizer(string, token_length) -> bool:
    if len(string) % token_length != 0:
        return False
    i = token_length
    a = 0
    needle = string[0:token_length]
    while i <= len(string):
        if string[a:i] != needle:
            return False
        a += token_length
        i += token_length
    return True
        

if not do_Test:
    with open('./input/day02.txt') as f:
        test = f.read()

test_list = test.split(",")

total = 0

for x in test_list:
    for i in range(int(x.split("-")[0]), int(x.split("-")[1])+1):
        if part_one:
            if len(str(i)) % 2 == 0:
                if int(str(i)[0:int(len(str(i)) / 2)]) ==  int(str(i)[int(len(str(i)) / 2):]):
                    total += i
        else:
            tok = 1
            while tok < len(str(i)):
                if tokenizer(str(i), tok):
                    total += i
                    break
                tok += 1
                    
print(total)

