N = int(input())
nums = [int(input()) for _ in range(N)]
sum = 0

for i in range(len(nums)):
    if (nums[i] % 2 != 0) and (nums[i] % 3 == 0):
        sum += nums[i]

print(sum)