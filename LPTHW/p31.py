myo = "make your own"
print("now lets make a new game, what kind of game would you like?")
print("1.RPG")
print("2. advanture")
print(f"3. {myo}")
kind = input("> ")
if kind == "1":
    print("what name do you want to give to it?")
    print("1. a")
    print("2. b")
    print(f"3. {myo}")
    name = input("> ")
    print(">>>>>>>>name=", name)
    if name == "1" or name =="2":
        print("<<<<<<nice choise brench")
        print("nice choise!")
    else:
        print(">>>>>> good luck brench")
        print("good luck!")
        input("> ")
elif kind == "2":
    print("how big do you want to make it?")
    print("1. 1gb")
    print("2. 2gb")
    print("3. 3gb")
    size = input("> ")
    if size =="1":
        print("ok 1gb game")
    elif size == "2":
        print("ok 2gb game")
    else:
        print("thats a little too big")
else:
    print("good luck!")
