import random
import sys
import string


class Words:

    def __init__(self):
        self.wordlist_filename = "words.txt"

    def getWordlistFilename(self):
        return self.wordlist_filename

    def loadWords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print("Loading word list from file...")

        try:
            inFile = open(self.wordlist_filename, 'r')

        except FileNotFoundError:
            print("File", self.wordlist_filename, "not found!")
            sys.exit(0)

        line = inFile.readline()

        if not line:
            print("Words not found!")
            sys.exit(0)

        wordlist = line.split()

        print("  ", len(wordlist), "words loaded.")

        return wordlist


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


class Letter:

    def __init__(self):
        # 'abcdefghijklmnopqrstuvwxyz'
        self.alfa = string.ascii_lowercase

    def getAlfa(self):
        return self.alfa

    def showAlfa(self, available):
        print('Available letters', available)

    def letterDif(self, alfa, secretWord):
        count_letter = 0

        for letter in secretWord:
            if letter in alfa:
                count_letter = count_letter + 1
                alfa = alfa.replace(letter, '')

        return count_letter


def hangman():
    # Creating objects ---------------------
    words = Words()
    guess_what = GuessWhat()
    available_letter = Letter()

    secretWord = ''
    letters_dif = 27
    alfa = available_letter.getAlfa()
    guesses = guess_what.getGuesses()

    wordlist = words.loadWords()

    # verificar se todas as palavras do arquivo tem a quantidade de
    # letra maior que o número de tentativas
    while letters_dif > guesses:
        secretWord = random.choice(wordlist).lower()
        letters_dif = available_letter.letterDif(alfa, secretWord)

    lettersGuessed = []

    print('Welcome to the game, Hangam!')
    print('I am thinking of a word that is', len(secretWord), ' letters long.')
    print(letters_dif, "different letters in word!")
    print('-------------')

    while(not(guess_what.isWordGuessed(secretWord, lettersGuessed))
          and guesses > 0):

        guesses = guess_what.getGuesses()
        guess_what.showGuesses(guesses)

        alfa = available_letter.getAlfa()

        for letter in alfa:
            if letter in lettersGuessed:
                alfa = alfa.replace(letter, '')

        available_letter.showAlfa(alfa)

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
        
        elif letter not in string.ascii_lowercase:
            print("Please, enter only one letter")

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
