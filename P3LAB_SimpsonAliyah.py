# Aliyah Simpson
# 10/8/2026
# Determine the most efficient coin combination

# Get amount of money
money= float(input("Enter an amount of money: $"))

# Convert money into an interger
money_int = int(money * 100)

print(money_int)

# Determine how many dollars are needed
num_dollars = money_int // 100
remaining_money = money_int % 100

# Determine how many quartes are needed
num_quarters = remaining_money // 25
remaining_money = remaining_money %25

# Determine how many dimes are needed
num_dimes = remaining_money // 10
remaining_money = remaining_money %10

# Determine how many nickels are needed
num_nickels = remaining_money // 5
remaining_money = remaining_money %5

# Determine how many pennies are needed
num_pennies = remaining_money // 1
remaining_money = remaining_money %1

if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
else:
    print(f"{num_dollars} Dollars")

if num_quarters > 0:
    if num_quarters == 1:
     print(f"{num_quarters} Quarter")
else:
    print(f"{num_quarters} Quarters")

if num_dimes > 0:
    if num_dimes == 1:
     print(f"{num_dimes} Dime")
else:
    print(f"{num_dimes} Dimes")

if num_nickels > 0:
    if num_nickels == 1:
        print(f"{num_nickels} Nickel")
else:
    print(f"{num_nickels} Nickels")

if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Penny")
else:
    print(f"{num_pennies} Pennies")

    