# Write your code here
from random import choice
from string import ascii_lowercase


class Hangman:
    def __init__(self):
        self.words = ["python", "java", "kotlin", "javascript"]
        self.chosen_word = choice(self.words)
        self.chosen_set = set(self.chosen_word)
        self.tried_set = set()
        self.hint = ""
        self.lives = 8
        self.word_guessed = False
        self.welcome_message = "H A N G M A N"
        self.menu_message = 'Type "play" to play the game, "exit" to quit: '
        self.victory_message = f"\n{self.chosen_word}\nYou guessed the word!\nYou survived!"
        self.defeat_message = "You are hanged!"
        self.game_state = ""

    def start(self):
        print(self.welcome_message)
        while True:
            self.game_state = input(self.menu_message)
            if self.game_state == "play":
                self.game_loop()
            elif self.game_state == "exit":
                break
            else:
                continue

    def game_loop(self):
        self.update_hint()
        while self.lives > 0:
            if self.hint == self.chosen_word:
                self.word_guessed = True
                break
            self.ask_for_letter()
        self.result()

    def update_hint(self):
        self.hint = self.chosen_word
        for char in self.chosen_set:
            self.hint = self.hint.replace(char, "-")

    def ask_for_letter(self):
        print()
        print(self.hint)
        self.check_input(input("Input a letter: "))

    def check_input(self, char):
        if self.input_error(char):
            return
        if char in self.chosen_set:
            self.tried_set.add(char)
            self.chosen_set.discard(char)
            self.update_hint()
            return
        if char in self.tried_set:
            print("You already typed this letter")
            return
        self.tried_set.add(char)
        print("No such letter in the word")
        self.lives -= 1

    @staticmethod
    def input_error(char):
        if len(char) != 1:
            print("You should print a single letter")
            return True
        if char not in ascii_lowercase:
            print("It is not an ASCII lowercase letter")
            return True

    def result(self):
        print(self.victory_message if self.word_guessed else self.defeat_message)


game = Hangman()
game.start()
