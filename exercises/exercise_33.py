# Your solution to Exercise 33
n = int(input("Enter an integer: "))
for i in range(n):
    for j in range(n):
        if i == j:
            print(0, end="\t")
        elif i < j:
            print(1, end="\t")
        else:
            print(-1, end="\t")
    print()