def main ():
    print ("This program calculates gross pay")
    rate , hworked = get_info()
    gross(rate, hworked)


def get_info():
    rate = int(input("Enter pay rate: "))
    hoursworked = int(input("Enter hours worked: "))
    return rate, hoursworked
    

def gross(rate, hworked):
    grosspay = rate * hworked
    print("The gross pay is:", grosspay)
    
    

main()
