with open('input.txt', 'r') as f:
    print(sum(int(item) for item in f.read().split('\n') if item))
