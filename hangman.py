import random
import string


def game_name():
    print("H A N G M A N")


def make_hint(hint, base, letter=''):
    pass
    for i in range(len(base)):
        if letter == base[i]:
            hint[i] = letter
    return hint


# Prepairing

game_name()  # Title


# Game
def game():
    word_list = 'python', 'java', 'kotlin', 'javascript'
    lives = 8
    secret_word = random.choice(word_list)  # слово загадка
    word_list = list(secret_word)  # слово в виде списка букв
    word_hint = list('-' * len(secret_word))  # слово подсказка
    letters_left = set(secret_word)
    letters_entered = set()
    user_word = ''.join(make_hint(word_hint, secret_word))

    while lives > 0:

        if user_word == secret_word:
            print(f"\n{user_word}\nYou guessed the word")
            break

        print()
        print(f"{user_word}")
        letter = input("Input a letter: ")

        if len(letter) > 1 or letter == '':
            print("You should print a single letter")
            continue
        if letter not in string.ascii_lowercase:
            print("It is not an ASCII lowercase letter")
            continue
        if letter in letters_entered:
            print("You already typed this letter")
            continue
        elif letter in letters_left:
            make_hint(word_hint, secret_word, letter)
            letters_left.remove(letter)
            letters_entered.add(letter)
        elif letter in set(secret_word):
            print("Заглушка")
        else:
            print("No such letter in the word")
            letters_entered.add(letter)
            lives -= 1
        user_word = ''.join(make_hint(word_hint, secret_word))

    if user_word != secret_word:
        print("You are hanged!")
    else:
        print("You survived!")


while True:
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == 'play':
        game()
    elif choice == 'exit':
        break
