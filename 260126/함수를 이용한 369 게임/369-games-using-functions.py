a, b = map(int, input().split())

# Please write your code here.
def find_num(a, b):
    cnt = 0
    for i in range(a, b+1, 1):
        _list = list(map(int, str(i)))
        if (3 in _list) or (6 in _list) or (9 in _list) or (i % 3 == 0):
            cnt += 1
    return cnt

print(find_num(a,b))