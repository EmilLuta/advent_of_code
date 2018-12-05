from collections import Counter

with open('input.txt', 'r') as f:
    ids = [item for item in f.read().split('\n') if item]
    twos = 0
    threes = 0
    for i in ids:
        c = Counter(i)
        two = False
        three = False
        for key in c:
            if c[key] == 2:
                two = True
            if c[key] == 3:
                three = True
        if two:
            twos += 1
        if three:
            threes += 1
    print(twos * threes)
