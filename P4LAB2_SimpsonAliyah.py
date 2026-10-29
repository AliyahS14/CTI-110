# Aliyah Simpson
# 10/27/2026
# Loops that display multiplication

run_again = "yes"

while run_again == "yes":
    # Get an integer input from use
    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        for i in range(1, 12+1):
            print(f'{user_num} * {i} = {user_num * i}')
        
    else:
        print('This program does not handle negative numbers!!')








    # Get a new value for run_again
    run_again = input("Run the program again? ")

# Loop breaks here
print("Program has ended")
