
import time
import random
import sys

LVL1 = [{'question': 'What is the capital of France?', 'a': 'Paris',
         'b': 'London', 'c': 'Berlin', 'd': 'Madrid', 'answer': 'a'},
        {'question': 'How many continents are there on Earth?',
         'a': '5', 'b': '6', 'c': '7', 'd': '8', 'answer': 'c'},
        {'question': 'What gas do plants breathe in that humans and animals breathe out?',
         'a': 'Nitrogen', 'b': 'Oxygen', 'c': 'Carbon Dioxide', 'd': 'Argon', 'answer': 'c'},
        {'question': "Which of these is a well-known children's book by Dr. Seuss", 'a': 'Moby Dick',
         'b': 'Huckleberry Finn', 'c': 'Alice in Wonderland', 'd': 'The Cat in the Hat', 'answer': 'd'},
        {'question': 'Which of these is not a prime number?',
         'a': '2', 'b': '3', 'c': '5', 'd': '7', 'answer': 'a'}
        ]
LVL2 = [{'question': 'Which of these chemical elements is NOT a noble gas?', 'a': 'Neon', 'b': 'Argon', 'c': 'Mercury', 'd': 'Xenon', 'answer': 'c'},
        {'question': 'In Which Year did the Berlin Wall Fall', 'a': '1987',
            'b': '1988', 'c': '1989', 'd': '1990', 'answer': 'c'},
        {'question': "'The Scream' is a famous painting by which artist?", 'a': 'Edvard Munch',
            'b': 'Piet Mondrian', 'c': 'Salvador Dali', 'd': 'Edvard Munch', 'answer': 'a'},
        {'question': 'Which novel features the character Atticus Finch?', 'a': 'The Catcher in the Rye',
            'b': 'The Great Gatsby', 'c': 'To Kill a Mockingbird', 'd': 'Pride and Prejudice', 'answer': 'b'},
        {'question': 'The term "piano" is short for pianoforte, a word that in Italian means what?', 'a': 'Softly played', 'b': 'Loud and strong', 'c': 'Soft and loud', 'd': 'Quickly with spirit', 'answer': 'c'}]

LVL3 = [{'question': "The principle of 'Pareto Efficiency' is most closely associated with which field of study?", 'a': 'Physics', 'b': 'Chemistry', 'c': 'Mathematics', 'd': 'Economics', 'answer': 'd'},
        {'question': 'Who wrote the epic poem Paradise Lost?', 'a': 'William Shakespeare',
            'b': 'John Keats', 'c': 'John Milton', 'd': 'Geoffrey Chaucer', 'answer': 'c'},
        {'question': "Which element has the highest melting point of all metallic elements?",
            'a': 'Iron', 'b': 'Tungsten', 'c': 'Platinum', 'd': 'Uranium', 'answer': 'b'},
        {'question': "What is the term for a word that is similar in meaning to another word?",
            'a': 'Antonym', 'b': 'Synonym', 'c': 'Homonym', 'd': 'Hyponym', 'answer': 'b'},
        {'question': 'The Battle of Hastings in 1066 was fought in which country?', 'a': 'England', 'b': 'Scotland', 'c': 'France', 'd': 'Ireland', 'answer': 'a'}]

MONEY = {
    0: 100,
    100: 200,
    200: 300,
    300: 500,
    500: 1000,
    1000: 2000,
    2000: 4000,
    4000: 8000,
    8000: 16000,
    16000: 32000,
    32000: 64000,
    64000: 125000,
    125000: 250000,
    250000: 500000,
    500000: 1000000
}

