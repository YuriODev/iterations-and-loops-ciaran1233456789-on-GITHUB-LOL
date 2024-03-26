# Your solution to Exercise 14
count = 0
n = int(input("Enter the value of n:"))

for _ in range(n):
    if int(input()) == 0:
        count += 1

print(count)