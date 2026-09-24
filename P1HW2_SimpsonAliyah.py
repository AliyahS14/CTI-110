# Simpson Aliyah
# 9/17/26
# Calculating and showing travel expenses

print("--------calculating travel expenses---------")

print()
print()

#Enter Budget
Budget = int(input("Enter the Budget value: "))

#Enter your travel destination
Destination = input("Enter yor travel destination: ")

#Amount spent on gas
Gas_spent = int(input("Enter how much you spent on gas: "))

#Money for accomomodation
Hotel = int(input("Enter how much you think you will spend on a hotel: "))

#Money for food
Food = int(input("Enter how much you will need for food: "))

print("--------Travel Expenses--------")

# Remaining_balance
remaining_balance = Budget - Gas_spent - Hotel - Food

print("Location: ", Destination)
print("Initial buget: ", Budget)
print("Fuel: ", Gas_spent)
print("Accomodation: ", Hotel)
print("Food: ", Food)

# Calculate the remaining balance
print("Remaining balance: ", remaining_balance)


