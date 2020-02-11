import re

print("Our Magical Calculator")
print("Type quit to Exit\n")

previous = 0
run = True

def peformMath():
    global run
    equation = input("enter equation")
    if equation == 'quit':
        run = False
    else:
     print("You typed,", equation)

while run:
    peformMath()