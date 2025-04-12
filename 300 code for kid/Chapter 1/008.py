# Write a program to count the number of even or odd numbers in a list

# Input
# Enter a list of integer numbers

# Output
# Number of even numbers
# Number of odd numbers

# Step to write the program
# 1. Enter a list of integer number from user input
# 2. Iterate each number and check every number in the list if it is odd or even
# 3. Count the number of odd and even numbers
# 4. Print the number

# Program to count the number of odd and even numbers in a list

def count_even_odd(numbers):
    count_even = 0
    count_odd = 0
    for number in numbers:
        if number % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd
    
# Enter a list of integer numbers
try:
    input_list = input("Enter a list of integer numbers, separated by space: ")
    numbers = [int(num) for num in input_list.split()]
# To split string into elements using SPLIT() and turn these elements into integers by using INT()
# Using list comprehension to do this: [int (num)  for num in input_list.split()]
# LIST COMPREHENSION: To make a list to iterate over a iterable and apply a EXPRESSION for every elements

    even_count, odd_count = count_even_odd(numbers)
    print(f"Number of even: {even_count}")
    print(f"Number of odd: {odd_count}")
except ValueError:
     print("Please enter a valid number.")
    


  
