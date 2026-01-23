N = int(input())
cnt = 0

while True: # 짝수
    if N % 2 == 0:
        N = N * 3 + 1
    else:   # 홀수
        N = N * 2 + 2
    cnt += 1

    if N >= 1000:
        break

print(cnt)