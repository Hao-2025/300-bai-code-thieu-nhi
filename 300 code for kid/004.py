# Write a program that calculates taxi fare based on the number of kilometers traveled.

# Input : The number of kilometers traveled that user enters
# Output : Total of taxi fare

# Pricing levels
# First km: 10.000 vnd
# From 2nd km to 10th km: 8.500 vnd/km
# From 11th km onward: 7.500 vnd/km

# Step to perform
# step 1: Enter the number of kilometers traveled by user (float number)
# step 2: Calculate the total of taxi fare based on the number of kilometers traveled according to the pricing levels
# step 3: Print the total of taxi fare

# Program that calculates taxi fare based on the number of kilometers traveled.

def calculate_taxi_fare(km):
    if km <= 1:
        fare = 10000
    elif km <= 10:
        fare = 10000 + (km - 1) * 8500
    else:
        fare = 10000 + 9 * 8500 + (km - 10) * 7500
    return fare

# Enter the number of kilometers traveled by user

try:
    distance = float(input("The number of kilometers traveled: "))
    if distance < 0:
        print("The distance in kilometers is invalid. Please enter a positive number")
    else:
        total_fare = calculate_taxi_fare(distance)
        print(f"Total of taxi fare is: {distance} vnd")
except ValueError:
    print("Invalid input. Please enter a positive number.")

