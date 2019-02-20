''' CTI 110
    P3HW2 Meal, Tip, and Tax Calulator
    02/20/2019
    Matthew White '''

# Ask user for their meal price

meal = float(input("Enter the price of your meal: "))

# Ask user for the tip percent they want to give

tip = float(input("Would you like to give a tip of .15, .18, or .20? "))
tipTotal = meal * tip

# If/elif statements depenidng on tip amount

if tip == .15:
    print("You will pay a tip of: ", format(tipTotal,'.2f'))

elif tip == .18:
    print("You will pay a tip of: ", format(tipTotal,'.2f'))

elif tip == .20:
    print("You will pay a tip of: ", format(tipTotal,'.2f'))

else:
    print ("Error, not a tip value")

# Calculating the sales tax

tax = meal * .07
print("You have a sales tax of: ", format(tax,'.2f'))

# Telling the user their total

total = meal + tipTotal + tax
print("Your meal comes out to a total of: ", format(total,'.2f'))
