# Your solution to Exercise 39
n = int(input("Enter an integer: "))
n = abs(n)
total_sum = sum(int(digit) for digit in str(n))
print(total_sum)