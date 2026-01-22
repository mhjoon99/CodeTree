N = int(input())
i = 1
cnt = 0

while N > 1:
    N /= i
    i += 1
    cnt += 1

print(cnt)