# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word_so_far = ''
    for letter in secret_word:
        if letter not in letters_guessed:
            guessed_word_so_far += '_ '
        else:
            guessed_word_so_far += letter
    return guessed_word_so_far


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = string.ascii_lowercase
    for letter in letters_guessed:
        available_letters = available_letters.replace(letter, '')
    return available_letters


def print_number_of_guesses(number_of_guesses):
    print(f'You have {number_of_guesses} guesses left.')


def print_number_of_warnings(number_of_warnings, word):
    if number_of_warnings >= 0:
        print(f'You have {number_of_warnings} warnings left: {word}')
    else:
        print(f'You have no warnings left so you lose one guess: {word}')


def print_available_letters(available_letters):
    print(f'Available letters: {available_letters}')


def print_good_guess(word):
    print(f'Good guess: {word}')


def print_oops_guess(word):
    print(f'Oops! That letter is not in my word: {word}')


def print_opps_already_guess():
    print("Oops! You've already guessed that letter. ")


def print_opps_invalid_letter():
    print('Opps! That is not a valid letter. ')


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} long.')
    print('--------------------------')
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    guessed_word = ''
    while secret_word != guessed_word and guesses_remaining > 0:
        # print_number_of_warnings(warnings_remaining)
        print_number_of_guesses(guesses_remaining)
        print_available_letters(get_available_letters(letters_guessed))
        letter = input('Please guess a letter: ').lower()

        if letter in letters_guessed or (not str.isalpha(letter)):
            if not str.isalpha(letter):
                print_opps_invalid_letter()
            else:
                print_opps_already_guess()
            if warnings_remaining <= 0:
                guesses_remaining -= 1
            else:
                warnings_remaining -= 1
            print_number_of_warnings(warnings_remaining, guessed_word)
        else:
            letters_guessed.append(letter)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            if letter in secret_word:
                print_good_guess(guessed_word)
            else:
                if letter in ['a', 'e', 'i', 'o']:
                    guesses_remaining -= 1
                guesses_remaining -= 1

                print_oops_guess(guessed_word)
        print('------------------------')
    if guesses_remaining > 0:
        print('Congratulations, you won!')
        print(f'You total score for this game is: {guesses_remaining * len(set(secret_word))}')
    else:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}')


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word):
        return False
    for i in range(0, len(my_word)):
        if (my_word[i] != other_word[i] and my_word[i] != '_') or (my_word[i] == '_' and other_word[i] in my_word):
            return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_word = my_word.replace(' ', '')
    possible_matches = []
    for word in wordlist:
        if len(word) == len(my_word):
            match = True
            for i in range(0, len(my_word)):
                if (my_word[i] != '_' and my_word[i] != word[i]) or (my_word[i] == '_' and word[i] in my_word):
                    match = False
                    break
            if match:
                possible_matches.append(word)
    return possible_matches


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} long.')
    print('--------------------------')
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    guessed_word = ''
    while secret_word != guessed_word and guesses_remaining > 0:
        # print_number_of_warnings(warnings_remaining)
        print_number_of_guesses(guesses_remaining)
        print_available_letters(get_available_letters(letters_guessed))
        letter = input('Please guess a letter: ').lower()
        if letter == '*':
            print('Possible word matches are: ')
            print(show_possible_matches(guessed_word))
            continue
        if letter in letters_guessed or (not str.isalpha(letter)):
            if not str.isalpha(letter):
                print_opps_invalid_letter()
            else:
                print_opps_already_guess()
            if warnings_remaining <= 0:
                guesses_remaining -= 1
            else:
                warnings_remaining -= 1
            print_number_of_warnings(warnings_remaining, guessed_word)
        else:
            letters_guessed.append(letter)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            if letter in secret_word:
                print_good_guess(guessed_word)
            else:
                if letter in ['a', 'e', 'i', 'o']:
                    guesses_remaining -= 1
                guesses_remaining -= 1

                print_oops_guess(guessed_word)
        print('------------------------')
    if guesses_remaining > 0:
        print('Congratulations, you won!')
        print(f'You total score for this game is: {guesses_remaining * len(set(secret_word))}')
    else:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}')


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)
    # print(show_possible_matches('a_ pl_ '))

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