LOSING_FACE = """
⡴⠒⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠉⠳⡆⠀
⣇⠰⠉⢙⡄⠀⠀⣴⠖⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠁⠙⡆
⠘⡇⢠⠞⠉⠙⣾⠃⢀⡼⠀⠀⠀⠀⠀⠀⠀⢀⣼⡀⠄⢷⣄⣀⠀⠀⠀⠀⠀⠀⠀⠰⠒⠲⡄⠀⣏⣆⣀⡍
⠀⢠⡏⠀⡤⠒⠃⠀⡜⠀⠀⠀⠀⠀⢀⣴⠾⠛⡁⠀⠀⢀⣈⡉⠙⠳⣤⡀⠀⠀⠀⠘⣆⠀⣇⡼⢋⠀⠀⢱
⠀⠘⣇⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⡴⢋⡣⠊⡩⠋⠀⠀⠀⠣⡉⠲⣄⠀⠙⢆⠀⠀⠀⣸⠀⢉⠀⢀⠿⠀⢸
⠀⠀⠸⡄⠀⠈⢳⣄⡇⠀⠀⢀⡞⠀⠈⠀⢀⣴⣾⣿⣿⣿⣿⣦⡀⠀⠀⠀⠈⢧⠀⠀⢳⣰⠁⠀⠀⠀⣠⠃
⠀⠀⠀⠘⢄⣀⣸⠃⠀⠀⠀⡸⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠈⣇⠀⠀⠙⢄⣀⠤⠚⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⢘⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢰⣿⣿⣿⡿⠛⠁⠀⠉⠛⢿⣿⣿⣿⣧⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⣸⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡀⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠹⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡿⠁⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣤⣞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⣀⣠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⢤⣀⣀⠀⢀⣀⣀⠤⠒⠉⠀⠀⠀⠀⠀⠀
"""

WINNING_FACE = """
                     $$$$$$$$$$$$$$$$$$$$$$
                  $$$$$$$$$$$$$$$$$$$$$$$$$$$$
                $$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$
               $$$$$$$$$$$$$$  $$$$$$$  $$   $ $$$$
             $$$$$$$$$$$   $$   $$$  $$  $   $  $$$$
            $$$$%$$$  $ $   $$   $$$  $  $   $$ $ $$
           $$$$%%$$$   $ $   $$   $$$  $  $$  $ $ $$$
          $$$$$%%$$$$  $ $    $    $$  $  $$$ $ $$ $$$$
         $$$$$%%%$$$$$ $$$$   $  $ $$   $ $$$$$ $$ $$$$$
        $$$$$$%%%$$$$$$$$$$$  $$ $ $$$$ $ $$$$$$$$$$$$$$$$
       $$$$$$%%%$$$$$$$$$$$$$$$ $$$$$$ $$$$$$$$$$$$$$$$$$$
      $$$$$$%%%$$%%%%%%$$$$$$$$$$$$$$$ $$$$$$$$$   $$$$$$$$
      $$$$$$%%$$%%%%%%%%%$$$$$$$$$$$$$ $$$$$$$     $$$$%$$$
      $$$$$$%$$%%%%%%%%%%%$$$$$$$$$$$$$$$$$        $$$$%%$$$
      $$$$$$$$%%%%%%%%%%%%%$$$$$$$$$$$             $$$$%%$$$
     $$$$$$$%%%            $$$$$$$$                 $$$%%$$$
     $$$$$$%%%                                      $$$%%$$
     $$$$$$%%%                                      $$$%%$$
     $$$$$%%%%                                    % $$$%%$$
     $$$$$%%%%                                    %  $$%%$$
     $$$$$%%%%                                    %  $$%%$$
     $$$$$%%%%                                   %%  $$$%$$
     $$$$$%%%%                                  %%%  $$$%$$
     $$$$$%%%%                                   %%  $$$%$$
     $$$$$%%%%                                   %%  $$$%$$
     $$$$$%%%%                                   %%  $$$%$$
      $$$$%%%%                             $$$$  %% $$$$%$$
     $ $$$%%%% $$$$$$$$$                $$$$$$$$$%% $$$$$$$
    $$$ $$%%%  $$$$$$$$$$              $$$$$$$$$$$%% $$$$$$
    $$$$  %%%          $$$           $$$$       $$%% $$$$$$
    $$$$$$%%%    $$$$$ $$$$         $$$$$$$$$$   $%% $$$$$$
     $$$$ %%%  $$$     $$$$$       $$$$$$    $$$  %%% $$$$$
     $$$$     $$$$$$$$$ $$$$      $$$$$$$$$$$$$$   %  $$$$$
     $$$$     $$$  $ $$  $$$$    $$$$$$  $ $  $$      $$$$
     $$$$      $   $$$ %%%$$$         %% $$$          $$$$
     $$$$             %%%% $$         %%%%%%  %%%     $$$$
      $$$$      %%% %%%%%   $           %%%%%%%       $$$$
      $$$$        %%%%%    $$             %%%         $$ $
      $$ $          %%     $                          $ $$
      $ $$                 $                          $  $
      $ $$  $             %$                         $$  $
      $  $  $            %%$                          $$$$
       $$$  $$         $ %%%                       $ $ $$
        $$  $$        $ %%%%          $ $$$       $$ $
         $ $$$     $$  %%%%        $$$  $$$     $$$ $
         $ $$$    $$  %%%$$$     $$$$    $$$$  $$$$ $
         $$$$$$$$$$   $$$$$$$$$$$$$$      $$$$$$$$$ $
          $$$$$$$   $$$$$$$$$$$$$$         $$$$$$$$ $
          $$$$$$ %%$$$$$$$$$$$$$$      $$$$$$$$$$$$$$
          $$$ $$  %$$$$$$$$$$      $$$$$$$$$    $$$$
           $$  $   $$$$     $$$$$$$$    $$      $$$
           $$  $   %$$$$               $$      $$$$
            $  $   %%%%$$$ $$$$$$$$$$$$$       $$$
            $$ $$   %%%%             $$       $$$$
            $$ $$    %%$$$$ $$$$$$$$$$        $$$
             $  $    $$$$$%%%%%%%%%%         $$$$
             $$ $$  $$$$$%%%                 $$$
              $  $ $$$$ %%%%%%%%%%%%%%      $$$
              $$  $$$$  %%%%%%%%%%%%%       $$$
     $$$       $ $$$$   $%%%%              $$$
   $$   $$      $$$$$  $$$$               $$$
  $  $$  $$   $$$$$$   $$$                $$$
 $ $$$$  $$  $$$$$$   $$$$               $$$
$  $$$  $$$ $$$$$$ $$$$$$$              $$$
$      $$$$$$$$$$   $$$$$$             $$$
$  $$   $$$$$$$$     $$$$$$$$$$$$$$$  $$$
$$$$$   $$$$$$$       $$$$$$$$$$$$$$$$$$
$$$$$$   $$$$$                  $$$$$$
 $$$$$   $$$$
 $$$$$$  $$$
  $$$$$  $$$
   $$$$$$$$
    $$$$$$

"""

