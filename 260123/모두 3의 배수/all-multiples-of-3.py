nums = [int(input()) for _ in range(5)]
cnt = 0

for i in range(len(nums)):
    if nums[i] % 3 == 0:
        cnt += 1

if cnt == 5:
    print(1)
else:
    print(0)