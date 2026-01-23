N = int(input())
result = 0

for i in range(2, N):
    if N % i == 0:
        result = 1
        break

if result == 1: # 합성수라면
    print("C")
else:   # 합성수가 아니라면
    print("N")