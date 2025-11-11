response = input("Would you like some food? (Y/N) ")

if response == "Y":
    print("Here is some food!")
else:
    print("No food for you!")  

name = input("What is your name? ")

if name=="":
    print("You didn't enter a name!")
else:
    print(f"Hello, {name}!")
