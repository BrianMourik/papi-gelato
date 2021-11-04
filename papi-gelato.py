print("--------------------------------------------------------------------------------")
print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
print("--------------------------------------------------------------------------------")

number_icecream = 0


def number_bolletjes():
    global number_icecream
    number_icecream = input("Hoeveel bolletjes wilt u; ")

def cup_horn():
    global number_icecream

    if number_icecream.isnumeric() == False or int(number_icecream) < 0:
        print("Sorry, dat snap ik niet...")
        quit()
    
    number_icecream = int(number_icecream)

    if number_icecream <= 3 and number_icecream >= 0:
        input("Wilt u deze " + str(number_icecream) + " bolletje(s) in A) een hoorntje of B) een bakje; ")

    
    elif number_icecream <= 8 and number_icecream >= 4:
        print("Dan krijgt u van mij een bakje met " + str(number_icecream) + " bolletjes.")

    elif number_icecream > 8:
        print("Sorry, zulke grote bakken hebben we niet.")


number_bolletjes()
cup_horn() 