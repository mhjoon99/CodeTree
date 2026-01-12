a, b = map(int, input().split())

for i in range(a, b+1, 2):
    if a % 2 != 0:
        print(i, end=' ')
    else:   # a가 짝수
        print(i+1, end=' ')