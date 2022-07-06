#this robot will assist you in taking your order

print("Hello, welcome to Lotus!")

#this is just so spacing shows up nice when running the program
print()

name = input("What is your name?\n\n")

#this is just so spacing shows up nice when running the program
print()

print("Nice to meet you " + name + ", thanks for coming in today.\n")

specials = "a Banh Mi, Pho, a Skirt Steak Rice Bowl, and Fried Chicken Rolls"

print(name + ", our specials for the day are " + specials + ".")

order = input("What would you like to order?\n\n")

cost = 15.75

#this is just so spacing shows up nice when running the program
print()

quantity = input("How many would you like?\n\n")

#this is just so spacing shows up nice when running the program
print()

total = (cost * int(quantity))

print("Thank you, Your total is: $" + str(total) + ", Have a great day!")
