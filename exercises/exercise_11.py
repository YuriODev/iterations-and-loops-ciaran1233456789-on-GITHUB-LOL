#Exercise 11

upper_limit = int(input("Enter the Upper Limit: "))
total = 0
for n in range (1, upper_limit+1):
    total += n / (n+1)

print(round(total, 2))# Your solution to Exercise 11