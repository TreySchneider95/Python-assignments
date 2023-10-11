import random

def roll_die():
    return random.randint(1, 6)

def game():
    print("Try to guess what the dice will roll\n\n")
    p_guess = int(input("Your guess: "))
    flag = True
    rolls = 1
    while flag:
        roll = roll_die()
        if roll == p_guess:
            print(f"you win it only took {rolls} rolls")
            flag = False
        else:
            print(f"Dang the die rolled a {roll}")
            input("hit enter to roll again")
            rolls += 1

game()
