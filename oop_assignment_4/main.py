import random


def check_60():
    rand_num = random.randint(1, 10)
    if rand_num <= 6:
        return True
    return False

class BigCat:
    def __init__(self):
        self.speed = 5
        self.strength = 5
        self.intelligence = 5
        self.health = 5
        self.durability = 5

class Cheetah(BigCat):
    def __init__(self):
        super().__init__()
        self.speed = 75
        self.strength = 25
        self.intelligence = 25
        self.health = 25
        self.durability = 25

    def run(self, BigCat):
        if isinstance(BigCat, Lion):
            BigCat.king(self)
        elif isinstance(BigCat, Leopard):
            BigCat.attack(self)

class Lion(BigCat):
    def __init__(self):
        super().__init__()
        self.strength = 50
        self.health = 50

    def king(self, BigCat):
        if not isinstance(BigCat, Cheetah):
            BigCat.speed = 0
            BigCat.strength = 0
            BigCat.intelligence = 0
            BigCat.health = 0
            BigCat.durability = 0
        else:
            if check_60():
                self.health -= 20
            else:
                BigCat.speed = 0
                BigCat.strength = 0
                BigCat.intelligence = 0
                BigCat.health = 0
                BigCat.durability = 0


class Leopard(BigCat):
    def __init__(self):
        super().__init__()
        self.strength = 30
        self.intelligence = 30

    def attack(self, BigCat):
        if isinstance(BigCat, Lion):
            BigCat.king(self)
        else:
            BigCat.health -= 15

# test = Leopard()
# print(test.health)

def game():
    choice = int(input("Please select your big cat (1,2,3):\n1: Lion\n2: Cheetah\n3: Leopard\n"))
    player = Lion() if choice == 1 else Cheetah() if choice == 2 else Leopard()
    enemy = random.choice([x for x in [1,2,3] if x != choice])
    enemy_name = "Lion" if enemy == 1 else "Cheetah" if enemy == 2 else "Leopard"
    enemy = Lion() if enemy == 1 else Cheetah() if enemy == 2 else Leopard()
    flag = True
    print(f"your fighting a {enemy_name}")
    while flag:
        if isinstance(player, Lion):
            input("Hit enter to do your King attack")
            player.king(enemy)
        elif isinstance(player, Cheetah):
            input("Hit enter to do your run move")
            player.run(enemy)
        elif isinstance(player, Leopard):
            input("Hit enter to do your attack")
            player.attack(enemy)
        if enemy.health <= 0:
            print("you won!")
            flag = False
        elif player.health <= 0:
            print("Sorry you died")
            flag = False
        print(f"Your health: {player.health}")
        print(f"Enemy health: {enemy.health}")
    

game()
