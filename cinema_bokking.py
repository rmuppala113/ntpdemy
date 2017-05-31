films = {
    "Sully":[16,4],
    "Shallows":[18,5],
    "Finding Dory":[8,4],
    "Premam":[22,2],
    "Bahubali":[15,10]
}

while True:
    movie = input("Which movie do you want to watch?: ").strip().title()
    if movie in films:
        age = int(input("What is your age?: ").strip())
        if age >= films[movie][0]:
            tickets = int(input("How many tickets?: ").strip())
            total_tickets = films[movie][1]
            if tickets <= total_tickets:
                print("Enjoy the film {}".format(movie))
                films[movie][1] = films[movie][1] - tickets
            else:
                print("Tickets sold out........Check next show!")
        else:
            print("Sorry, you are not allowed to watch this movie")
    else:
        print("Sorry,{} movie is not showing in this Theatre".format(movie))
