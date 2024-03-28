# Finding the sum of the digits of the entered number

number = int(input("enter the number:"))
sum = 0
number1 = number

while number1 != 0:
    unitsdigit = number1 % 10
    sum += unitsdigit
    number1 //= 10

print(sum)