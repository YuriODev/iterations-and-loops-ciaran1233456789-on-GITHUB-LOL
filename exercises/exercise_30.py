# Your solution to Exercise 30
t = int(input("Enter number of hours: "))
divisions = t // 3
amoeba = 1
for _ in range(divisions):
    amoeba *= 2

print(amoeba)