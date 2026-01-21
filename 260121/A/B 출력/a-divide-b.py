a, b = map(int, input().split())

n = a // b  # 몫
m = a % b   # 나머지

answer = []

for _ in range(20):
    m *= 10
    answer.append(str(m//b))
    m %= b

print(f"{n}.{''.join(answer)}")
