''' Meal and Tip calculator
    CTI-110 P2HW2 - Meal snd Tip calcuator
    02/11/2019
    Matthew White '''


# Meal and Tip calculator



# Ask user for price of meal

price = float(input("Enter the price of your meal: "))


# Calculate the different tip percents

tip1 = price * .15
tip2 = price * .18
tip3 = price * .20


# Display the tip amount for all 3 percents

print ("You will pay", format(tip1,'.2f'), "for a 15% tip.")
print ("You will pay", format(tip2,'.2f'), "for a 18% tip.")
print ("You will pay", format(tip3,'.2f'), "for a 20% tip.")
