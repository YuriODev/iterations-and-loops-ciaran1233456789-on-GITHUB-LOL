# Your solution to Exercise 21
n = int(input())
count = 1
total = 0

for i in range(n, 1, -1):
    count = count * i 
    total += count

print(total)