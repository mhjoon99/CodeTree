a, b, c = map(int, input().split())

total = a + b + c
avg = int(total / 3)
residual = total - avg

print(total)
print(avg)
print(residual)