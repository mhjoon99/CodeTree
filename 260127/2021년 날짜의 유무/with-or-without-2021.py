M, D = map(int, input().split())

# Please write your code here.
def judge_month(month):
    if 1 <= month <= 12:
        return True
    else:
        return False

def judge_day(month, day):
    if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
        return True
    if month == 2 and (1 <= day <= 28):
        return True
    if month in [4, 6, 9, 11] and 1<= day <= 30:
        return True
    return False

def judge_True(month, day):
    if judge_month(month) and judge_day(month, day):
        return "Yes"
    return "No"

print(judge_True(M, D))