DOLLAR_SIGN = """
              ⠀⠀⠀⠀⣀⣼⣿⣿⣧⣀⠀⠀⠀⠀
            ⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣦⣰⠀
            ⠠⣿⣿⣿⠟⢿⣿⣿⣿⢻⣿⣿⣷⡀
            ⢀⣿⣿⣿⣄⣸⣿⣿⡇⠐⢿⣿⣿⠃
            ⠀⢻⣿⣿⣿⣿⣿⣿⣯⣤⣀⠀⠈⠀
            ⠀⠀⠋⢻⠿⣿⣿⣿⣿⣿⣿⣿⣍⠀
            ⠀⠀⢤⠀⠀⢺⣿⣿⡿⠿⣿⣿⣿⣧
            ⣿⣿⣿⣧⠀⢸⣿⣿⡇⠀⢟⣿⣿⣿
            ⠸⣿⣿⣿⣧⣽⣿⣿⣷⣠⣿⣿⣿⡏
            ⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀
            ⠀⠀⠀⠘⠉⢻⣿⣿⡟⠙⠉⠁
                    """

CROWN = '''
                                    o
                                   $""$o
                                  $"  $$
                                   $$$$
                                   o "$o
                                  o"  "$
             oo"$$$"  oo$"$ooo   o$    "$    ooo"$oo  $$$"o
o o o o    oo"  o"      "o    $$o$"     o o$""  o$      "$  "oo   o o o o
"$o   ""$$$"   $$         $      "   o   ""    o"         $   "o$$"    o$$
  ""o       o  $          $"       $$$$$       o          $  ooo     o""
     "o   $$$$o $o       o$        $$$$$"       $o        " $$$$   o"
      ""o $$$$o  oo o  o$"         $$$$$"        "o o o o"  "$$$  $
        "" "$"     """""            ""$"            """      """ "
         "oooooooooooooooooooooooooooooooooooooooooooooooooooooo$
          "$$$$"$$$$" $$$$$$$"$$$$$$ " "$$$$$"$$$$$$"  $$$""$$$$
           $$$oo$$$$   $$$$$$o$$$$$$o" $$$$$$$$$$$$$$ o$$$$o$$$"
           $"""""""""""""""""""""""""""""""""""""""""""""""""""$
           $"                                                 "$
           $"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$
'''

