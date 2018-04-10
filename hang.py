import random


class Words:

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

    def __init__(self):
        self.guessed = ''
        self.guesses = 8

    def isWordGuessed(self, secretWord, lettersGuessed):

        secretLetters = []

        for letter in secretWord:
            if letter in secretLetters:
                secretLetters.append(letter)

            if not(letter in lettersGuessed):
                return False

        return True

    def guessLetter(self, guessed, secretWord, lettersGuessed):
        for letter in secretWord:
            if letter in lettersGuessed:
                guessed += letter
            else:
                guessed += '_ '
        return guessed

    def getGuesses(self):
        return self.guesses

    def putGuesses(self, guesses):
        self.guesses = guesses

    def getGuessedWord(self):
        return self.guessed

    def showGuesses(self, guesses):
        print('You have ', guesses, 'guesses left.')


class availableLetter:

    def __init__(self):
        import string
        # 'abcdefghijklmnopqrstuvwxyz'
        self.available = string.ascii_lowercase

    def getAvailableLetters(self):
        return self.available

    def showAvailable(self, available):
        print('Available letters', available)


def printWelcome(secretWord):
    print('Welcome to the game, Hangam!')
    print('I am thinking of a word that is', len(secretWord), ' letters long.')
    print('-------------')


def hangman():
    # Creating objects ---------------------
    words = Words()
    guess_what = GuessWhat()
    available_letter = availableLetter()

    secretWord = words.loadWords().lower()
    guesses = guess_what.getGuesses()
    lettersGuessed = []

    printWelcome(secretWord)

    while(not(guess_what.isWordGuessed(secretWord, lettersGuessed))
          and guesses > 0):

        guesses = guess_what.getGuesses()
        guess_what.showGuesses(guesses)

        available = available_letter.getAvailableLetters()

        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        available_letter.showAvailable(available)

        letter = input('Please guess a letter: ')
        if letter in lettersGuessed:
            guessed = guess_what.guessLetter(guess_what.getGuessedWord(),
                                             secretWord,
                                             lettersGuessed)
            print('Oops! You have already guessed that letter: ', guessed)

        elif letter in secretWord:
            lettersGuessed.append(letter)
            guessed = guess_what.guessLetter(guess_what.getGuessedWord(),
                                             secretWord,
                                             lettersGuessed)
            print('Good Guess: ', guessed)

        else:
            guess_what.putGuesses(guesses - 1)
            lettersGuessed.append(letter)
            guessed = guess_what.guessLetter(guess_what.getGuessedWord(),
                                             secretWord,
                                             lettersGuessed)
            print('Oops! That letter is not in my word: ',  guessed)

        print('------------')

    else:
        if guess_what.isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
        else:
            print('Sorry, you ran out of guesses. The word was ',
                  secretWord, '.')


hangman()
