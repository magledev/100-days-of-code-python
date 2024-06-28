print(
    '''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''
)

print("Welcome to The Treasure Hunt Game")
print("Explore and find the hidden treasure")

move1 = input(
    "You come to a cross road, you now have a decision to make. Go left or right? "
).lower()
if move1 == "left":
    print("You proceed on the path to the left and continue your adventure.")
else:
    print(
        "You take the path on the right and encounter a hungry bear, which mauls you to death.\nGAME OVER!"
    )

move2 = input(
    "You come to a clearing, which opens on to a large lake.\nDo you swim to the other shore or wait for a distant boat heading your way? "
).lower()
if move2 == "wait":
    print(
        "You decide to wait for the boat to reach shore and in the meantime take shelter."
    )
else:
    print(
        "You make your way in to the water and attempt to swim to the other side of the lake.\nUnfortunately you become tangled in long weeds and drown\nGAME OVER!"
    )

move3 = input(
    "You board the board the boat and after a short ride, reach the other side of the lake.\nWhen you dismount the boat you see a large hut, not far away and decide to investigate.\nThe hut has 3 doors: red, blue and yellow. Which one do you open? "
).lower()
if move3 == "yellow":
    print(
        "You have open the door and proceed inside. The room is filled with hordes of treasure.\nYOU WIN!"
    )
elif move3 == "blue":
    print(
        "You open the blue door and proceed inside. Halway in to the room you step on a trapdoor and fall to your death.\nGAME OVER!"
    )
else:
    print(
        "You open the red door and immediately set off booby trap which impails you and you die.\nGAME OVER!"
    )
