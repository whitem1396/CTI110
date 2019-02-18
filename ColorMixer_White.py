''' CTI - 110
    P3HW1 - Color Mixer
    02/18/2019
    Matthew White '''

# Asking user to input Colors

color1 = input("Enter a primary color: ")

color2 = input("Please enter a different primary color: ")

# If and else statements on the 1st color

if color1 == "red":
    print("The first color is red.")
else:
    if color1 == "blue":
        print("The first color is blue.")
    else:
        if color1 == "yellow":
            print("The first color is yellow.")
        else:
            print ("That is not a primary color.")

 # If and else statements on the 2nd color           

if color2 == "red":
    print("The second color is red.")
else:
    if color2 == "blue":
        print("The second color is blue.")
    else:
        if color2 == "yellow":
            print("The second color is yellow.")
        else:
            print ("That is not a primary color.")
            
# Output the result of the 2 colors mixed together            
            
if color1 == "red" and color2 == "blue":
    print("red and blue become purple.")
else:
    if color1 == "blue" and color2 == "red":
        print("blue and red become purple.")


if color1 == "red" and color2 == "yellow":
    print("red and yellow become orange.")
else:
    if color1 == "yellow" and color2 == "red":
        print("yellow and red become orange.")       


if color1 == "blue" and color2 == "yellow":
    print("blue and yellow become green.")
else:
    if color1 == "yellow" and color2 == "blue":
        print("yellow and blue become green.") 
