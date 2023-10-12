class Boxer:
    def __init__(self, size, strength, wins, losses):
        self.size = size
        self.strength = strength
        self.wins = wins
        self.losses = losses
    
    def display_stats(self):
        print(f'Size: {self.size}\nStrength: {self.strength}\nWins: {self.wins}\nLosses: {self.losses}')
    
    def give_score(self):
        return self.size + self.strength + self.wins - self.losses
    
def compare_boxers(boxer_1, boxer_2, user_bet):
    winner = boxer_1 if boxer_1.give_score() > boxer_2.give_score() else boxer_2
    return winner == user_bet

def game(boxer_1, boxer_2):
    print(f"Boxer 1:\n{boxer_1.display_stats()}")
    print("\n")
    print(f"Boxer 2:\n{boxer_2.display_stats()}")
    print("\n")
    choice = input("Chose your boxer (1/2): ")
    user_bet = boxer_1 if choice == "1" else boxer_2
    print("You win!") if compare_boxers(boxer_1, boxer_2, user_bet) else print("Sorry you lost")


boxer_1 = Boxer(100, 120, 3, 4)
boxer_2 = Boxer(100, 140, 2, 6)

game(boxer_1, boxer_2)