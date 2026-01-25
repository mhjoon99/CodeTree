y = int(input())

# Please write your code here.
def judge_leap(n):
    is_leap = 0
    if n % 4 == 0:
        is_leap = 1
        if n % 100 == 0 and n % 400 != 0:
            is_leap = 0
    return is_leap

flag = judge_leap(y)
if flag == 1:
    print("true")
else:
    print("false")