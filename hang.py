import random


class Words:

    wordlist_filename = ""

    def __init__(self):
        self.wordlist_filename = "palavras.txt"

    def getWordlistFilename(self):
        return self.wordlist_filename

    def loadWords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print("Loading word list from file...")

        inFile = open(self.wordlist_filename, 'r')

        line = inFile.readline()

        wordlist = line.split()
        print("  ", len(wordlist), "words loaded.")
        return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):

    secretLetters = []

    for letter in secretWord:
        if letter in secretLetters:
            secretLetters.append(letter)
        else:
            pass

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True


def getGuessedWord():

    guessed = ''

    return guessed


def getAvailableLetters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase

    return available


def hangman(secretWord):

    guesses = 8
    lettersGuessed = []
    print('Welcome to the game, Hangam!')
    print('I am thinking of a word that is', len(secretWord), ' letters long.')
    print('-------------')

    while(not(isWordGuessed(secretWord, lettersGuessed)) and guesses > 0):
        print('You have ', guesses, 'guesses left.')

        available = getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print('Available letters', available)
        letter = input('Please guess a letter: ')
        if letter in lettersGuessed:

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print('Oops! You have already guessed that letter: ', guessed)
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print('Good Guess: ', guessed)
        else:
            guesses -= 1
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print('Oops! That letter is not in my word: ',  guessed)
        print('------------')

    else:
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
        else:
            print('Sorry, you ran out of guesses. The word was ',
                  secretWord, '.')


words = Words()

secretWord = words.loadWords().lower()
hangman(secretWord)
