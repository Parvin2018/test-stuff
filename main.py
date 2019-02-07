# Sang Kaghaz Gheichi! Game ;)


# Initial step for this progarm is to transform my Strings to numeric codes !
# 0 = Rock
# 1 = Spock
# 2 = Paper
# 3 = Lizard
# 4 = Scissors

# Converting names to numbers
import random
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Hey! Wana paly? Pick something!"
        return

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Error: choose another number!"
        return



def uplay():
    player_choice = raw_input("Enter (rock, spock, paper, lizard, scissors): ")
    # print out the message for the player's choice
    print "Player chooses %s" % player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses %s" % comp_choice
    # compute difference of comp_number and player_number
    diff = player_number - comp_number
    if diff == 0:
        print "You and I tie!"
    elif diff == 4 or diff == 3 or diff == -1 or diff == -2:
        print "I win!"
    else:
        print "You win!"

# testing the code
uplay()



