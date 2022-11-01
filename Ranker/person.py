class player:
    def __init__(self, username, age):
        self.username = username
        self.age = age


class stats(player):
    def __init__(self, username, age, points, rank):
        super().__init__(username, age)
        self.points = points
        self.rank = rank
        print("\nPlayer Stats!"
              "\n   -   Username:", self.username,
              "\n   -   Age:     ", self.age,
              "\n   -   Points:  ", self.points,
              "\n   -   Rank:    ", self.rank)
