# Your solution to Exercise 23
total = 0
count = 0
n = int(input("Enter an integer: "))

while n != 0:
    total += n
    count += 1
    n = int(input("Enter an integer: "))


average = total / count
print(average)