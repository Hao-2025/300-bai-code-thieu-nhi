# Write a program to check the number is positive or negative

# Input : An integer number that user enters
# Output : Notify user that whether the number is positive or negative

# Step to perform
# step 1: Enter the number from user input
# step 2: Check if the number is greater than 0 or smaller than 0

# if the number is great than 0 that means the number is positive
# if the number is smaller than 0 that means the number is negative
# if the number is equal to 0 that means the number is neither positive number nor negative number

# Program to check the number is positive or negative

# Define the function check_number(n) which will check the number is positive or negative
def check_number(n):
    if n > 0:
        return "Your number is positive."
    elif n < 0:
        return "Your number is negative."
    else:
        return "Your number is 0."
    
# Input from user
try:
    number = int(input("Enter an integer number: "))
    result = check_number(number)
    print(result)
except ValueError:
    print("Please enter a valid number.")

