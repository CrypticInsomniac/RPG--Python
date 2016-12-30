#This program is a story RPG


#-----------------------------------Inventory-----------------------------------------#
#Blades#
Rusted_Dagger = False
Steel_Shortsword = False
Steel_Longsword = False
Steel_Broadsword = False

#-----------------------------------#
#Ranged Weapons#

#-----------------------------------#
#Armour#

#-----------------------------------#
#Potions#
Health_Potion = False
Health_Potion_Lesser = False
Health_Potion_Greater = False
#-----------------------------------#
#Books/Antiques#

#-----------------------------------#
#Specialty Items#
Poison_Dagger = False
#-----------------------------------#
#Gold#
gold = 0
#-----------------------------------#

#-----------------------------------Inventory-----------------------------------------#

#-----------------------------------Story Line----------------------------------------#
print()#this generates a new line with no text.

print("Welcome to the world of Astar")
print("---------------------------------------------------------------")
print()
print()
print("---------------------------------------------------------------")


print("Hello stranger what is your name?")
playerName = input()
print()
if playerName == "":
    playerName = "George"
    print("Dont want to tell me your name eh? I'm going to call you ")
    print(playerName + ".")
    print()

print("You have come to the world of Astar at a terrible time " + playerName + ".")
print()
print("*Mumbles* I'm eating dinner go away!")
print()
print("Oh well I guess now that your here you may as well do something")
print("First things first you must choose which direction to go:")
print()
print("You have choice of two directions")
print()
print("You can go to the East or the West.")
print("Which direction do you choose?")
print()
print("Type: 'West' or 'East'")
while True:         #Creates an Infinite Loop.
    directionChoice = input() #Sets the kingdomChoice Variable to whatever the user inputs.

    if directionChoice == "West": #Checks to see if the input is equal to "West" '==' means equal to.
        break
    if directionChoice == "west": #   This allows for the user to         #
        directionChoice = "West"  #   input "west" as a valid input       #
        break
    
    if directionChoice == "East": #Checks to see if the input is equal to "East" == means equal to.
        break
    if directionChoice == "east": #   This allows for the user to         #
        directionChoice = "East"  #   input "east" as a valid input       #
        break
    if directionChoice == "North":
        print("East or West dickhead!")
        continue
    if directionChoice == "north":
        print("East or West dickhead!")
        continue
    if directionChoice == "South":
        print("East or West dickhead!")
        continue
    if directionChoice == "south":
        print("East or West dickhead!")
        continue
    if directionChoice == "NO":
        print("YES!!!")
        input()
        quit()
        break
    if directionChoice == "No":
        print("Yes!")
        input()
        quit()
        break
    if directionChoice == "no":
        print("yes.")
        input()
        quit()
        break
    
    if directionChoice != "West": #Checks to see if the input is equal to "West" != means not equal to.
        print("Invalid Input Type: 'West' or 'East'")
        continue    #By this point if the input isn't "West" the computer will continue reading.
            
    if directionChoice != "East":#Checks to see if the input is equal to "East" != means not equal to.
        print("Invalid Input Type: 'West' or 'East'")
        continue       #By this point if the input isn't "East" the computer will go to the beginning of the loop.
            
    
print("You have chosen to go " + directionChoice + "." + "REMOVE THIS TEXT")

#-------------------------------------------------------------------------------------#
#while True:
#    if directionChoice == "west":
#        directionChoice = "West"
#        break
#    if directionChoice != "West":      This was a test to see how this may work
#        continue
#    if directionChoice == "East":
#        directionChoice = 1
#        break
#    if directionChoice != "West":
#        continue
#-------------------------------------------------------------------------------------#

print("--------------------------------------------------------------------------------")

#--Story setting--#

story = 0
if directionChoice == "West":
    story = 1

if directionChoice == "East":
    story = 2

#-----------------#

#West Storyline from here.
#--------------------------------------------------#
if story == 1:
    print("West? Herm... I see.")
    print()
    print("You begin to travel West")
    print()

##if story == 1:
##    if gold >= 0:
##        print(str(gold) + "Noot")

if story == 1:
    print("On your travels West you find a road marked with an illegible sign")
    print()
    print("Do you wish to follow the road or continue trekking through the wilderness?")
    print()
    print("Type: 'Road' or 'Wild'")
    choice = "Null"
    while True:
        choice = input()
        
        if choice == "Road":
            break
        if choice == "road":
            choice = "Road"
            break
        
        if choice == "Wild":
            break
        if choice == "wild":
            choice = "Wild"
            break

        
        if choice != "Road":
            print("Invalid Input Type: 'Road' or 'Wild'")
            continue
        if choice != "Wild":
            print("Invalid Input Type: 'Road' or 'Wild'")
            continue

    if choice == "Road":
        story = 1.1
    if choice == "Wild":
        story = 1.2

print(story)
    
input("end")

if story == 1.1 or 1.2:
    print("You have reached the end of your journey " + playerName + ".")
    input()
    quit()
#West Storyline ends here.
#--------------------------------------------------#

#East Storyline from here.
#--------------------------------------------------#
while True:
    if story != 2:
        print("Error this program is corrupted")
        input()
        quit()
    if story == 2:
        print("You begin to travel Eastwards.")
        print()
        print("Oh look an obvious pit-trap")
        print()
        print("*You fell into the pit-trap and died*")
        print("...")
        print("Dickhead!")
        print()
        input()
        quit()
        break

    

print("You have reached the end of your journey " + playerName + ".")
input("end")
quit()
#East Storyline ends here.
#--------------------------------------------------#

#-----------------------------------------------------------------------------------------------------------------------------------#
#while True:
    #input("Press Enter to Start again")
#    if 


#Courier New
#-----------------------------------Story Line----------------------------------------#
