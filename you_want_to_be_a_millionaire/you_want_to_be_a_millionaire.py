

LVL1 = {{'question': 'What is the capital of France?', 'a': 'Paris',
         'b': 'London', 'c': 'Berlin', 'd': 'Madrid', 'answer': 'a'},
        {'question': 'How many continents are there on Earth?',
         'a': '5', 'b': '6', 'c': '7', 'd': '8', 'answer': 'd'},
        {'question': 'What gas do plants breathe in that humans and animals breathe out?',
         'a': 'Nitrogen', 'b': 'Oxygen', 'c': 'Carbon Dioxide', 'd': 'Argon', 'answer': 'b'},
        {'question': "Which of these is a well-known children's book by Dr. Seuss", 'a': 'Moby Dick',
         'b': 'Huckleberry Finn', 'c': 'Alice in Wonderland', 'd': 'The Cat in the Hat', 'answer': 'd'},
        {'question': 'Which of these is not a prime number?',
         'a': '2', 'b': '3', 'c': '5', 'd': '7', 'answer': 'a'}}

LVL2 = {{'question': 'Which of these chemical elements is NOT a noble gas?', 'a': 'Neon', 'b': 'Argon', 'c': 'Mercury', 'd': 'Xenon', 'answer': 'c'},
        {'question': 'In Which Year did the Berlin Wall Fall', 'a': '1987',
            'b': '1988', 'c': '1989', 'd': '1990', 'answer': 'c'},
        {'question': "'The Scream' is a famous painting by which artist?", 'a': 'Edvard Munch',
            'b': 'Piet Mondrian', 'c': 'Salvador Dali', 'd': 'Edvard Munch', 'answer': 'a'},
        {'question': 'Which novel features the character Atticus Finch?', 'a': 'The Catcher in the Rye',
            'b': 'The Great Gatsby', 'c': 'To Kill a Mockingbird', 'd': 'Pride and Prejudice', 'answer': 'b'},
        {'question': 'The term "piano" is short for pianoforte, a word that in Italian means what?', 'a': 'Softly played', 'b': 'Loud and strong', 'c': 'Soft and loud', 'd': 'Quickly with spirit', 'answer': 'c'}}

LVL3 = {{'question': "The principle of 'Pareto Efficiency' is most closely associated with which field of study?", 'a': 'Physics', 'b': 'Chemistry', 'c': 'Mathematics', 'd': 'Economics', 'answer': 'd'},
        {'question': 'Who wrote the epic poem Paradise Lost?', 'a': 'William Shakespeare',
            'b': 'John Keats', 'c': 'John Milton', 'd': 'Geoffrey Chaucer', 'answer': 'c'},
        {'question': "Which element has the highest melting point of all metallic elements?",
            'a': 'Iron', 'b': 'Tungsten', 'c': 'Platinum', 'd': 'Uranium', 'answer': 'b'},
        {'question': "What is the term for a word that is similar in meaning to another word?", 'a': 'Antonym', 'b': 'Synonym', 'c': 'Homonym', 'd': 'Hyponym', 'answer': 'c'}, }


class YouWantToBeAMillionaire:

    def __init__(self):
        self.bank = 0
        self.hand = 0
        self.lvl = 1

    def run(self):
        print("Let's play You Want to be a Millionaire!!")

    def _a(self):
        pass

    def _q(self):
        pass

    def _increase_money(self):
        pass
