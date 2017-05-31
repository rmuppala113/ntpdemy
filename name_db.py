users = ["Rakesh","Nishi","Varma","Siva","Satish","Sunny","Bobby","Bunny"]

while True:
    name = raw_input("Hi, Enter your name (y/n): ").strip().capitalize()
    if name in users:
        print("Hi {}, you are in name Database ".format(name))
        removed = raw_input("Would you like to be removed (y/n): ").strip().lower()
        if removed == "y":
            print(users)
            users = users.remove('name')
            print(users)
        else:
            print("Not removed")
    else:
        print("Hi {},you are not in Database".format(name))
        add = raw_input("Would you like to be added(y/n): ").strip().lower()
        if add == "y":
            users = users.append(add)
        else:
            print("Not added")




