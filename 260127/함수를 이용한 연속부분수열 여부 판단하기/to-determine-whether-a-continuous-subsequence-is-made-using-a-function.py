n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def judge_part_seq(a, b):
    n1, n2 = len(a), len(b)
    if n2 > n1:
        return "No"
    
    for i in range(n1 - n2 + 1):
        if a[i:i+n2] == b:
            return "Yes"
    return "No"

print(judge_part_seq(a, b))