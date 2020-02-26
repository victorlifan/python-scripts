from sys import exit
def happy_scale():
    print("How happy are you from scale 1~10?")
    try:
        happiness = int(input("> "))
    except ValueError:
        happy_scale()

    if happiness > 5:
        list_happy()

    else:
        list_unhappy()

def list_happy():
    print("list things you are happy with, type 'End' if you are done:")
    while True:
        list_happy = input("> ")
        if "End" in list_happy:
            enough()

def enough():
    print("Are thses enough for you? (type Yes or No)")
    while True:
        enough = input("> ")

        if "Yes" in enough:
            print("U R A LOSER! try again")

        elif "No" in enough:
            list_unhappy()

        else:
            print("Yes or No.")

def list_unhappy():
    print("What do you want in life?")
    wants = ["1. job","2. company","3. money"]
    for wish_list in wants:
        print(wish_list)
    choice = input("> ")
    if choice == "1":
        print("What kind of job?")
        input("> ")
        require()
    elif choice == "2":
        print("What compnay?")
        input("> ")
        require()
    elif choice == "3":
        how_much_money()
        require()
    else:
        require()

def how_much_money():
    print("How much?")
    try:
        how_much = int(input("> "))
    except ValueError:
        how_much_money()
    else:
        require()

def require():
    print("What do you need to do?")
    todo = ["1.study","2.move","3.both"]
    for to_do in todo:
        print(to_do)
    choice = input("> ")
    if choice == "1":
        print("then?")
        choice_1 = input("> ")
        if choice_1 == "2" or choice_1 == "3":
            win()
        else:
            require()

    elif choice == "2":
        print("then?")
        choice_1 = input("> ")
        if choice_1 == "1" or choice_1 == "3":
            win()
        else:
            require()

    elif choice == "3":
        win()

    else:
        require()

def win():
    print("dreams come true!!!!!")

happy_scale()
