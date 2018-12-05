with open('input.txt', 'r') as f:
    frequencies = [int(item) for item in f.read().split('\n') if item]
    n = len(frequencies)
    visited = set()
    i = 0
    c = 0
    while True:
        c += frequencies[i]
        i += 1
        i = i % n
        if c in visited:
            print(c)
            break
        visited.add(c)
