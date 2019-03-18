''' P5HW1 Random Number
    Matthew White
    03/18/2019
    Random number generator '''

# Display a random number in the range of 1 to 100
import random



def get_number():
    # Get the random number
    number = random.randint(1, 100)
    # Ask the user to guess the number
    guess = int(input("Guess the number: "))
    print("The number is:", number)
    # If/Else statement depending on the users guess
    if guess > number:
        print("Too high, try again")
    else:
        if guess < number:
            print("Too low, try again")
        else:
            print("They are the same congrats!!")

def main():
    #variable to control the loop
    again = "y"
    print("Random number generator 1-100")
    # Calling the get_number function
    while again == 'y' or again == 'Y':
        get_number()
        #Want to play another game?
        again = input("Generate another number? (y = yes): ")

    
    

# Call the main function
main()
