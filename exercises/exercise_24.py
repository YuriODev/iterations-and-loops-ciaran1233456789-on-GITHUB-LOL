# Your solution to Exercise 24
count = 0
n = int(input("Enter the first value"))

while n != 0:
    if n % 2 == 0:
        count += 1
    n = int(input("Enter the next value"))

print(count)