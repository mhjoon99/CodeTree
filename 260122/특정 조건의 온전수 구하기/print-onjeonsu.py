N = int(input())
nums = []

for i in range(1, N+1):
    if (i % 2 == 0) or (i % 10 == 5) or (i % 3 == 0 and i % 9 != 0):
        continue
    nums.append(i)

for i in range(len(nums)):
    print(nums[i], end=" ")