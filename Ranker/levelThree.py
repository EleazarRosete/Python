import random


def master(player, points):
    print("\nWelcome,", player, "\nThis is the Master Level.\n"
                                "Good Luck!\n")
    ctr = 1
    creds = points
    colors = ["Red", "Blue", "Yellow", "Green", "White", "Pink"]

    print("This is the Color Game!\n"
          "Sometimes in life you need to take a risk for your dreams!\n")

    while ctr <= 10:
        print("\n" + str(ctr) + ".")
        print("This are the colors you can choose:")

        # printing choices
        cnt = 1
        for color in colors:
            print("|", cnt, color, end="  | ")
            cnt += 1
        print("\nYou have a total points of", creds)
        userColor = int(input("\nEnter the number of color you want to place your bet: "))
        bet = int(input("How much would you bet for this color? "))
        luckyColor = colors[random.randint(0,5)]

        if bet > creds:
            print("\nInsufficient Creds!\n")
        elif bet == 0:
            print("\nPlace a bet!\n")
        elif bet <= creds:
            creds -= bet
            print("\nYou bet in color", colors[userColor],
                  "\nLucky Color is", luckyColor)
            if colors[userColor] == luckyColor:
                print("You win!")
                creds = creds + (bet * 2)
                ctr += 1
            else:
                print("You lose!")
                print("Points:", creds)
                ctr += 1
        else:
            print("Invalid!")
    else:
        print("\nGame Over")
        print("Total Points:", creds)
    return creds
