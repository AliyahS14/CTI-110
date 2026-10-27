# Aliyah Simpson
# 10/22/26




import turtle


# Set up the window
window= turtle.Screen()


# Make the turtle object
cosmo = turtle.Turtle()


# Change the size and colors of the lines
cosmo.pensize(5)
cosmo.pencolor("pink")


# Draw the square
for side in range(4):
    cosmo.forward(100)
    cosmo.right(90)




# While loop to draw the roof
num = 0
while num < 3:
    num = num + 1
    cosmo.forward(100)
    cosmo.left(120)



window.mainloop()
