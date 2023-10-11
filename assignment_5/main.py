import random

def computer_choice():
    return random.randint(1, 3)

def game():
    game_dict = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    comp = computer_choice()
    p_choice = int(input("Pick a number between 1-3.\n1 = Rock\n2 = Paper\n3 = Scissors\nThe computer will also pick and then display if you won, lost, or tied\nYour Pick: "))
    if p_choice == comp:
        print('Tie')
    elif (p_choice - 1 == comp) or (p_choice - 1 == 0 and comp == 3):
        print("You win!")
    else: 
        print("You lost that one")
    print(f"You picked: {game_dict[p_choice]}\nComputer picked: {game_dict[comp]}")

game()