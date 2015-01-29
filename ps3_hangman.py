def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    valueToCompare=len(secretWord)
    numberOfMatches=0
    for first in secretWord:
        for second in lettersGuessed:
            if first==second:
                #print first
                #print second
                numberOfMatches+=1
                #print numberOfMatches
                break;
                
    if numberOfMatches>0:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    def emptyWords(words):
        myList=[]
        for index in range(0,len(words)):
            myList.append('_')
        return myList
        
    arrayOfEmpty=emptyWords(secretWord)
    counterOfWords=0
    numberOfMatches=0
    for first in secretWord:
        for second in lettersGuessed:
            if first==second:
                #print first
                #print second
                numberOfMatches+=1
                arrayOfEmpty[counterOfWords]=first
                #print numberOfMatches
                break;
        counterOfWords+=1
    resultToShow=''
    for rang in range(0,len(arrayOfEmpty)):
        resultToShow=resultToShow+arrayOfEmpty[rang]+' '
    return resultToShow


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet=string.ascii_lowercase
    resultCompared=''
    commons=''
    for letterGuess in lettersGuessed:
        for letter in alphabet:
            if letterGuess == letter:
                alphabet=alphabet.replace(letterGuess,'')
                break
    return alphabet
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    def reCreateWord(oldWord,listOfLetters):
        newWord=oldWord
        for letter in listOfLetters:
            newWord=newWord.replace(letter,'')
        return newWord
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is '+ str(len(secretWord)) +' letters long.'
    print '-------------'
    wordToSearch=secretWord.lower()
    wordFormatted=wordToSearch
    intentosRestantes=8
    letraIngresada=''
    listaDeLetrasIngresadas=[]
    while intentosRestantes!=0:
        print 'You have '+ str(intentosRestantes) +' guesses left.'
        print 'Available letters:', getAvailableLetters(listaDeLetrasIngresadas)
        letraIngresada=raw_input('Please guess a letter: ')
        if letraIngresada in listaDeLetrasIngresadas:
            print "Oops! You've already guessed that letter: "+getGuessedWord(wordToSearch,listaDeLetrasIngresadas)
            print '-----------'
        else:
            listaDeLetrasIngresadas.append(letraIngresada.lower())
            if isWordGuessed(wordFormatted,listaDeLetrasIngresadas)==True:
                print 'Good guess: '+ getGuessedWord(wordToSearch,listaDeLetrasIngresadas)
                print '-----------'
                wordFormatted=reCreateWord(wordToSearch,listaDeLetrasIngresadas)
                if wordFormatted=='':
                    print 'Congratulations, you won!'
                    break
            else:
                print 'Oops! That letter is not in my word: '+ getGuessedWord(wordToSearch,listaDeLetrasIngresadas)
                print '-----------'
                intentosRestantes-=1
            if intentosRestantes==0:
                print 'Sorry, you ran out of guesses. The word was '+ str(wordToSearch)+'.'
                break
import string
hangman('camel')
