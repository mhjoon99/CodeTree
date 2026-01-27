Y, M, D = map(int, input().split())

# Please write your code here.
def is_leap_year(year):  # 윤년 판단
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        
        if year % 100 == 0:
            return False
        
        return True
    
    return False

def is_exist(year, month, day):
    if month == 2:
        if is_leap_year(year):   # 윤년이라면
            if 1 <= day <= 29:
                return True
        else:   # 윤년이 아니라면
            if 1 <= day <= 28:
                return True

    elif month in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= day <= 31:
            return True
    
    else:
        if 1 <= day <= 30:
            return True
    
    return False

def print_season(year, month, day):
    if is_exist(year, month, day):
        if 3 <= month <= 5:
            return "Spring"
        elif 6 <= month <= 8:
            return "Summer"
        elif 9 <= month <= 11:
            return "Fall"
        else:
            return "Winter"
    else:
        return -1
    
print(print_season(Y, M, D))
