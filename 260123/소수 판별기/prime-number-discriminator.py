N = int(input())
result = 0

for i in range(1, N+1):
    if N % i == 0:
        result = 1
        break

if result == 1: # 소수 X
    print("C")
else:   # 소수
    print("P")

