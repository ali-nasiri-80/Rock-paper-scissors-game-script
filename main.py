import random

from config import GAME_CHOICES, RULES, scoreboard


def get_user_choice():
    user_input = input("Enter your choice please(r,p,s):")
    if user_input not in GAME_CHOICES:
        print("oops! please enter agine")
        return get_user_choice()
    return user_input


def get_system_choice():
    return random.choice(GAME_CHOICES)


def find_winner(user, system):
    match = {user, system}
    if len(match) == 1:
        return None
    return RULES[tuple(sorted(match))]


def update_scoreboard(result):
    if result['user'] == 3:
        scoreboard['user'] += 1
        msg = 'you win'
    else:
        scoreboraed['system'] += 1
        msg = 'you lose'

    print("#" * 30)
    print("##", f'user:{scoreboard["user"]}'.ljust(24), "##")
    print("##", f'system:{scoreboard["system"]}'.ljust(24), "##")
    print("##", f'last game::{msg}'.ljust(14), "##")
    print("#" * 30)


def play():
    result = {'user': 0, 'system': 0}
    while result['user'] < 3 and result['system'] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice)
        if winner == user_choice:
            msg = 'you win'
            result['user'] += 1
        elif winner == system_choice:
            msg = 'you win'
            result['system'] += 1
        else:
            msg = 'Draw'
        print(f"user:{user_choice}\t system:{system_choice}\t result:{msg}")

    update_scoreboard(result)
    play_again = input("do you want to play again?(y/n)")
    if play_again == 'y':
        play()


if __name__ == "__main__":
    play()
