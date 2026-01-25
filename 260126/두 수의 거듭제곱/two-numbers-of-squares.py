a, b = map(int, input().split())

# Please write your code here.
def calc_square(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

print(calc_square(a, b))