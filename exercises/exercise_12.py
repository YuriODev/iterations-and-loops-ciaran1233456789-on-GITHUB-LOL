#Exercise 12
n = int(input())

total_sum = 0
for num in range(100, 1000):
    if num % n == 0:
        total_sum += num

print(total_sum)# Your solution to Exercise 12