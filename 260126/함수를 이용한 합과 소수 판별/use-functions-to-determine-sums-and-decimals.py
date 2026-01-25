a, b = map(int, input().split())

# Please write your code here.
# 소수인지 반환하는 함수
def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

# 자릿수 합이 짝수인지 반환하는 함수
def is_digit_sum_even(n):
    num_list = list(map(int, str(n)))
    digit_sum = sum(num_list)

    if digit_sum % 2 == 0:
        return True
    
    return False

# 소수와 자릿수 합이 짝수인지 판별하는 함수
def judge_num(n):
    if is_prime(n) and is_digit_sum_even(n):
        return True
    
    return False

cnt = 0

for i in range(a, b+1):
    if judge_num(i):
        cnt += 1

print(cnt)