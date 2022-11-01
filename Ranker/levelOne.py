import random


def apprentice(player):
    print("Welcome", player, "\nThis is the Apprentice Level.\n"
                             "Good Luck!\n\n")

    hand = ["Rock", "Paper", "Scissor"]
    print("This game is called \"Bato-Bato Pick\"\n"
          "You must be at Guessing!\n")

    ctr = 1
    points = 0

    while ctr <= 10:
        botAttack = hand[random.randint(0, 2)]
        userAttack = int(input("\nChoose your attack:\n"
                               "1.Rock\n"
                               "2.Paper\n"
                               "3.Scissor\n"
                               "Your attack is: "))

        print("Bot Attack:", botAttack)

        # user attack
        if userAttack == 1:
            userAttack = "Rock"
            print("User Attack:", userAttack)
            ctr += 1
        elif userAttack == 2:
            userAttack = "Paper"
            print("User Attack:", userAttack)
            ctr += 1
        elif userAttack == 3:
            userAttack = "Scissor"
            print("User Attack:", userAttack)
            ctr += 1
        else:
            print("\n\nInvalid!\n\n")

        if userAttack == "Rock" and botAttack == "Scissor":
            print("You win!")
            points += 20
            print(points)
        elif userAttack == "Paper" and botAttack == "Rock":
            print("You win!")
            points += 20
            print(points)
        elif userAttack == "Scissor" and botAttack == "Paper":
            print("You win!")
            points += 20
            print(points)
        elif userAttack == botAttack:
            print("Draw!")
            print(points)
        else:
            print("You lose!")
            points -= 10
            print(points)
    else:
        print("\nGame Over!\n"
              "Total points:", points)
    return points
