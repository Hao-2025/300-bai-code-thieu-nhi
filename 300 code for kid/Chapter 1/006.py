# Write a program to print the multiplication table

# Explain 
# Write the multiplication table from 1 to 10.
# The multiplication table where each number from 1 to 10 is multiplied by number from 1 to 10.

# Input
# There is NO input from user

# Output
# Print the multiplication table    

# Program to print the multiplication table

def print_multiplication_table(): 
    for i in range(1,11): # Outer loop: Iterates through number from 1 to 10, presenting the MULTIPLICANDS
        print(f"Multiplication table {i}:")
        for j in range (1,11): # Inter loop: Iterates through number from 1 to 10, presenting the MULTIPLIERS
            print(f"{i} x {j} = {i * j}")
        print() # Print a space between each multiplication tables 
    
# Function to print multiplication table
print_multiplication_table()

  
