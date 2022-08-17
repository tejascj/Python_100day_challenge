#rock, papers and scissors game
# https://replit.com/@tejascj/rock-paper-scissors-start#README.md <--README.md

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

#Write your code below this line 👇
import random
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print("You chose\n")
# print user choice
if user_choice==0:
    print(rock)
elif user_choice==1:
    print(paper)
elif user_choice==2:
    print(scissors)
else:
    print("Enter valid input")
    exit()

# add rock,paper,scissors to a list
lst=[0,1,2]
lst2=[rock,paper,scissors]
# using random.choice select computer choice
comp_choice=random.choice(lst)
print("Computer chose\n")
print(lst2[comp_choice])

# Decide who wins
if user_choice>2 or user_choice<0 :
    print("You typed invalid choice. You Loss!")
elif user_choice==comp_choice:
    print("Draw!")
elif user_choice==0 and comp_choice==2:
    print("you win!")
elif comp_choice>user_choice:
    print("You Loss!")
elif user_choice==1 and comp_choice==0:
    print("You Win!")
elif user_choice==2 and comp_choice==1:
    print("YOu win!")
elif user_choice==2 and comp_choice==0:
    print("You Loss!")