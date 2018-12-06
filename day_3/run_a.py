with open('input.txt', 'r') as f:
    lines = [item for item in f.read().split('\n') if item]
    claims = []
    n = 0
    m = 0
    for line in lines:
        data = line.split(' ')
        x, y = [int(i) for i in data[2][:-1].split(',')]
        w, h = [int(i) for i in data[3].split('x')]
        n = max(n, x + w)
        m = max(m, y + h)
        claims.append({'x': x, 'y': y, 'w': w, 'h': h})
    n += 1
    m += 1
    matrix = [[False] * n for i in range(m)]
    t = 0
    for claim in claims:
        for i in range(claim['y'], claim['h'] + claim['y']):
            for j in range(claim['x'], claim['w'] + claim['x']):
                if matrix[i][j]:
                    matrix[i][j] = 'C'
                else:
                    matrix[i][j] = True
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 'C':
                t += 1
    print(t)
