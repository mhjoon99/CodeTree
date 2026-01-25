a, b = map(int, input().split())

# Please write your code here.
def judge_nums(a, b):
    cnt = 0
    for i in range(a, b+1):
        total = 0
        flag = 1    # 소수라면
        num_list = list(map(int, str(i)))    # 각 자리수 합
        total += sum(num_list) 
        for j in range(2, i):   # 소수 판별
            if i % j == 0:
                flag = 0    # 소수가 아님
                break
        if flag == 1 and total % 2 == 0:
            cnt += 1
    
    return cnt

result = judge_nums(a, b)
print(result)
