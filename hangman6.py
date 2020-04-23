from random import choice
from string import ascii_lowercase


class Word:
    print("H A N G M A N")
    list = ['python', 'java', 'kotlin', 'javascript']
    hangman = tuple(choice(list))
    hint = "-" * (len(hangman))
    letters = set(hangman)
    life = 8
    guess = None
    guess_list = []
    _exit = True

    def __init__(self):
        self.letters_list = list(ascii_lowercase)
        if self._exit:
            self.menu()
        else:
            return

    def menu(self):
        self.hangman = tuple(choice(self.list))
        self.hint = "-" * (len(self.hangman))
        self.letters = set(self.hangman)
        self.life = 8
        self.guess = None
        self.guess_list = []
        option = input('Type "play" to play the game, "exit" to quit: ')
        if option == "play":
            self.start()
        else:
            self._exit = False
            self.__init__()

    def start(self):
        if self.life == 0:
            print("You are hanged!")
            print()
            self.menu()
        elif "-" not in self.hint:
            print()
            print(self.hint)
            print("You guessed the word!")
            print("You survived!")
            print()
            self.menu()
        else:
            print()
            print(self.hint)
            self.guess = input("Input a letter: ")
            self.play()

    def play(self):
        if self.guess in self.guess_list:
            print("You already typed this letter")
            self.guess_list.append(self.guess)
            self.start()
        elif len(self.guess) > 1:
            print("You should print a single letter")
            self.start()
        elif self.guess not in self.letters_list:
            print("It is not an ASCII lowercase letter")
            self.start()
        elif self.guess in self.letters:
            c = 0
            for i in self.hangman:
                if i == self.guess:
                    self.hint = list(self.hint)
                    self.hint[c] = self.guess
                    self.hint = "".join(self.hint)
                    c += 1
                else:
                    c += 1
            self.guess_list.append(self.guess)
            self.start()
        else:
            print("No such letter in the word")
            self.guess_list.append(self.guess)
            self.life -= 1
            self.start()


Word()
