def main():
  priorGuesses = []
  incorrectGuesses = 0
  word = getRandomWord()
  letters = []
  possibleLetters = "abcdefghijklmnopqrstuvwxyz"
  guessSpace = "_" * len(word)
  print(word)
  for i in word:
    letters.append(i)
  while True:
    hangmanPrint(incorrectGuesses)
    print(centerText(str("".join(guessSpace))))
    print("\nAllowed letters: " + possibleLetters) 
    guess = input("Enter your guess: ")
    while True:
      if guess in priorGuesses or len(guess) != 1 or guess.isalpha() == False:
        break
      elif guess not in letters:
        priorGuesses.append(guess)
        possibleLetters = possibleLetters.replace(str(guess),"-")
        incorrectGuesses += 1
        break
      else:
        indexOfGuess = int(word.find(str(guess)))
        guessSpace = list(guessSpace)
        guessSpace[indexOfGuess] = str(guess)
        if word.count(str(guess)) <= 2:
          indexOfGuess = int(word.find(str(guess)))
          guessSpace = list(guessSpace)
          guessSpace[indexOfGuess] = str(guess)
        "".join(guessSpace)
        break




#Input:     Takes no arguments
#Output:    Returns a random word (string) from the word list.
#Purpose:   Randomly shuffles a list of words and then selects the first word in the new list.
def getRandomWord():
   import random  #Do not remove. Will cover later in the course.
   
   randomWords = ["abode", "access", "adieu", "afar", "apace", "argosy", "arrant", "asunder", "atrabilious", "aurora", "bard", "barque", "bedizen", "beget", "behold", "beseech", "bestrew", "betide", "betoken", "blade", "blithe", "bosky", "brand", "brume", "celerity", "circumvallate", "clarion", "cockcrow", "coruscate", "crapulent", "crescent", "darkling", "dell", "dingle", "divers", "Dives", "dolour", "dome", "dulcify", "effulgent", "eld", "eminence", "empyrean", "ere", "erne", "espy", "ether", "evanescent", "farewell", "fervid", "finny", "firmament", "flaxen", "fleer", "flexuous", "fulgent", "fulguration", "fuliginous", "fulminate", "furbelow", "gird", "glaive", "gloaming", "greensward", "gyre", "hark", "horripilation", "hymeneal", "ichor", "illude", "imbrue", "impuissant", "incarnadine", "ingrate", "inhume", "inly", "ire", "isle", "knell", "lachrymal", "lacustrine", "lambent", "lave", "lay", "lea", "lenity", "lightsome", "limn", "lucent", "madding", "mage", "malefic", "manifold", "marge", "mead", "mephitic", "mere", "moon", "muliebrity", "nescient", "nigh", "niveous", "nocuous", "noisome", "nymph", "orb", "orgulous", "pellucid", "perchance", "perfervid", "perfidious", "philippic", "plangent", "plash", "plenteous", "plumbless", "poesy", "prothalamium", "puissant", "pulchritude", "purl", "quidnunc", "realm", "refulgent", "rend", "repine", "roundelay", "rubescent", "rutilant", "sans", "scribe", "sea-girt", "sempiternal", "serpent", "shade", "shore", "slay", "slumber", "steed", "stilly", "storied", "strand", "Stygian", "summer", "supernal", "susurration", "swain", "sylvan", "tarry", "temerarious", "tenebrous", "threescore", "thrice", "tidings", "toilsome", "tope", "travail", "troublous", "tryst", "unman", "vestal", "vesture", "virescent", "viridescent", "visage", "want", "wax", "wayfarer", "wed", "wind", "without", "wondrous", "wont", "wonted", "wrathful", "wreathe", "yon", "yore", "youngling", "zephyr"]
   random.shuffle(randomWords)
   return(randomWords[0])



#Input:     String to center.
#Output:    String padded with whitespace to be centered within 60 characters.
#Purpose:   Used to ensure all current information is "centered".
def centerText(string):
   return string.center(60)



#Input:     Integer for the number of current incorrect guesses.
#Output:    None
#Purpose:   Takes the number of current incorrect guesses and prints the current hangman.  Prints "Game Over" given a value of 4 or more
def hangmanPrint(incorrectGuesses):
   #Hack to "clear the screen in all OS and even IDLE"
   print('\n'*20)

   #Set default values
   prefix = ""
   output = ""
   gameOverBool = False

   #See if we are being told the game is over.
   if incorrectGuesses >= 4:
      gameOverBool = True
   #Resets a value >4 to 4 in order to prevent an IndexError.
   if incorrectGuesses > 4:
      incorrectGuesses = 4

   #The hanged man...
   incorrect = ["(_)",
                "\\|/",
                " | ",
                "/ \\"]

   #The gallows
   printList = ["     _______",
                "     |/    |",
                "    |    ",
                "    |    ",
                "    |    ",
                "    |    ",
                "    |    ",
                " ___|_   "]

   #Print loop
   for i in range(len(printList)):
      if i >= 2 and incorrectGuesses > 0:
         print(centerText(printList[i] + incorrect[i-2]))
         incorrectGuesses -= 1
      else:
         print(centerText(printList[i] + "  "))

   #Game over print
   if gameOverBool:
      print(centerText(" _____                  _____             "))
      print(centerText("|   __|___ _____ ___   |     |_ _ ___ ___ "))
      print(centerText("|  |  | .'|     | -_|  |  |  | | | -_|  _|"))
      print(centerText("|_____|__,|_|_|_|___|  |_____|\_/|___|_|  "))


def winnerPrint():
   print(centerText("                                   __ "))
   print(centerText(" __ __            _ _ _           |  |"))
   print(centerText("|  |  |___ _ _   | | | |___ ___   |  |"))
   print(centerText("|_   _| . | | |  | | | | . |   |  |__|"))
   print(centerText("  |_| |___|___|  |_____|___|_|_|  |__|"))
                                      

main()
