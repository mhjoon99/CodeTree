N = int(input())
nums = [int(input()) for _ in range(N)]
sum = 0
avg = 0.0

for i in range(N):
    sum += nums[i]

avg = round(sum/N, 1)
print(sum, avg)