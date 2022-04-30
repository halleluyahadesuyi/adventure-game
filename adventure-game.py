import time
import random

# List all enemies in the game
enemy_list = ['orc', 'witch', 'dragon', 'monster']
# Initialize enemy with an empty string
enemy = ''
# Initialize user's weapon as axe
weapon = 'axe'


# Pause input 'message' for 2 seconds before displaying it
def print_pause(message):
    print(message)
    time.sleep(2)


# End the adventure game
def end_game():
    print("It was such an adventure! See you next time.")


# Make the choice to replay game or not
def replay_game():
    choice = get_input("Would you like to replay this game? (y/n)\n",
                       ['y', 'n'])
    if choice == 'y':
        global weapon
        print_pause("Awesome! Restarting the game...")
        weapon = 'axe'
        play_adventure_game()
    else:
        end_game()


# User chooses to move towards the house
def move_towards_house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a "
                + enemy + ".")
    print_pause("Yikes! This is the " + enemy + "'s house!")
    print_pause("The " + enemy + " attacks you!")
    fight_or_run()


# Move to the house or switch weapon
def make_decision():
    choice = get_input("Please enter 1 or 2.\n", ['1', '2'])
    if choice == '1':
        move_towards_house()
    else:
        switch_weapon()


# Choose the decision to take
def decide():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    make_decision()


# User changes weapon
def switch_weapon():
    global weapon
    print_pause("You peer cautiously into the cave.")
    if weapon == 'sword':
        print_pause("You've been here before, and gotten all the" +
                    " good stuff. It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You discard your silly old " + weapon +
                    " and take the sword with you.")
        weapon = 'sword'
    print_pause("You walk back out to the field.")
    decide()


# Display information about the game
def play_adventure_game():
    global enemy
    enemy = random.choice(enemy_list)
    print_pause("You find yourself standing in an open field, filled" +
                " with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + enemy + " is somewhere around" +
                " here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)"
                + " " + weapon + ".")
    decide()


# Fight the enemy heads on
def fight():
    if weapon == 'sword':
        print_pause("As the " + enemy + " moves to attack, you unsheath" +
                    " your new " + weapon + ".")
        print_pause("The " + weapon + " of Mordith shines brightly in your" +
                    " hand as you brace yourself for the attack.")
        print_pause("But the " + enemy + " takes one look at your shiny" +
                    " new toy and runs away!")
        print_pause("You have rid the town of the " + enemy +
                    ". You are victorious!")
    else:
        print_pause("You do your best...")
        print_pause("But your " + weapon + " is no match for the "
                    + enemy + ".")
        print_pause("You have been defeated!")
    replay_game()


# User runs from the enemy
def run():
    print_pause("You run back into the field. Luckily, you don't seem to" +
                " have been followed.")
    decide()


# User chooses to fight or run away
def fight_or_run():
    choice = get_input("Do you want to (1) fight or (2) run for your life?\n",
                       ['1', '2'])
    if choice == '1':
        fight()
    else:
        run()


# The choice of user
def get_input(prompt, values):
    while True:
        choice = input(prompt).lower()
        if choice in values:
            return choice


# Start the adventure game
play_adventure_game()
