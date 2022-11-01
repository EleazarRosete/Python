import random


def expert(player):
    print("Welcome,", player, "\nThis is the Expert Level.\n"
                              "Good Luck!\n\n")
    ctr = 1
    points = 0
    print("This is a Math Quiz!\n"
          "You must be GOOD IN MATH to be a certified Pinoy!\n")
    while ctr <= 10:
        operations = ['+', '-', '*', '/']
        rand_operation = operations[random.randint(0, 3)]
        num1 = random.randint(1, 300)
        num2 = random.randint(1, 300)

        if rand_operation == '+':
            print(ctr, ".", num1, rand_operation, num2, '= ?')
            result = num1 + num2
            ans = int(input("   Enter your Answer here: "))
            ctr += 1
            if ans == result:
                points += 10
                print("Correct!\n"
                      "Points: ", points)
            else:
                if points <= 0:
                    points -= 0
                else:
                    points -= 5
                print("Correct Answer: ", result)
                print("Wrong!\n"
                      "Points: ", points)
        elif rand_operation == '-':
            print(ctr, ".", num1, rand_operation, num2, '= ?')
            result = num1 - num2
            ans = int(input("   Enter your Answer here: "))
            ctr += 1
            if ans == result:
                points += 10
                print("Correct!\n"
                      "Points: ", points)
            else:
                if points <= 0:
                    points -= 0
                else:
                    points -= 5
                print("Correct Answer: ", result)
                print("Wrong!\n"
                      "Points: ", points)
        elif rand_operation == '*':
            print(ctr, ".", num1, rand_operation, num2, '= ?')
            result = num1 * num2
            ans = int(input("   Enter your Answer here: "))
            ctr += 1
            if ans == result:
                points += 10
                print("Correct!\n"
                      "Points: ", points)
            else:
                if points <= 0:
                    points -= 0
                else:
                    points -= 5
                print("Correct Answer: ", result)
                print("Wrong!\n"
                      "Points: ", points)
        elif rand_operation == '/':
            print(ctr, ".", num1, rand_operation, num2, '= ?')
            result = num1 / num2
            ans = float(input("   Enter your Answer here: "))
            ctr += 1
            if ans == result:
                points += 10
                print("Correct!\n"
                      "Points: ", points)
            else:
                if points <= 0:
                    points -= 0
                else:
                    points -= 5
                print("Correct Answer: ", result)
                print("Wrong!\n"
                      "Points: ", points)
    else:
        print("\nQuiz Ended!")
        multiplier = random.randint(0, 2)
        if multiplier == 1:
            if points < 0:
                points = 0
            else:
                points = points
        elif multiplier == 2:
            if points < 0:
                points = 0
            else:
                points = points * 2

    print("Total points: ", points)
    return points
