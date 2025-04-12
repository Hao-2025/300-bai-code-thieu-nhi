# Write a program to find the program GREATEST COMMON DIVISOR (gcd) of two integers

# Define GCD 
# Is the largest positive integer that divides two or more numbers without leaving a remainder

# Algorithm : Using Euclid algorithm to find GCD
# 1. If b = 0, then GCD (a, b) = a
# 2 Otherwise, GCD (b, a % b)

# Step to write the program 
# 1. Enter two integers from user input
# 2. Apply Euclid algorithm to find GCD (a, b)
# 3. Print the result   

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Enter two integers from user input
try:
    num1 = int(input("Enter first integer number: "))
    num2 = int(input("Enter first integer number: "))

    ucln = gcd(num1, num2)
    print(f"The GDC of {num1} and {num2} is: {ucln}.")
except ValueError:
    print("Please enter valid numbers.")
