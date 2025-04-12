# Write a program to print all prime numbers from 1 to 100

# Input
# There is NO input from user input

# Output
# Print all prime numbers from 1 to 100

# Define PRIME NUMBER
# A prime number is a natural number greater than 1, whose only factors are 1 and itself

# Step to write the program
# 1. Iterate over all prime numbers from 1 to 100
# 2. Check these numbers are prime numbers or not
# 3. If they are prime numbers, print them

# Program to print all prime numbers from 1 to 100

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int (n**0.5) + 1):
    # Using loop FOR  to check from 2 to square root of N (int(n**0.5)+1)
    # if N divided by any numbers in this range, return False
    # if N NOT divided by any numbers in this range, return True
        if n % i == 0:
            return False
    return True
def print_prime_up_to_100():
    for number in range(1,101):
        if is_prime(number):
            print (number, end=' ')
# parameter END=' ' to print every prime numbers in same line and split them by space
    print() # New line after print all prime numbers
                   
# Function to print all prime numbers from 1 to 100
print_prime_up_to_100()
