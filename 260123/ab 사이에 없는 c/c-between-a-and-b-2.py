a, b, c = map(int, input().split())
result = 0

for i in range(a, b+1):
    if i % c == 0:
        result = 1
        break

if result == 0:
    print("YES")
else:
    print("NO")