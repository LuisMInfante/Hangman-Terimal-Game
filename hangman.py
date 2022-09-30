import random 
from stages import hangman_stages
from random_word import RandomWords


randomWords = RandomWords()


#function to select a random word from library and switch to upper case
def select_word():
    word = randomWords.get_random_word()
    return word.upper()

def play(word):
    hiddenWord = "-" * len(word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    numberOfTries = 0

    print("\n")
    print("Welcome to Hangman!")
    print(hangman_stages(numberOfTries))
    print(hiddenWord)

    while not guessed and numberOfTries < 6:
        guess = input("Please guess a letter or a word: ").upper()
        # logic for guessing a letter
        if guess.isalpha() and len(guess) == 1:
            if guess in guessedLetters:
                print("The letter " + guess + "has already been guessed!")
            elif guess not in word:
                print(guess, "is not in the word.")
                numberOfTries += 1
                guessedLetters.append(guess)
            else:
                print("Nice! " + guess + " is in the word!")
                guessedLetters.append(guess)
                # changing string to a list so that we can iterate over it
                wordAsList = list(hiddenWord)
                # using list comprehension to find the index of guessed letter
                letterLocation = [i for i, letter in enumerate(word) if letter == guess]
                for letter in letterLocation:
                    wordAsList[letter] = guess
                # changing word back to a string
                hiddenWord = "".join(wordAsList)
                # if the guess complete the word then set guessed variable to true
                if "-" not in hiddenWord:
                    guessed = True 
            
        # logic for guessing an entire word
        elif guess.isalpha() and len(guess) == len(word):
            if guess in guessedWords:
                print("The word ", guess, " was already guessed!")
            elif guess != word:
                print(guess, " is not the correct word.")
                numberOfTries += 1
                guessedWords.append(guess)
            else:
                guessed = True
                hiddenWord = word

        else:
            print("This is not a vaild guess! Try Again.")
        
        print(hangman_stages(numberOfTries))
        print(hiddenWord)
        print("\n")
        
    if guessed:
        print("Awesome! You guessed the word!")
    else:
        print("Oops! You ran out of tires... The word was " + word + ".")

def main():
    word = select_word()
    play(word)
    while input("Do you want to play again? (Y/N) ").upper() == "Y":
        word = select_word()
        play(word)

if __name__ == "__main__":
    main()