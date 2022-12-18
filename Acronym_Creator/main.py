while True:
    print("\n\"Acronym Creator\"\n")
    phrase = input("Enter Phrase: ")
    word = phrase.split(" ")
    print("- Phrase: " + phrase)
    print("- Acronym: ", end="")
    for x in word:
        print(x[0].upper(), end="")
    try:
        again = int(input("\n\nCreate Again?\n1.[Yes] 2.[No]\n-> "))
        if again == 1:
            pass
        elif again == 2:
            print("\n\"Thank You!\"")
            exit()
        else:
            print("\n\"Invalid Input\"")
    except Exception:
        print("\n\"Oops! Something Went Wrong!\"")