n = int(input())

# Please write your code here.
def draw_square(n):
    nums = [x for x in range(1,10)]
    cnt = 0
    
    for _ in range(n):
        for _ in range(n):
            print(nums[cnt], end=" ")
            cnt += 1
            if cnt >= 9:
                cnt = 0
        print()

draw_square(n)