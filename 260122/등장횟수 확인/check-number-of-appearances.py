nums = [int(input()) for _ in range(5)]
cnt = 0

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        cnt += 1

print(cnt)