WIN_MESSAGE = """
┌────────────────────────────────────────────────────────────┐
│ _ _  ___  _ _  _ ___  ___   ___                            │
│| | || . || | ||/| . \| __> | . |                           │
│\   /| | || ' |  |   /| _>  |   |                           │
│ |_| `___'`___'  |_\_\|___> |_|_|                           │
│                                                            │
│ __ __  _  _    _    _  ___  _ _  ___  _  ___  ___  _  _  _ │
│|  \  \| || |  | |  | || . || \ || . || || . \| __>| || || |│
│|     || || |_ | |_ | || | ||   ||   || ||   /| _> |_/|_/|_/│
│|_|_|_||_||___||___||_|`___'|_\_||_|_||_||_\_\|___><_><_><_>│
└────────────────────────────────────────────────────────────┘
"""


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
        print("Let's play You Want to be a Millionaire!!")
        print(DOLLAR_SIGN)
        play = input("Would you like to play? (y/n): ")
        if play.lower() == 'y':
            self._play()
        else:
            sys.exit()

    def _play(self):

        # While the accumulated money
        # is less than 1 million
        while self.hand < 1000000:

            # Ask a question
            q = self._q()

            # Check if the answer is correct
            if self._a(q):  # If Correct answer
                self.q_num += 1  # Increment the question number

                # Bank money at $1000
                # and $64000
                if self.hand == 1000:
                    self.bank = 1000
                if self.hand == 64000:
                    self.bank = 64000

                # Increase the money
                self._increase_money()

                # Print the correct message
                print(f"Correct! You have {self.hand}")
                print(WINNING_FACE)

            else:  # If Wrong answer
                # Print the lose message
                print("Wrong answer. You lose.")

                # Print the amount in the bank
                print(f"You took home ${self.bank}")

                # Print the losing face
                print(LOSING_FACE)

                # Reinitialize the game
                self.__init__()
                break
        if self.hand == 1000000:
            print("You have won the million dollars!!!")
            time.sleep(0.5)
            print("***CONGRATULATIONS****")
            time.sleep(0.5)
            print(CROWN)
            time.sleep(0.5)
            print(WIN_MESSAGE)

        # Run game menu
        self.run()

    def _a(self, q):

        # Retrieve user answer
        answer = input("Answer: ").lower()

        # Check if answer is valid
        if answer not in ['a', 'b', 'c', 'd']:  # If answer is not valid
            print("Please enter a valid answer.")  # Print error message
            return self._a(q)  # Ask question again

        # Check if answer is correct
        if answer == q['answer']:  # If answer is correct
            return True  # Return True

        else:  # If answer is wrong
            return False  # Return False

    def _q(self):
        print(f"Question {self.q_num}.")
        print(f"For ${MONEY[self.hand]}:")

        time.sleep(0.2)

        if self.q_num <= 5:
            q = self.LVL1.pop(self.LVL1.index(random.choice(LVL1)))
        if self.q_num > 5 and self.q_num <= 10:
            q = self.LVL2.pop(self.LVL2.index(random.choice(LVL2)))
        if self.q_num > 10:
            q = self.LVL3.pop(self.LVL3.index(random.choice(LVL3)))

        print(q['question'])
        time.sleep(0.5)
        print(f"a: {q['a']}")
        time.sleep(0.5)
        print(f"b: {q['b']}")
        time.sleep(0.5)
        print(f"c: {q['c']}")
        time.sleep(0.5)
        print(f"d: {q['d']}")
        time.sleep(0.5)
        return q

    def _increase_money(self):
        self.hand = MONEY[self.hand]


if __name__ == "__main__":
    app = YouWantToBeAMillionaire()
    app.run()
