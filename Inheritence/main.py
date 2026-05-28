from archer import Archer
from mage import Mage
from worrior import Warrior

print("Enter the Balzzzz Game Character Arena")
print("\nChoose Character")
print("1. Warrior")
print("2. Mage")
print("3. Archer")

choice = input("Enter choice: ")

name = input("Enter character name: ")
health = int(input("Enter health value: "))

# character selection we will do :)
if choice == "1":
    weapon = input("Enter weapon name: ")
    character = Warrior(name, health, weapon)

elif choice == "2":
    magic = input("Enter magic power: ")
    character = Mage(name, health, magic)

elif choice == "3":
    arrows = int(input("Enter number of arrows: "))
    character = Archer(name, health, arrows)

else:
    print("Invalid choice")
    exit()

# actions character do <=====|--
while True:

    print("\n===== MENU =====")
    print("1. Show Status")
    print("2. Attack")
    print("3. Exit")

    option = input("Enter option: ")

    if option == "1":
        character.status()

    elif option == "2":
        character.attack()

    elif option == "3":
        print("Exiting game, bye..... C U SOON")
        break

    else:
        print("Invalid option")

