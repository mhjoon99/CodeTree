N = int(input())
cnt = 0

while True:
    N /= 2
    cnt += 1
    if N == 1:
        break
print(cnt)