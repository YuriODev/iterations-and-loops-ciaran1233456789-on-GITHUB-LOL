# Your solution to Exercise 27
total_sum = 0
n = int(input())

sign = 1
denominator = 1
for _ in range(n):
    total_sum += 4 * sign / denominator
    sign = sign * -1
    denominator += 2

print(total_sum)