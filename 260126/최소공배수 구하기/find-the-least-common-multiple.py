n, m = map(int, input().split())

# Please write your code here.
def lcm(a, b):
    # gcd 구하기
    for i in range(min(a,b), 0, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
    # 최소공배수 = a * b / 최대공약수
    result = int(a * b / gcd)
    print(result)

lcm(n, m)