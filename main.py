class account:
    def __init__(self, fname, lname, likesCount, friendsList):
        self.fname = fname
        self.lname = lname
        self.likesCount = likesCount
        self.friendsList = friendsList

    def introduce(self):
        print("Hi! I am", self.fname, self.lname)

    def info(self):
        print("This is " + self.fname + "'s Account")
        print("Full name:" + self.fname + " " + self.lname)
        print("Likes:", self.likesCount)
        print("Friends:")
        for friend in self.friendsList:
            print(" -", friend)


x = 0
my_friends = []
firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
likes = int(input("Enter how many likes you have: "))
numOfprends = int(input("Enter how many friends you have: "))

for x in range(numOfprends):
    friends = input("Enter the full name of your friends: ")
    my_friends.append(friends)

user = account(firstname, lastname, likes, my_friends)
user.introduce()
user.info()
