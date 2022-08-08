import random

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

lizard = '''
              ____...---...___
___.....---"""        .       ""--..____
     .                  .            .
 .             _.--._       /|
        .    .'()..()`.    / /
            ( `-.__.-' )  ( (    .
   .         \        /    \ \
       .      \      /      ) )        .
            .' -.__.- `.-.-'_.'
 .        .'  /-____-\  `.-'       .
          \  /-.____.-\  /-.
           \ \`-.__.-'/ /\|\|           .
          .'  `.    .'  `.
          |/\/\|    |/\/\|
'''

spock = '''
                      _    
                     | |   
 ___ _ __   ___   ___| | __
/ __| '_ \ / _ \ / __| |/ /
\__ \ |_) | (_) | (__|   < 
|___/ .__/ \___/ \___|_|\_\
    | |                    
    |_|                    
'''


print(lizard)
options = [rock, paper, scissors, lizard, spock]
print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
player = input("Type 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, and 4 for Spock. Good Luck!\n")
player1 = int(player)
if player1 >= 5 or player1 < 0:
  print("You typed an invalid number you loose!")
else:  
  player1_choice = options[player1]
  print("You chose:")
  print(player1_choice)

  print("I the mighty computer choose:")
  player2 = (random.choice(options))
  print(player2) 

  if player1_choice == scissors and player2 == paper:
    print("You win! Scissors cuts Paper.")
  if player1_choice == paper and player2 == rock:
    print("You win! Paper covers Rock.")  
  if player1_choice == rock and player2 == lizard:
    print("You win! Rock crushes Lizard.")
  if player1_choice == lizard and player2 == spock:
    print("You win! Lizard poisons Spock.")
  if player1_choice == spock and player2 == scissors:
    print("You win! Spock smashes Scissors.")
  if player1_choice == scissors and player2 == lizard:
    print("You win! Scissors decapitates Lizard.")
  if player1_choice ==lizard and player2 == paper:
    print("You win! Lizard eats paper.")  
  if player1_choice == paper and player2 == spock:
    print("You win! Paper disproves Spock.")
  if player1_choice == spock and player2 == rock:
    print("You win! Spock vaporizes Rock.")
  if player1_choice == rock and player2 == scissors:
    print("You win! Rock crushes Scissors.")
                

  if player2 == scissors and player1_choice == paper:
    print("I the mighty computer wins! Scissors cuts Paper.")
  if player2 == paper and player1_choice == rock:
    print("I the mighty computer wins!! Paper covers Rock.")  
  if player2 == rock and player1_choice == lizard:
    print("I the mighty computer wins! Rock crushes Lizard.")
  if player2 == lizard and player1_choice == spock:
    print("I the mighty computer wins! Lizard poisons Spock.")
  if player2 == spock and player1_choice == scissors:
    print("I the mighty computer wins! Spock smashes Scissors.")
  if player2 == scissors and player1_choice == lizard:
    print("I the mighty computer wins! Scissors decapitates Lizard.")
  if player2 == lizard and player1_choice == paper:
    print("I the mighty computer wins! Lizard eats paper.")  
  if player2 == paper and player1_choice == spock:
    print("I the mighty computer wins! Paper disproves Spock.")
  if player2 == spock and player1_choice == rock:
    print("I the mighty computer wins! Spock vaporizes Rock.")
  if player2 == rock and player1_choice == scissors:
    print("I the mighty computer wins! Rock crushes Scissors.")
                    
  if player2 == player1_choice:
    print("You tied with me. Let's go again!")
