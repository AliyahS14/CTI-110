'''
Aliyah Simpson
9/24/2026
use the math library to calculate circle features
'''

import math

print(math.pi)

# Get radius from user as float
radius = float(input("Enter the radius as a float: "))

print()

# Calculate diameter
diameter = 2 * radius

#Display diameter using an f-string
print(f"The diameter of the circle is {diameter:.1f}")

print()

# Calculate circumferance
circumferance = 2 * math.pi * radius

# Display circumferance
print(f"The circumferance of the circle is {circumferance:.2f}")

# calculate the area
area = math.pi * math.pow(radius, 2)

print(f"The area of the circle is {area:.3f}")