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

option =[rock,paper,scissors]
computer_choise=random.choice(option)
user_choise=input("please choose; rock, paper, scissors \n").lower()
print(f"the computer have pick \n {computer_choise}")
if user_choise == rock:
    user_choise = rock
elif user_choise == paper:
    user_choise=paper
else:
    user_choise=scissors

print (f"user have choose {user_choise}\n ")

print ("The result of the match are \n")
if user_choise == computer_choise:
    print("its a tie!")
elif user_choise == rock:
    computer_choise==scissors
    print("you won")
elif user_choise ==paper:
    computer_choise=rock
    print("you won")
elif user_choise ==scissors:
    computer_choise=paper
    print("you won")
else:
    print("computer wins")
