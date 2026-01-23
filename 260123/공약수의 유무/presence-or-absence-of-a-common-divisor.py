A, B = map(int, input().split())
result = 0

for i in range(A, B+1):
    if (1920 % i == 0) and (2880 % i == 0):
        result = 1
        break

if result == 1:
    print(1)
else:
    print(0)