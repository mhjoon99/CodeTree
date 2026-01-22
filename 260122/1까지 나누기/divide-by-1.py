N = int(input())
cnt = 0

for i in range(1, 5000):
    N = N // i    
    if N <= 1:
        break
    cnt += 1