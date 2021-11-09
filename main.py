gamestate =  1
game_on = True
import time
playerhealth = 3
inventory = []

while game_on:
    while gamestate == 1:
        time.sleep(3)
        question_a = input('You awaken and find yourself in the cockpit of a Spcaecraft \n What do you do? '
                         '\n mess around the cockpit \n look around : ')

        print(question_a)

        if question_a == "mess around the cockpit":
                print('you mess around with the controls of the cockpit,\n nothing happens\n it appears that it is switched off')

        elif question_a == "look around":
            print('You get up and look around you notice a shinny object \n you find a keycard: ' )
            inventory.append('keycard')
            time.sleep(3)
            print("keycard has been added to inventory")
            gamestate = 2
    while gamestate == 2:
        userinput = input("You notice a big doorway, one the right there is a console, \n It looks like the card goes there ")







