from random import randint
from colorama import Fore
from passlib.hash import pbkdf2_sha256 as cryp

# Menu
print('Welcome to\n')
print(Fore.RED + 'Exemple Book Marks Market!')
print(Fore.RESET)
print('First of all you need to login on our server to buy something!\n')

# Classes
class Acc:

    def __init__(self, id, name, email, password):
        self.__id = randint(0, 9999999999)
        self.__name = name
        self.__email = email
        self.__password = cryp.hash(password, rounds=999999, salt_size=24)

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    def pass_check(self):
        if len(password1) >= 10:
            return True
        else:
            print(Fore.YELLOW + f'Please, you must have a +10 letters pass to continue.')
            print(Fore.RESET)
            return accregister()

class Books:

    def __init__(self, title, values, pages):
        self.title = title
        self.values = values
        self.pages = pages

    def __repr__(self):
        return self.title

    def totalvalue(self, *arg):
        return 


book1 = Books("Diary of a Wimpy Kid: Rodrick Rules", 13.88, 170)
book2 = Books("Diary of a Wimpy Kid: Dog Days", 14.90, 170)
book3 = Books("Diary of a Wimpy Kid: The Ugly Truth", 17.90, 170)
book4 = Books("Captain Underpants and the Sensational Saga of Sir Stinks-A-Lot (Captain Underpants #12)", 32.56, 35)
book5 = Books("Zac Power: Poison Island", 5.99, 138)

# User account infos
def accregister():
    global name1, email1, password1
    name1 = input('username: ')
    email1 = input('e-mail: ')    
    password1 = input('password (+10 letters): ')


try:
    accregister()
    userinfos = Acc(id, name1, email1, password1)
    userinfos.pass_check()

except (ValueError, AttributeError) as err:
    print(f"Something's wrongs: {err}")

print()
# Logged in confirmation
print(f"Congrats! your are logged as {Fore.YELLOW + f'{userinfos.name}'} #ID:{f'{userinfos.id}' + Fore.RESET}, always check your email for offers!")
print(f'Have a good shop on EBM Market!')
print(Fore.RESET)

# Shopping
cart = list()
books = [book1, book2, book3, book4, book5]
cartmode = 1
tocart = 0
        
    
def shopping():
    global cartmode, tocart
    for y in books:
        print(f"- {y.title} / Pages: {y.pages} / ${y.values}")
    print('\nCommands to navigate on our shop:\n - 0-4 to add a book in to your cart\n - tip "9" to logout\n - tip "7" to check your cart')

    while True:
        try:
            tocart = int(input("\n"))
        except (ValueError) as erra:
            print(f"Something's wrong in 'shopping' section: {erra}")
        
        # client options
        if tocart == 9:
            cartmode = False 
        elif tocart == 0 or tocart <= 4:
            cart.append(books[tocart])
            print(f"Book added! {books[tocart].title}")
        elif tocart == 7:
            print("\nThis is your actual cart:\n")
            for x in cart:
                print(f"- {x.title} / Pages: {x.pages} / ${x.values}")
            yn = input(Fore. YELLOW + "Do you still wanna buy something? y/n\n")
            if yn == "y": pass
            elif yn == "n":
                break
            else: pass
        else: pass

shopping()
print(Fore.RESET)


# Logging out


def loggout():
    print('This is your cart:')
    total = 0
    for z in cart:
        print(f"- {z.title} / Pages: {z.pages} / ${z.values}")
        total = total + z.values
    print(f"\nTotal: ${total} USD")


loggout()
