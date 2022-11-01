import random


def ranker(player, points):
    print("\nWelcome,", player, "\nThis is the Ranker Level.\n"
                                "Good Luck!\n")
    ctr = 10
    creds = points
    print("This is the Guessing Game 2.0!\n"
          "\"Sometimes in life you need to make a decision even though you dont know if its the right decision!\"\n")

    print("Start by guessing a number that ranges from 0-500.\n"
          "You have 10 lives and each time you guess it wrong 20pts will be deducted,\n"
          "If you guess it right you will earn 100pts and attempts will reset.You can play\n"
          "as long as you have sufficient points1\n")

    randNum = random.randint(0, 500)

    while ctr >= 1:
        print("You have:", creds, "pts")
        print("You have:", ctr, "attempts")

        guess = int(input("What do you think is the number? "))
        if guess > randNum:
            print("The number is below you!")
            creds -= 20
            ctr -= 1
        elif guess == randNum:
            print("\nCongrats! You've got it right!")
            creds += 100
            ctr = 0
        elif guess < randNum:
            print("The number is above you!")
            creds -= 20
            ctr -= 1
        elif creds < 10:
            ctr = 0
        else:
            print("Invalid!")
    else:
        print("\nGame over!\n"
              "Total points:", creds)
    return creds
