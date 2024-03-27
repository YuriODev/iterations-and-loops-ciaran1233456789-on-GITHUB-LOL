# Your solution to Exercise 5
n = int(input("Enter a number: "))
count = 0

for ohio in range(n, 0, -1):
    count = count + ohio

print(count)