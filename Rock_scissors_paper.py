import random

player_move = input('Choose [r]ock,[p]aper or [s]cissors:')

if player_move == 'r':
    player_move = 'Rock'
elif player_move == 'p':
    player_move = 'Paper'
elif player_move == 's':
    player_move = 'Scissors'
else:
    raise SystemExit('Invalid input!Try again.')

computer_chose = random.randint(1, 3)
if computer_chose==1:
    computer_move='rock'
elif computer_chose==2:
    computer_move='scissors'
elif computer_chose==3:
    computer_move='paper'

print(f'The computer chose {computer_move}')

computer_move = ''

if (player_move == 'rock' and computer_move == 'scissors') or \
        (player_move == 'paper' and computer_move == 'rock') or \
        (player_move == 'scissors' and computer_move == 'paper'):
    print('You win!')
elif player_move==computer_move:
    print('Draw!')
else:
    print('You lose!')
