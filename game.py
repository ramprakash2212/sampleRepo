import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playAgain = True
while playAgain:
    print("")
    playerChoice = input('Enter...\n1 for Rock,\n2 for paper\n3 for scissors\n')
    player=int(playerChoice)

    if(player < 1 or player > 3):
        sys.exit('You must choose 1,2 or 3')

    computerChoice = random.choice('123')
    computer = int(computerChoice)

    print('')
    print('You choose'+ str(RPS(player)).replace('RPS.','')+'.')
    print('Python choose'+ str(RPS(computer)).replace('RPS.','')+'.')
    print('')

    if player == 1 and computer == 3:
        print('You win')
    elif player == 2 and computer == 1:
        print('You win')
    elif player == 3 and computer == 2:
        print('You win')
    else:
        print('Python wins')        

    play = input('\nAre you play again? \npress y for yes \npress n for no\n')
    if play.lower() == 'y':
        continue
    else:
        print("\nThank you!!!")
        playAgain = False

sys.exit('Bye!!!')

