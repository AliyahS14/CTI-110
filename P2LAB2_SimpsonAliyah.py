'''
Aliyah Simpson
9/24/2026
use a dictionary to determine cars mpg
'''


# Create the dictionary - car names are keys and values are mpg
vroom = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}


# Display ONLY the keys from the dictionary
print()
print(vroom.keys())


# Get an input from the user - choose a car
car_name = input("Enter a car to see its mpg: ")

# Use the vehicle name entered by the user to get the mpg value
mpg = vroom[car_name]

# Display the mpg for the vehicle selected
print(f"The {car_name} gets {mpg} mpg. ")

# Ask the user how many miles they want to go
miles = float(input(f"How many miles will you drive the {car_name}?"))

# Calculate the gallons, divide the miles driven he vehicles mpg
gallons_needed = miles/mpg

#Display the results, rounded to 2 decimal places
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles} mile.")