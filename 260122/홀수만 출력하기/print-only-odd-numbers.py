N = int(input())
nums = [int(input()) for _ in range(N)]

for i in range(N):
    if (nums[i] % 3 == 0) and (nums[i] % 2 != 0):
        print(nums[i])