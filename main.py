from random import randint
import emoji


def user_interface(weapons_list: list):
    """
        Function that prints all available weapons in the game and their number,
        you need this number to choose the correct weapon and ask you to choose one weapon.
        returns integer number
    """

    print(emoji.emojize('Welcome to Rock, Paper, Scissors.\nPlease pick your weapon. :thumbs_up:\n'))
    for index, weapons in enumerate(weapons_list):
        print(f'{index + 1} = {weapons}')

    player_choice = int(input("\nWhat do you choose? "))
    return player_choice


def random_choice(n: int):
    """
        Function generate random choice for 'AI'
        returns integer
    """
    return randint(1, n)


def win_checker(weapons: list, player: int, rand: int) -> str:
    """
        Function calculates who win the game.
        returns string
    """
    if player == rand:
        return "It\'s a tie"
    elif (player == 0 and rand == len(weapons) - 1) or (
            player > rand and not (player == len(weapons) - 1 and rand == 0)):
        return 'Player Won'
    return 'Player Lost'


def game():
    weapons = ['Rock', 'Paper', 'Scissors']  # All weapons in the game

    ai_choice = random_choice(len(weapons))
    user = user_interface(weapons)

    print(f"                    You choose <<{weapons[user - 1]}>>")
    print(f"Artificial Intelligence choose <<{weapons[ai_choice - 1]}>>")

    rezults = win_checker(weapons, user, ai_choice)
    print(f"\n{rezults}")


def main():
    play_again = ''
    while play_again.lower() != 'n':
        game()
        print(f'Do you want to play again? ')
        play_again = input('type \'y\' for yes or \'n\' for no: ')


if __name__ == '__main__':
    main()
