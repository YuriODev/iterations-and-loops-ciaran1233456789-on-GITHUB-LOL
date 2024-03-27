# Your solution to Exercise 29
total = 0
squares_sum = 0
while True:
    num = int(input())
    total += num
    squares_sum += num * num
    if total == 0:
        break

print(squares_sum)