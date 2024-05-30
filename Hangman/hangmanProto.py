import random as rand

print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

#First step

computerChoice = rand.choice(words)

#Second step

outputBlank = []
for i in range(len(computerChoice)):
    outputBlank += '_'

life = 7

while ('_' in outputBlank) and (life != 0):
    print(f"The word to guess: {''.join(outputBlank)}")
    userGuess = input("Enter a letter: ").lower()
    index = 0
    listComputerChoice = list(computerChoice)
    if userGuess in outputBlank:
        print(f"You've already guessed {userGuess}")
        
    for i in range(len(listComputerChoice)):
        letter = computerChoice[i]
        if letter == userGuess:
            outputBlank[i] = letter

    #Fifth step
    if userGuess not in computerChoice:
        print("Oops! You just lost a life!")
        print(stages[life-1])
        life -= 1
        
if life == 0:
    print("You lose!")
if ('_' not in outputBlank):
    print(f"You guessed the word {''.join(outputBlank)} correctly!")
    print("You win!")