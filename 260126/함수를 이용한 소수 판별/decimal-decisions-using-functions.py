a, b = map(int, input().split())

# Please write your code here.
def sum_prime_nums(a, b):
    prime_nums = []
    sum = 0
    
    for i in range(a, b+1):
        isPrime = 1
        for j in range(2, i):
            if i % j == 0:
                isPrime = 0
                break
        if isPrime == 1:
            prime_nums.append(i)
    for i in range(len(prime_nums)):
        sum += prime_nums[i]
    return sum

print(sum_prime_nums(a, b))

        