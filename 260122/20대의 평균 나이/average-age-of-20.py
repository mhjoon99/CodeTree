sum = 0
avg = 0.0
cnt = 0
while True:
    n = int(input())
    if n // 10 != 2:
        break
    sum += n
    cnt += 1

avg = sum / cnt
print(f"{avg:.2f}")