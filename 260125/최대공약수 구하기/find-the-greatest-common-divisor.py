n, m = map(int, input().split())

# Please write your code here.
def gcd(n, m):
    for i in range(min(n,m), 1, -1):
        if n % i == 0 and m % i == 0:
            result = i
            break
    print(i)

gcd(n, m)