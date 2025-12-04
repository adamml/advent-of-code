test = []

summed = 0

do_test = False
part_one = False

if not do_test:
    test = open('/input/day03.txt')

def recurse(string, length):
    maxm = 0
    maxm_loc = 0
    i = 0
    while i < len(string) - (length):
        if int(string[i]) > maxm:
            maxm = int(string[i])
            maxm_loc = i+1
        i += 1
    return maxm, maxm_loc
    

for x in test:
    if not do_test:
        x = x[:-1]
    a = 0
    a_loc = 0
    if part_one:
        b = 0
        for i, y in enumerate(str(x)):
            if i == len(str(x)) - 1:
                pass
            elif int(str(x)[i]) > a:
                a = int(str(x)[i])
                a_loc = i+1
                b = 0
                while a_loc < len(str(x)):
                    if int(str(x)[a_loc]) > b:
                        b = int(str(x)[a_loc])
                    a_loc += 1
        summed += ((a*10)+b)
    else:
        [y, j] = recurse(str(x), 11)
        [z, k] = recurse(str(x)[j:], 10)
        [aa, l] = recurse(str(x)[j+k:], 9)
        [ab, m] = recurse(str(x)[j+k+l:], 8)
        [ac, n] = recurse(str(x)[j+k+l+m:], 7)
        [ad, o] = recurse(str(x)[j+k+l+m+n:], 6)
        [ae, p] = recurse(str(x)[j+k+l+m+n+o:], 5)
        [af, q] = recurse(str(x)[j+k+l+m+n+o+p:], 4)
        [ag, r] = recurse(str(x)[j+k+l+m+n+o+p+q:], 3)
        [ah, s] = recurse(str(x)[j+k+l+m+n+o+p+q+r:], 2)
        [ai, t] = recurse(str(x)[j+k+l+m+n+o+p+q+r+s:], 1)
        [aj, u] = recurse(str(x)[j+k+l+m+n+o+p+q+r+s+t:], 0)
        summed += ((y*100000000000)+
                   (z*10000000000)+
                   (aa*1000000000)+
                   (ab*100000000)+
                   (ac*10000000)+
                   (ad*1000000)+
                   (ae*100000)+
                   (af*10000)+
                   (ag*1000)+
                   (ah*100)+
                   (ai*10)
                   +aj)
    
print(summed)
