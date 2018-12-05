def go():
    with open('input.txt', 'r') as f:
        ids = [item for item in f.read().split('\n') if item]
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                diff_count = 0
                for k in range(len(ids[i])):
                    if ids[i][k] != ids[j][k]:
                        diff_count += 1
                if diff_count == 1:
                    return ''.join([ids[i][k] for k in range(len(ids[i])) if ids[i][k] == ids[j][k]])
print(go())
