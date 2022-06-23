#just playing around with variables
#this will be a robot order taker

print("Hello, welcome to Lotus!")

print()

name = input("What is your name?\n\n")

print()

print("Nice to meet you " + name + ", thanks for coming in today.\n")

specials = "a Banh Mi, Pho, a Skirt Steak Rice Bowl, and Fried Chicken Rolls"

print(name + ", our specials for the day are " + specials + ".")

order = input("What would you like to order?\n\n")

cost = 15.75

print()

quantity = input("How many would you like?\n\n")

print()

total = (cost * int(quantity))

print("Thank you, Your total is: $" + str(total) + ", Have a great day!")

#print("Sounds great " + name + ", your price for that will be " + total)

#print("Great! Your " + order + " will be ready shortly!")