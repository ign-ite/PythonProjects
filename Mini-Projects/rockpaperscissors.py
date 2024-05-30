import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

compChoices = [rock, paper, scissors]
compChoice = random.randint(0, 2)
print("Welcome to Rock, Paper, Scissors!")
userChoice = int(input("Enter your choice 0 for Rock, 1 for Paper, 2 for Scissors: \n"))
#Rules for Rock Paper Scissors
#1.Rock >> Scissors , Rock == Rock, Rock << Paper
if (userChoice == 0):
    if (compChoice == 0):
        print(f"Computer chose {compChoices[0]}\nUser chose {compChoices[0]}\nIt is a draw!")
    elif (compChoice == 1):
        print(f"Computer chose {compChoices[1]}\nUser chose {compChoices[0]}\nOops! Computer Won, Better luck next time!")
    else:
        print(f"Computer chose {compChoices[2]}\nUser chose {compChoices[0]}\nUser Won!")
if (userChoice == 1):
    if (compChoice == 0):
        print(f"Computer chose {compChoices[0]}\nUser chose {compChoices[1]}\nUser Won!")
    elif (compChoice == 1):
        print(f"Computer chose {compChoices[1]}\nUser chose {compChoices[1]}\nIt is a draw!")
    else:
        print(f"Computer chose {compChoices[2]}\nUser chose {compChoices[1]}\nOops! Computer Won, Better luck next time!")
if (userChoice == 2):
    if (compChoice == 0):
        print(f"Computer chose {compChoices[0]}\nUser chose {compChoices[2]}\nOops! Computer Won, Better luck next time!")
    elif (compChoice == 1):
        print(f"Computer chose {compChoices[1]}\nUser chose {compChoices[2]}\nUser Won!")
    else:
        print(f"Computer chose {compChoices[2]}\nUser chose {compChoices[2]}\nIt is a draw!")
