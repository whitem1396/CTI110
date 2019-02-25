''' Areas of Rectangles
    CTI-110 P3T1 Area of Rectangles
    02/25/2019
    Matthew White '''



# Ask user for length and width of 1 rectangle

width = int(input("Enter the width of the rectangle: "))
length = int(input("Enter the length of the rectangle: "))

# Calculate the area of the first rectangle
area = width * length

# Ask user for length and width of a second rectangle

width2 = int(input("Enter the width of the second rectangle: "))
length2 = int(input("Enter the length of the second rectangle: "))

# Calculate the area of the second rectangle
area2 = width2 * length2

# The If/Else statement to determine which area is bigger

if area > area2:
    print ("The first rectangle has a larger area.")
else:
    if area2 > area:
        print ("The second rectangle has a larger area.")
    else:
        if area == area2:
            print ("Both rectangles have an equal area.")
