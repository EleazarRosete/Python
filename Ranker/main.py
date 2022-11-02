import levelFour
import levelThree
import person
import levelOne
import levelTwo

points = 0
rank = "Apprentice"

print("\nWelcome to Ranker Story!\nPlease start by creating your player!\n")

username = input("Enter a username: ")
age = int(input("How old are you? "))

player = person.player(username, age)

while True:
    option = int(input("\n\n1.Start Being an Ranker\n2.Show Stats\n0.Quit\nYou "
                       "will: "))
    if option == 1:
        print("\nStart earning points to rank up!")
        if rank == "Apprentice":
            points += levelOne.apprentice(username)
        elif rank == "Expert":
            points += levelTwo.expert(username)
        elif rank == "Master":
            points += levelThree.master(username,points)
        elif rank == "Ranker":
            points += levelFour.ranker(username, points)
    elif option == 2:
        if points >= 200:
            rank = "Ranker"
            show = person.stats(username,age,points,rank)
        elif points >= 100:
            rank = "Master"
            show = person.stats(username,age,points,rank)
        elif points >= 30:
            rank = "Expert"
            show = person.stats(username,age,points,rank)
        elif points < 0:
            points = 0
        else:
            show = person.stats(username,age,points,rank)
    elif option == 0:
        break
    else:
        print("\n\n\nInvalid!!\n\n\n")
