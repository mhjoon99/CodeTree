n = int(input())

# Please write your code here.
def judge_num(n):
    ten = n // 10
    one = n % 10
    return (n % 2 == 0) and ((ten+one) % 5 == 0)

if judge_num(n) == True:
    print("Yes")
else:
    print("No")