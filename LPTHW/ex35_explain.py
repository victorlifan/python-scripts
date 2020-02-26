# call modual "sys" import function exit
from sys import exit
# crate function "gold_room"
def gold_room():
    print("This room is full of gold. How much do you take?")

    # assign input value to variable choice
    try:
        how_much = int(input("> "))
    except ValueError:
        dead("Man, learn to type a number.")

    # "if" statement: int(choice)< 50:
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        # call function "exit"
        exit(0)

    else:
        #call function "dead"
        dead("You greedy bastard!")

#crate function "bear_room" with argument()
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("Thea fat bear is in front of another door.")
    print("How are you going to move the bear?")
    # assign false to variable bear_moved
    bear_moved = False
    while True:
        # assign input value to variable "choice"
        choice = input ("> ")

        # "if" statement if choice = "take honey" is true, then run function "dead"
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")

        elif choice == "taunt bear" and bear_moved is False:
            print("The bear has moved from the door.")
            print("You can go though it now.")
            bear_moved = True

        elif choice == "taunt bear" and bear_moved is True :
            # run function "dead"
            dead("The bear gets pissed off and hews your leg off.")

        elif choice == "open door" and bear_moved is True:
            # run function "gold_room"
            gold_room()

        else:
            print("I got no idea what that means.")

#crate function "cthulhu_room"()
#def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stars at ou and you go insane.")
    print("Do you flee for your life or eat your head?")
    # assign input value to variable choice
    choice = input("> ")
    if "flee" in choice:
        # run "start" function
        start()

    elif "head" in choice:
        # run "dead" function
        dead("Well that was tasty!")

    else:
        #run "cthulhu_room" function
        cthulhu_room()

# crate function "dead" function with variable "why"
def dead(why):
    print(why,"Good job!")
    exit(0)

# crate "start" function:
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("WHich one do you take?")

    #assign input value to variable "choice"
    choice = input("> ")

    if choice == "left":
        #run function "bear_room"
        bear_room()

    elif choice == "right":
        cthulhu_room()
        
    else:
        # run "function" dead
        dead("You stuble around the room until you starve.")

#run funcion "start"
start()
