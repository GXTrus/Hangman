import random


def check_errors(letter, word_set):
    if len(letter) != 1:
        print("You should print a single letter")
    elif ord(letter) < 97 or ord(letter) > 122:
        print("It is not an ASCII lowercase letter")
    elif letter in word_set:
        print("You already typed this letter")
    else:
        return False
    return True


def play_game():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    tries = 8
    random_word = random.choice(word_list)
    word_set = set()
    hidden_random_word = '-' * len(random_word)

    while tries > 0:
        print('\n' + hidden_random_word)
        letter = input("Input a letter: ")
        if check_errors(letter, word_set):
            continue
        else:
            word_set.add(letter)
            if letter in random_word:
                hidden_random_word = random_word
                for i in random_word:
                    if i not in word_set:
                        hidden_random_word = hidden_random_word.replace(i, '-')
                if hidden_random_word == random_word:
                    print("You guessed the word!\nYou survived!")
                    break
            else:
                print("No such letter in the word")
                tries -= 1
    else:
        print("You are hanged!")


print("H A N G M A N")

while True:
    decision = input('Type "play" to play the game, "exit" to quit: ')
    if decision == "play":
        play_game()
    elif decision == "exit":
        break
