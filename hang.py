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


class GuessWhat:

    guessed = ''

    def __init__(self):
        self.guessed = ''

    def isWordGuessed(self, secretWord, lettersGuessed):

        secretLetters = []

        for letter in secretWord:
            if letter in secretLetters:
                secretLetters.append(letter)

            if not(letter in lettersGuessed):
                return False

        return True

    def getGuessedWord(self):
        return self.guessed

    def getAvailableLetters(self):
        import string
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase

        return available


def printWelcome(secretWord):
    print('Welcome to the game, Hangam!')
    print('I am thinking of a word that is', len(secretWord), ' letters long.')
    print('-------------')


def hangman():

    words = Words()
    guess_what = GuessWhat()

    secretWord = words.loadWords().lower()
    guesses = 8
    lettersGuessed = []

    printWelcome(secretWord)

    while(not(guess_what.isWordGuessed(secretWord, lettersGuessed)) and guesses > 0):
        print('You have ', guesses, 'guesses left.')

        available = guess_what.getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print('Available letters', available)
        letter = input('Please guess a letter: ')
        if letter in lettersGuessed:

            guessed = guess_what.getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print('Oops! You have already guessed that letter: ', guessed)
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = guess_what.getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print('Good Guess: ', guessed)
        else:
            guesses -= 1
            lettersGuessed.append(letter)

            guessed = guess_what.getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print('Oops! That letter is not in my word: ',  guessed)
        print('------------')

    else:
        if guess_what.isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
        else:
            print('Sorry, you ran out of guesses. The word was ',
                  secretWord, '.')


hangman()
