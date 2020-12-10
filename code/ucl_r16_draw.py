"""
This file contains code for the application "UEFA Champions League Round of 16 Draw".
Author: DtjiSoftwareDeveloper
"""

# Importing necessary libraries


import sys
import copy
import os
import random


# Creating static function


def clear():
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


# Creating necessary classes


class Team:
    """
    This class contains attributes of a team qualifying to the UEFA Champions League Round of 16.
    """

    def __init__(self, name, group, group_rank, country):
        # type: (str, str, int, str) -> None
        self.name: str = name
        self.group: str = group
        self.group_rank: int = group_rank
        self.country: str = country

    def clone(self):
        # type: () -> Team
        return copy.deepcopy(self)


# Creating main function used to run the application.


def main():
    """
    This main function is used to run the application.
    :return: None
    """

    print("Welcome to 'UEFA Champions League Round of 16 Draw' by 'DtjiSoftwareDeveloper'.")
    print("This application will quickly draw the round of 16 of UEFA Champions League.")
    print("Enter 'Y' for yes.")
    print("Enter anything else for no.")
    continue_using: str = input("Do you want to continue using 'UEFA Champions League Round of 16 Draw'? ")
    while continue_using == "Y":
        # Clearing command lind window
        clear()

        groups: list = ["A", "B", "C", "D", "E", "F", "G", "H"]
        group_winners: list = []
        group_runner_ups: list = []
        for i in range(8):
            print("Please enter information regarding group " + str(groups[i]) + " winner.")
            curr_group: str = groups[i]
            group_winner_name: str = input("Please enter the name of the team being group " + str(curr_group) +
                                           " winner: ")
            country: str = input("Which country is the winner of group " + str(curr_group) + " associated with: ")
            group_winners.append(Team(group_winner_name.upper(), curr_group, 1, country.upper()))
            print("\n")
            print("Please enter information regarding group " + str(groups[i]) + " runner-up.")
            group_runner_up_name: str = input("Please enter the name of the team being group " + str(curr_group) +
                                              " runner-up: ")
            country2: str = input("Which country is the runner-up of group " + str(curr_group) + " associated with: ")
            group_runner_ups.append(Team(group_runner_up_name.upper(), curr_group, 2, country2.upper()))

        # Drawing the Round of 16
        result: str = "UEFA CHAMPIONS LEAGUE ROUND OF 16 DRAW\n\n"  # initial value
        chosen_teams: list = []  # initial value
        for i in range(8):
            first_team: Team = group_runner_ups[random.randint(0, 7)]
            second_team: Team = group_winners[random.randint(0, 7)]
            while first_team.group == second_team.group or first_team.country == second_team.country or \
                first_team in chosen_teams or second_team in chosen_teams:
                first_team = group_runner_ups[random.randint(0, 7)]
                second_team = group_winners[random.randint(0, 7)]

            result += str(first_team.name) + " VS. " + str(second_team.name) + "\n"
            chosen_teams.append(first_team)
            chosen_teams.append(second_team)

        # Clearing command line window
        clear()

        # Displaying the UEFA Champions League Round of 16 Draw
        print(result)
        print("\n")

        string: str = input("")  # Asking the user to enter anything to proceed

        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        continue_using = input("Do you want to continue using 'UEFA Champions League Round of 16 Draw'? ")
    sys.exit()


if __name__ == '__main__':
    main()
