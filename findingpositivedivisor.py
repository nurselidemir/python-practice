# find the number of positive divisors of the entered number

number = int(input("enter the number:"))

numberofdivisors = 0

for i in range(1, number + 1):
    if number % i == 0:
        numberofdivisors += 1
print(f" the number {number} has {numberofdivisors} divisors")

