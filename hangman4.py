import random


def show_char(hidden_word, chars):
    result = []
    for ch in hidden_word:
        if ch in chars:
            result.append(ch)
        else:
            result.append('-')
    return ''.join(result)


def validate(char, chars):
    if len(char) != 1:
        return 'You should print a single letter'

    if not char.isalpha() or not char.islower():
        return 'It is not an ASCII lowercase letter'

    if char in chars:
        return 'You already typed this letter'

    return None


def play_game():
    hidden_words = ['python', 'java', 'kotlin', 'javascript']
    hidden_word = random.choice(hidden_words)
    display = '-' * len(hidden_word)
    chars = set()
    attempts = 8
    while attempts != 0:
        print()
        print(display)
        if display == hidden_word:
            print('You guessed the word!')
            print('You survived!')
            break

        char = input('Input a letter:')
        error = validate(char, chars)
        if error:
            print(error)
            continue

        chars.add(char)
        if char in hidden_word:
            display = show_char(hidden_word, chars)
        else:
            print('No such letter in the word')
            attempts -= 1

    if attempts == 0:
        print('You are hanged!')


# Write your code here
print('H A N G M A N')
while True:
    command = input('Type "play" to play the game, "exit" to quit:')
    if command == 'exit':
        break
    elif command == 'play':
        play_game()
    else:
        continue
