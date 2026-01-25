a, b = map(int, input().split())

# Please write your code here.
def find_num(a, b):
    cnt = 0
    for i in range(a, b+1):
        _list = map(int, str(i))
        if 3 in _list:
            cnt += 1
        if 6 in _list:
            cnt += 1
        if 9 in _list:
            cnt += 1
        if i % 3 == 0:
            cnt += 1
    return cnt

print(find_num(a,b))
    