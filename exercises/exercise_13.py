# Your solution to Exercise 13
password = int(input("Enter your password"))
guess = int(input())

while password != guess:
    print("Error")
    guess = int(input(""))

print("Done")