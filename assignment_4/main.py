from random import randrange

def pick_random(max_num):
    return randrange(max_num)

def check_num(num, target):
    if num > target:
        print("The target number is smaller than that\n")
    elif num < target:
        print("The target number is larger than that\n")
    else:
        return "done"
    
def ordinal(n):
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix
    
def game():
    target = 0
    start = True
    guesses = 0
    running = True
    max_num = 0
    while running:
        if start:
            print("Welcome player! In this game you will try to guess a randomly generated number.\nThe computer will tell you each time you guess if you are to high or to low.")
            input("If you are ready hit enter to continue")
            print("\n\nPick your max number. The computer will randomly choose a number between 0 and what you pick.\nThe higher the number the more dificult it will be.")
            max_num = int(input("Max number: "))
            target = pick_random(max_num)
            start = False
        guesses += 1
        guess = int(input(f"Take your {ordinal(guesses)} guess: "))
        result = check_num(guess, target)
        if result == 'done':
            print(f"\n========================================\nCongragulations!! you figured out the number and it only took you {guesses} guesses.")
            running = False
        

game()