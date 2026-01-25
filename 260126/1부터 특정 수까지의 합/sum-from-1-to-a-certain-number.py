n = int(input())

# Please write your code here.
def sum_div_ten(num):
    total = 0
    for i in range(1, num+1):
        total += i
    return total // 10

print(sum_div_ten(n))