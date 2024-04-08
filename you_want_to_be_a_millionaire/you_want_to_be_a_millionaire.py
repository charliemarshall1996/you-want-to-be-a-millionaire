
"""
A quiz game implementation titled "You Want To Be A Millionaire". This game is inspired by the
famous game show where participants answer questions to win cash prizes, aiming for the grand
prize of one million dollars. The game is structured into levels with questions of increasing difficulty
and corresponding monetary values. It is designed to provide an interactive and engaging experience
for users, simulating the thrill of the actual game show.

The game begins with an introduction and a prompt asking the user if they wish to play. Upon agreeing,
the user is presented with a series of questions. Each question must be answered correctly to move on
to the next, with the monetary value of questions increasing as the game progresses. Incorrect answers
result in a game over, where the user is shown their winnings. The game features a system to clear the
screen for a clean display, simulate suspense with timed delays, and celebrate the user's win with
special messages and ASCII art if they reach the million-dollar question. 

Throughout the game play, the `YouWantToBeAMillionaire` class manages the game's state, including tracking
the user's current level, question number, and earnings. Functions within the class handle the game's
flow, from starting and playing the game to selecting and presenting questions and validating user
answers. The implementation allows for easy additions or modifications to the question set and game
dynamics, making it a versatile template for creating a quiz-based entertainment application.


"""


import time
import random
import sys
import os

from constants import *


class YouWantToBeAMillionaire:

    def __init__(self):
        self.bank = 0
        self.hand = 0
        self.lvl = 1
        self.q_num = 1
        self.LVL1 = LVL1
        self.LVL2 = LVL2
        self.LVL3 = LVL3

    def run(self):
        """
        This function is called when the user runs the game.

        The function clears the screen using the `os.system()` function,
        which runs the `cls` command on Windows or the `clear` command
        on Linux/Mac. It then prints the introduction message and the
        dollar sign to the console.

        The function then asks the user if they want to play the game
        by using the `input()` function. The `input()` function returns
        a string, so we call the `lower()` method on the string to convert
        it to lowercase. We then check if the user entered `"y"` or `"yes"`
        (case insensitive) and if so, call the `_play()` function to start
        the game. If the user does not want to play, the function calls
        the `sys.exit()` function to exit the program.
        """
        # Clear the screen
        os.system('cls')

        # Print the introduction message
        # and the dollar sign
        print(INTRO)
        print(DOLLAR_SIGN)

        # Ask the user if they want to play
        play = input("Would you like to play? ([y]/n): ").lower() or "y"
        if play in ["y", "yes"]:
            self._play()
        else:
            sys.exit()

    def _play(self):
        """
        This function is called when the user
        wants to play the game.
        """
        # While the accumulated money
        # is less than 1 million
        while self.hand < 1000000:
            # Clear the screen
            os.system('cls')

            # Ask a question
            q = self._q()

            # Check if the answer is correct
            if self._a(q):  # If Correct answer
                self.q_num += 1  # Increment the question number

                # Print the correct message
                print(f"CORRECT! You have ${MONEY[self.hand]}!")
                time.sleep(0.5)

                # Increase the money
                self.hand = MONEY[self.hand]

            else:  # If Wrong answer
                # Print the lose message
                print("Wrong answer. You lose.")

                # Print the amount in the bank
                print(f"You took home ${self.bank}")

                # Print the losing face
                print(LOSING_FACE)

                # Reinitialize the game
                time.sleep(3)
                self._reset()
                break

        if self.hand == 1000000:
            print("You have won the million dollars!!!")
            time.sleep(0.5)
            os.system('cls')
            print("***CONGRATULATIONS****")
            time.sleep(0.5)
            os.system('cls')
            print(CROWN)
            time.sleep(0.5)
            print(WIN_MESSAGE)
            time.sleep(3)
            self._reset()

        # Clear the screen
        os.system('cls')

        # Run game menu
        self.run()

    def _a(self, q):
        """
        This function retrieves the user's answer to a question,
        checks if the answer is valid, and returns a boolean value
        indicating whether the answer is correct or not.

        The function first retrieves the user's answer to the question
        by using the `input()` function. The `input()` function returns
        a string, so we call the `lower()` method on the string to convert
        it to lowercase. We then call the slice notation `[:1]` on the
        string to retrieve the first character of the string. This
        will give us the user's answer as a single character. For example,
        if the user types `"A"` as their answer, the answer will be `"a"`.

        After retrieving the user's answer, the function checks if the
        answer is valid. An answer is considered valid if it is one of the
        four letters `"a"`, `"b"`, `"c"`, or `"d"`. If the answer is not valid,
        the function prints an error message and calls itself again to ask
        the question again.

        If the answer is valid, the function checks if the answer is correct
        by comparing the user's answer to the correct answer stored in the
        `"answer"` key of the question dictionary `(q)`. If the two answers match,
        the function returns True. If the two answers do not match, the function
        returns False.

        The main reason we need to check if the answer is valid is because
        we don't want to allow the user to enter any random string of characters
        as their answer. We only want to allow the user to enter a single
        character from the set `"a"`, `"b"`, `"c"`, or `"d"`.

        Returns:
        --------
        - bool: `True` if the answer is correct, `False` if the answer is wrong.
        """

        # Retrieve user answer
        answer = input("Answer: ").lower()[:1]

        # Check if answer is valid
        if answer not in 'abcd':  # If answer is not valid
            print("Please enter a valid answer.")  # Print error message
            return self._a(q)  # Ask question again

        # Check if answer is correct
        return answer == q['answer']  # Return True if correct, False if wrong

    def _q(self):
        """
        Select a random question from the appropriate level.

        This function randomly selects a question from one of
        the three levels (lvl1, lvl2, lvl3) based on the
        current question number (q_num).

        The question is selected from the corresponding level
        (lvl1, lvl2, or lvl3) and then printed to the console
        along with the amount of money the player has 
        ($100, $200, $300, etc.) and the options for the
        question (a, b, c, or d).

        Returns:
        --------
        - dict: A single question from the appropriate level
        """

        # Randomly select a question from the appropriate level
        if self.q_num <= 5:  # If the current question number is <= 5
            # Select a question from lvl1
            q = self.LVL1.pop(random.randint(0, len(self.LVL1)-1))
        elif self.q_num > 5 and self.q_num <= 10:  # If the current question number is > 5 and <= 10
            # Select a question from lvl2
            q = self.LVL2.pop(random.randint(0, len(self.LVL2)-1))
        else:  # If the current question number is > 10
            # Select a question from lvl3
            q = self.LVL3.pop(random.randint(0, len(self.LVL3)-1))

        # Print the question number and amount of money
        print(f"Question {self.q_num-1}. For ${MONEY[self.hand]}:")
        print(q['question'])  # Print the question
        # Print the options for the question
        print(f"a: {q['a']}, b: {q['b']}, c: {q['c']}, d: {q['d']}")

        return q  # Return the selected question

    def _reset(self):
        # Reinitialize the game
        self.bank = 0
        self.hand = 0
        self.lvl = 1
        self.q_num = 1
        self.LVL1 = LVL1
        self.LVL2 = LVL2
        self.LVL3 = LVL3


if __name__ == "__main__":
    app = YouWantToBeAMillionaire()
    app.run()
