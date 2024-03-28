number = int(input("Enter the number whose primality you want to check:"))

prime = True

for i in range(2,number):
    if number % i == 0:
        prime = False
        break
if prime == True:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")