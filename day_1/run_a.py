with open('input_1.txt', 'r') as f:
    print(sum(int(item) for item in f.read().split('\n') if item))
