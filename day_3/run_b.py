with open('input.txt', 'r') as f:
    lines = [item for item in f.read().split('\n') if item]
    claims = []
    n = 0
    m = 0
    unused_ids = set()
    for line in lines:
        data = line.split(' ')
        x, y = [int(i) for i in data[2][:-1].split(',')]
        w, h = [int(i) for i in data[3].split('x')]
        n = max(n, x + w)
        m = max(m, y + h)
        claims.append({'id': int(data[0][1:]), 'x': x, 'y': y, 'w': w, 'h': h})
        unused_ids.add(claims[-1]['id'])
    n += 1
    m += 1
    matrix = [[False] * n for i in range(m)]
    t = 0
    for claim in claims:
        for i in range(claim['y'], claim['h'] + claim['y']):
            for j in range(claim['x'], claim['w'] + claim['x']):
                if matrix[i][j]:
                    if claim['id'] in unused_ids:
                        unused_ids.remove(claim['id'])
                    if matrix[i][j] in unused_ids:
                        unused_ids.remove(matrix[i][j])
                else:
                    matrix[i][j] = claim['id']
    print([i for i in unused_ids][0])
