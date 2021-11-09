game_on = True
while game_on:
    inventory = []
    playerhealth = 3

    def shipsequence():
        question_a = input('You awaken and find yourself in the cockpit of a Spcaecraft \n What do you do? '
                     '\n mess around the cockpit \n look around : ')
        print(question_a)

        if question_a == "mess around the cockpit":
            print('you mess around with the controls of the cockpit,\n nothing happens\n it appears that it is switched off')

        if question_a == "look around":
            print('You get up and look around you notice a shinny object \n you find a keycard: ' )
            inventory.append('keycard')
            print(inventory)
            

    question_b = input(' you notice a large door, \n Theres console on the side, it looks like you can insert something in ')




