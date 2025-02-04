# Write a program to check the number is odd or even

# Input : An integer number that user enters
# Output : Notify user that whether the number is odd or even

# Step to perform
# step 1: Enter the number from user input
# step 2: Check if the number is odd or even

# if the number is divisible by 2 that means the number is even 
# if the number is not divisible by 2 that means the number is odd

# Program to check the number is odd or even
def check_even_odd(n):
    if n % 2 == 0:
        return "Your number is even."
    else:
        return "Your number is odd."
    
# Input from user

try:
    number = int(input("Enter an integer number: "))
    result = check_even_odd(number)
    print(result)
except ValueError:
    print("Invalid input. Please enter an integer number.")

    