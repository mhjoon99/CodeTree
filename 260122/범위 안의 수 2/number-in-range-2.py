nums = [int(input()) for _ in range(10)]
cnt = 0
sum = 0
avg = 0.0

for i in range(len(nums)):
    if 0 <= nums[i] <= 200:
        sum += nums[i]
        cnt += 1

avg = round(sum / cnt, 1)
print(sum, avg)