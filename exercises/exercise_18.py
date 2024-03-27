# Your solution to Exercise 18
count = 0
n = int(input("Enter the value of n:"))

for _ in range(n):
    error = int(input("Enter error collected"))
    count += error

print(count)