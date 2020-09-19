#!/usr/bin/env python3
"""
    - Pick Game Mode:
            - Game Mode determines if solutions are user-inputted or randomly generated
"""
from time import sleep


def get_player_mode(mode=None):
    """Gets player mode, either solo or multiplayer"""
    if mode == "1":
        print("You've chosen Solo Mode! Can you beat a computer?")
        return mode
    elif mode == "2":
        print("You've chosen Multiplayer Mode! Can you beat a human?")
        return mode
    else:
        if mode is not None:
            print("Unrecognized input. Please enter 1 or 2\n")
        mode = input("1 or 2 Players? ")
        return get_player_mode(mode)

def screen_clear():
    """Clears the screen after mode is chosen and displayed"""
    from subprocess import call
    import os
    call('clear' if os.name == 'posix' else 'cls')

def get_solution(player_mode):
    """Generates a code maker list of a possible solution"""
    from random import sample as randomizer

    # Red | Green | Blue | Yellow | Orange | Purple
    possible_inputs = "R G B Y O P".split()

    if player_mode == '2':
        solution = input("MasterMind, please enter a solution of 4 colors: ").split()
        # Check length
        if len(solution) != 4:
            print('Your input is invalid. Please enter a solution of 4 colors.\n')
            return get_solution('2')

        # Length's good, check whether the input's valid
        else:
            for i in solution:
                if i not in possible_inputs:
                    print('Your input is invalid. Please select from', possible_inputs)
                    print()
                    return get_solution('2')
        return solution

    else:
        return randomizer(possible_inputs, 4)

def mastermind():
    """ mvp """
    # Game Setup (Select Player Mode, Generate Solution, Set Guess Limit & Possible Inputs)
    mode = get_player_mode()
    sleep(2.5)
    screen_clear()
    solution = get_solution(mode)
    solution_color_distribution = {color : solution.count(color) for color in solution}
    guesses_left = 12
    possible_inputs = "R G B Y O P".split()
    dirty = 0

    # Initial prompt for CodeBreaker's first guess
    prompt = "CodeBreaker, please enter a guess of 4 colors: "

    # User Guess Loop
    while guesses_left > 0:
        dirty = 0
        white_pegs = 0
        black_pegs = 0
        unmatched = []
        user_guess = input(prompt).split()
        print(user_guess)
        if len(user_guess) != 4:
            print('Your input is invalid. Please enter a solution of 4 colors.\n')
            continue
        for i in user_guess:
            if i not in possible_inputs:
                print('Your input is invalid. Please select from', possible_inputs)
                print()
                dirty = 1
                break
        if dirty:
            continue
        user_colors = {color : user_guess.count(color) for color in user_guess}

        if user_guess == solution:
            print("You win!")
            return
        
        # Count black pegs
        for i in range(len(user_guess)):
            if user_guess[i] == solution[i]:
                black_pegs += 1

        # Count matched colors
        matched_colors = 0
        for color in solution_color_distribution.keys():
            times_in_user_input = user_colors.get(color)
            if times_in_user_input:
                times_in_solution = solution_color_distribution.get(color)
                matched_colors += min(times_in_user_input, times_in_solution)
        # Count white pegs
        white_pegs = matched_colors - black_pegs
        guesses_left -= 1
        print("White Pegs: {:d}".format(white_pegs))
        print("Black Pegs: {:d}".format(black_pegs))
        prompt = "Try again! You have {} guesses left.\nCodeBreaker, please enter a guess of 4 colors: ".format(guesses_left)

    print("You're out of guesses, you lose! Mastermind won with the solution: " + str(solution))

if __name__ == "__main__":
    mastermind()
    