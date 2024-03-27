# Your solution to Exercise 31
days = int(input("Enter a number of days: "))
lowest = 0
freezing = "No"
for _ in range (days):
    temperature = int(input())
    if temperature < -15 and temperature < lowest:
        lowest = temperature
        freezing = "Yes"

print(lowest)
print(freezing)
