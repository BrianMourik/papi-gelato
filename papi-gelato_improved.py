print("--------------------------------------------------------------------------------")
print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
print("--------------------------------------------------------------------------------")


def more(opslag):
    global repeat_whole

    repeat_this = 0
    while repeat_this == 0:

        repeat_whole = input("Hier is uw " + opslag + " met " + str(number_icecream) + " bolletje(s). Wilt u nog meer bestellen? (Y/N)")

        if (repeat_whole.lower() == "y"):
            number_bolletjes()

        elif (repeat_whole.lower() == "n"):
            return("Bedankt en tot ziens!")

        else:
            print("Sorry dat begrijp ik niet.")

def holder():
    global houder

    houder = input("Wilt u deze " + str(number_icecream) + " bolletje(s) in een hoorntje of een bakje; ")

    if (houder.lower() == "bakje" or houder.lower() == "hoorntje"):
        print(more(houder))
        if repeat_whole == "n":
            quit()
 
def number_bolletjes():
    repeat_icecream = 0

    global number_icecream

    while repeat_icecream == 0:
        number_icecream = input("Hoeveel bolletjes wilt u; ")
    
        if number_icecream.isnumeric() == False or int(number_icecream) < 0:
            print("Sorry, dat snap ik niet...")
            quit()

        number_icecream = int(number_icecream)

        if number_icecream <= 3 and number_icecream >= 0:
            holder()
    
        elif number_icecream <= 8 and number_icecream >= 4:
            print("Dan krijgt u van mij een bakje met " + str(number_icecream) + " bolletjes.")
            houder = "bakje"
            print(more(houder))
            if repeat_whole == "n":
                quit()

        elif number_icecream > 8:
            print("Sorry, zulke grote bakken hebben we niet.")

number_bolletjes()