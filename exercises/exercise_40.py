# Your solution to Exercise 40
n = int(input("Enter a number n: "))
a, b = 0, 1
fibonacci_sequence = [a, b]
while b < n:
    a, b = b, a + b
    fibonacci_sequence.append(b)
print(fibonacci_sequence)