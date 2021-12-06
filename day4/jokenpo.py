from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computer = randint(1, 3)
count_computer, count_player = 0, 0
while True:
    player = int(input('What do you chose? Type 0 for Rock, 1 for Paper, 2 to Scissors and 3 for Quit.\n>> '))

    if player == 0 and computer == 0:
        print("Player choose Rock:")
        print(rock)
        print("Computer choose Rock:")
        print(rock)
        print("IT'S A DRAW!")
    elif player == 0 and computer == 1:
        print(f"Player choose Rock:\n{rock}")
        print(f"Computer choose Paper:\n{paper}")
        print("Computer Wins!")
        count_computer += 1
    elif player == 0 and computer == 2:
        print(f"Player choose Rock:\n{rock}")
        print(f"Computer choose Scissors:\n{scissors}")
        print("Player Wins!")
        count_player += 1

    elif player == 1 and computer == 0:
        print(f"Player choose Paper:\n{paper}")
        print(f"Computer choose Rock:\n{rock}")
        print("Player Wins!")
        count_player += 1
    elif player == 1 and computer == 1:
        print(f"Player choose Paper:\n{paper}")
        print(f"Computer choose Paper:\n{paper}")
        print("It's a draw!")

    elif player == 1 and computer == 2:
        print(f"Player choose Rock:\n{paper}")
        print(f"Computer choose Scissors:\n{scissors}")
        print("Computer Wins!")
        count_computer += 1

    elif player == 2 and computer == 0:
        print(f"Player choose Scissors:\n{scissors}")
        print(f"Computer choose Rock:\n{rock}")
        print("Computer wins!")
        count_computer += 1
    elif player == 2 and computer == 1:
        print(f"Player choose Scissors:\n{scissors}")
        print(f"Computer choose Paper:\n{paper}")
        print("Player wins!")
        count_player += 1
    elif player == 2 and computer == 2:
        print(f"Player choose Scissors:\n{scissors}")
        print(f"Computer choose Scissors:\n{scissors}")
        print("It's a draw!")
    else:
        break


print(f'Player score : {count_player}')
print(f'Computer score: {count_computer}')
