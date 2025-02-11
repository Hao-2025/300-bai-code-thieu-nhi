# Write a program to check the largest number of three integer numbers

# Input : Three integer numbers that user enters
# Output : Notify user which number is the largest number

# Step to perform
# step 1: Enter three integer numbers from user input
# step 2: Check which number is the largest number

# Using if-elif-else conditional structures to compare each pair of numbers and determine the largest number.

# Program to check the largest number of three integer numbers

def check_largest_number (a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
# Input from user

try:
    num1 = int(input("Enter the first integer number: "))
    num2 = int(input("Enter the second integer number: "))
    num3 = int(input("Enter the third integer number: "))   

    max_number = check_largest_number(num1, num2, num3)
    print (f"The largest number of three integer numbers is: {max_number}")

    # f-string: 
    # Making format string faster, more readable, and more efficient
    # Allow to embed variable values, perform calculations, call functions,
    # or apply formatting directly a string without formatting manual concatenation (liên kết thủ công)


except ValueError: 
    print ("Invalid input. Please enter integer number.")

