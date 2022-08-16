# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
# random module ref

# https://replit.com/@tejascj/day-4-2-exercise#README.md  <- README.MD

# who gets to pay
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆



#Write your code below this line 👇
import random
from secrets import choice
person=random.randint(0,len(names)-1)
print(f"{names[person]} is going to buy the meal today!")

#input:- Give me everybody's names, separated by a comma. tejas, venu, skanda, sumanth
#output:- tejas is going to buy the meal today

#easy method using random.choice 
randper=random.choice(names)
print(f"{randper} is going to buy the meal today!")