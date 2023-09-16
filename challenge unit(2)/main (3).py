class Player:
    def __init__(self, name, age, team):
        self.name = name
        self.age = age
        self.team = team

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Team: {self.team}"

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def __str__(self):
        team_info = f"Team: {self.name}\n"
        players_info = "\n".join([str(player) for player in self.players])
        return team_info + players_info
if __name__ == "__main__":
    player1 = Player("Player 1", 25, "Team A")
    player2 = Player("Player 2", 28, "Team A")
    player3 = Player("Player 3", 22, "Team B")
    player4 = Player("Player 4", 30, "Team B")
    team_a = Team("Team A")
    team_a.add_player(player1)
    team_a.add_player(player2)

    team_b = Team("Team B")
    team_b.add_player(player3)
    team_b.add_player(player4)
    print("Player Information:")
    print(player1)
    print(player2)
    print(player3)
    print(player4)

    print("\nTeam Information:")
    print(team_a)
    print(team_b)
