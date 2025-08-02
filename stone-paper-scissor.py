#rock-paper scissors game

import random

def get_choice():
  player_choice=input("enter a choice(rock,paper,scissors):")
  options=["rock","paper","scissors"]
  computer_choice = random.choice(options)
  choice={"player":player_choice,"computer":computer_choice}
  return choice

def check_win(player,computer):
  print(f"you chose {player} , computer chose {computer}")
  if player==computer:
    return "its a tie!"
  elif player=="rock":
    if computer=="scissor":
      return "rock smashes scissors!you win!!!"
    else:
      return "paper cover rocks!you loose"
  elif player=="paper":
   if computer=="rock":
      return "paper cover rock!you win!!!"
   else:
     return "scissors cuts paper!you loose"
  elif player=="scissor":
   if computer=="paper":
     return "scissors cut paper!you win!!!"
  else :
     return "rock smashes scissors!you loose"

choice= get_choice()
result=check_win(choices["player"],choices["computer"])
print(result)
