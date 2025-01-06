print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

import random
choise_1 = input ("the 2 path ahead of you, you need to choose right or left: ").lower()
correct_choise = ["right", "left"]
correct_choise1 = ["orange","silver","gold"]
random = random.choice(correct_choise)
if choise_1 == random:
    choise_2 = input ("you arrive at the huge river, the water look calm, \ndo you wait "
                      "for the boat to arrive or you swim across? wait or swim?").lower()
    if choise_2 == "swim":
        choise_3 = input ("you swim your heart out and safely arrive at a magestic  mantion, these 3 "
                          "colour door, orange, gold, silver, which one you should choose?").lower()
        if choise_3 == "orange":
                print ("the hungry red dragon inside, you became his lunch..")
        if choise_3=="gold":
                print ("these no gold here, you find crazy princess with knife and cut off your head.")
        if choise_3 == "orange":
                print ("congratulation, you found the treasure chest with million of money "
                       "in it. you are rich and live happly ever after with the crazy princess")
    else:
        print ("the angry pack of wolf rushing toward you and eat "
               "you alive, your dead, game over")

else:
    print("you should  choose " + str(random))
    print ("your fell into a deep hole and die, game over")