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
moves=[rock,paper,scissors]

user_choice=int(input("Welcome to RPS, choose 0 Rock ,1 Paper, 2 Scissors \n"))
computer_choice=random.randint(0,2)

print("You chose",user_choice,":" ,moves[user_choice])
print("Computer chose ",computer_choice,":")
print(moves[computer_choice])

if user_choice == computer_choice:
  print("It's a Draw!")

if user_choice ==0 and computer_choice ==1:
  print("Computer wins")

if user_choice ==0 and computer_choice==2:
  print("You win!")

if user_choice ==1 and computer_choice ==0:
  print("You win!")

if user_choice ==1 and computer_choice ==2:
  print("Computer wins!")

if user_choice==2 and computer_choice==1:
  print("You win!")
elif user_choice >2:
  print("Wrong choice, you lose")





