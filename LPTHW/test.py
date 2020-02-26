print("""You enter a adrk room with two doors,
Do you go through dor #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("WHat do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    def function():
        bear = input("> ")
        if bear == "1":
            print("The bear eats your face off. Good job!")
        elif bear =="2":
            print("The bear eats your legs off. Good job!")
        else:
            print("choose from 1 or 2")
            print("1. Take the cake.")
            print("2. Scream at the bear.")
            function()
function()
