# Write a program to check whether given year is a leap year

# Explain 
# Write a program to check if a year is a leap year

# Conditions:
# 1. Divisible by 4 and not by 100 or 
# 2. Divisible by 400 

# Input
# Enter a year

# Output
# Notify for user if the given year is a leap year

# Program to check if a year is a leap year

def is_leap_year(year): 
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
 # Enter a year for user 
try:
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
except ValueError:
        print("Please enter a valid number.")


  
