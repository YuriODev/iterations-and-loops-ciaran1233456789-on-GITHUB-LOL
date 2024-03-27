# Your solution to Exercise 19
n = int(input("Enter the number: "))
for num in range(10, 100):
    ten = num // 10
    one = num % 10
    if (ten ** 2 + one ** 2) % n == 0:
        print(num)