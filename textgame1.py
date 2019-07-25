# Import Module built-in-Functions
import random
import time
import sys


# global variables
player_lives = 5
player_strength = 5
player_points = 3


# list -game items-
g_list = []


# It prints messages , with a short pause between each message.
# function taken from elevator.py
def prompt_pause(message):
    print()
    print(message)
    time.sleep(2)


# It clears the screen.str and operand.
def cls():
    print("\n" * 30)


# It prints the title of the text game.
def adventure_title():
    cls()
    print("Adventure in Amazonian's Jungle")
    print("=================================")


# It presents randomly game intro,using random.choice
def display_intro():
    adventure_title()
    intro_list = ["...Guerrillas", "... an Old Castle", " ...a killer wasp"]
    intro_item = random.choice(intro_list)
    prompt_pause("Your best buddy invited you to his "
                 "country-side home in South America.\n")
    prompt_pause("In the middle of the Amazonian jungle")
    prompt_pause("Sooner or later you could find... \n")
    print(intro_item)
    print()
    player_status()


# It validate all player answers.
# this code is re-use each time player inputs
def valid_response(prompt, options):
    while True:
        response = input(prompt).lower().strip()
        for option in options:
            if option == response:
                return option
        else:
            prompt_pause("Sorry that is not a valid input.")


# It prints the player status
def player_status():
    print("===================")
    print("You have: ", player_lives, "lives")
    print("Plus", player_strength, "strengths")
    print("and", player_points, "points")
    print("===================")


# It defines a "loot" type using strengths,points and lives "
def big_wasp(lives, strength):
    global player_strength
    global player_points
    global player_lives
    prompt_pause("Suddenly a salvage big-wasp appears!")
    print("====================")
    print("She has ", lives, "lives!")
    print("====================")
    while lives > 0:
        action = ["1", "2"]
        action = valid_response("What would you do? \n"
                                "Press 1 to Attack \n"
                                "Press 2 to Run away\n", action)
        if action == "1":
            lives = lives - player_strength
            if lives <= 0:
                print("===================")
                print("     You Won     !!")
                print("You earned 2 Points")
                print("===================")
                player_points += 2
                player_status()
            else:
                print("===================================")
                print("The big-wasp still has", lives, "lives")
                print("===================================")
                print()
                print("Killer Wasp attacks again!!!!")
                print()
                if player_points <= 0:
                    player_lives -= strength
                    if player_lives <= 0:
                        print("GAME OVER")
                        sys.exit()
                    game_in()
                else:
                    player_points -= strength
                    player_status()
        elif action == "2":
            print("You escaped")
            return


# It creates a randomly big_wasp , using module, random-variables
def a_random_big_wasp():
    wasp = random.randint(1, 5)
    if wasp % 2 == 0:
        lives = random.randint(1, 20)
        strength = random.randint(1, 4)
        big_wasp(lives, strength)


def the_bad_guy():
    global g_list
    badge = ["1", "2"]
    prompt_pause("A gangster kidnapped the village/'s teacher and \n"
                 "hide her in the 'Ravine of the Dead'.\n")
    badge = valid_response("Press 1 to  rescue  the teacher\n"
                           "Press 2 to  explore more\n", badge)
    if "1" in badge:
        g_list.append("Laptop")
        g_list.append("AKKA140")
        print("On your way to rescue the teacher,\n"
              "you found a ", g_list[-1], "and a brand\n"
              "new", g_list[-2], "that for sure belong to\n"
              "....the Guerrillas\n")
        if "Guerrilla's Laptop"  in g_list and "AKKA140"in g_list:
            print("You just find her, and better go to\n"
                  "your friend's HOME")
            finale()
        else:
            print()
            print("Not that bad, you are a HERO!!!\n")
            print("You got Guerrilla's laptop with\n"
                  "all secret operation records\n"
                  "and the latest riffle with eye detention\n"
                  "sensor.")
    elif "2" in badge:
        village_botica()


# it asks player to game.
def game_in():
    print()
    answer = ["yes", "no"]
    response = valid_response("Would you like to play? Press 'YES' "
                              "or press 'NO':\n ", answer)
    if "no" == response:
        prompt_pause("OK, Next time")
        sys.exit()
    elif "yes" == response:
        prompt_pause("Excellent, loading")
        player_status()


# Player's choice from home position.
def player_choice():
    cls()
    cardinal_pos()
    choice = ["1", "2", "3", "4"]
    prompt_pause("You find yourself standing in your friend's home\n")
    choice = valid_response("Press 1 to  go East  -Village-\n"
                            "Press 2 to  go West  -Guerrillas-\n"
                            "Press 3 to  go North -Old Castle-\n"
                            "Press 4 to  go South -Ravine-\n", choice)
    if "1" in choice:
        village()
    elif "2" in choice:
        guerrillas()
    elif "3" in choice:
        old_castle()
    elif "4" in choice:
        ravine()


# Room functions
def village():
    cls()
    villa = ["1", "2"]
    prompt_pause("There are some many thing going on in the Village\n")
    prompt_pause("You could not have more luck, a big wasp was just "
                 "passing.")
    a_random_big_wasp()
    player_status()
    prompt_pause("Keep going,from here You can go to the North -Old-Castle-\n"
                 "or go to the South -Ravine-\n")
    villa = valid_response("Press 1 to go North\n"
                           "Press 2 to go South\n", villa)
    if "1" in villa:
        old_castle()
    elif "2" in villa:
        ravine()


def village_botica():
    global player_strength
    global player_points
    villa2 = ["1", "2"]
    prompt_pause("There is big sign saying that\n"
                 "they got a antidote formula\n"
                 "to kill anything that hits or bites\n")
    prompt_pause("What would you do? \n")

    villa2 = valid_response("Press 1 to get the antidote\n"
                            "Press 2 to think about it\n", villa2)

    if "1" in villa2:
        player_strength += 5
        prompt_pause("The Gangster Chief was there ,but\n"
                     "You grasped the bottle first...\n")
        player_status()
        finale()
    elif "2" in villa2:
        prompt_pause("You didn't drink it!!!\n"
                     "You are not that adventured,aren't you?\n")
        prompt_pause("The good thing is your friend found you \n"
                     "and took you back home,\n"
                     "....'Jungle is not a joke' ")
        player_points -= 2
        player_status()
        player_choice()


def old_castle():
    cast1 = ["1", "2"]
    print("You are at the Old-Castle\n")
    print("Your friend previously warned you "
          "about some killer wasps "
          "you thought He was joking")
    a_random_big_wasp()
    player_status()
    prompt_pause("Now,You can go to the South -HOME-\n "
                 "or to the East  -Village-\n")
    cast1 = valid_response("Press 1 to go South or\n"
                           "Press 2 to go East\n", cast1)
    if "1" == cast1:
        player_choice()
    elif "2" == cast1:
        village()


def guerrillas():
    global player_points
    camp1 = ["1", "2"]
    cls()
    prompt_pause("You find yourself at the Guerrilla Camp\n")
    a_random_big_wasp()
    prompt_pause("The Guerrillas in their camp ran out of food but they\n"
                 "had plenty of weapons and high end equipments\n")
    if player_points <= 0:
        print()
        print("You better go home")
        player_points += 2
        player_status()
        player_choice()
    else:
        player_points += 4
        prompt_pause("This is a dangerous territory\n")
        prompt_pause("Inside their tent you heard them talking about\n"
                     "weapon shipments from a corrupted foreign country\n")
        player_status()
        print()
        camp1 = valid_response("Press 1 to go East -HOME- or \n"
                               "Press 2 to North -Castle-\n", camp1)
        if "1" in camp1:
            player_choice()
        elif "2" in camp1:
            old_castle()


def ravine():
    ine = ["1", "2"]
    prompt_pause("You don't believe your eyes! "
                 "What this place is like...\n")
    the_bad_guy()
    ine = valid_response("You haven't find the teacher,yet!\n"
                         "For now your options are:\n"
                         "Press 1 to go North -back to the village- or \n"
                         "Press 2 to go West -Guerrilla Camp\n", ine)
    if "1" in ine:
        village()
    elif "2" in ine:
        guerrillas()
    player_choice()


# End of this adventure,
# until I'll learn more of python programing language.
def finale():
    global g_list
    questfin = ["1", "2"]
    g_list.append("briefcase full of Money")
    name = input("Adventurer , forgot to ask you..."
                 "name ? >>>\n").capitalize().strip()
    prompt_pause("Finally,You found the Teacher and she is so beautiful")
    print("Just one more thing,", name, "\nthe gangster chief\n"
          "is now fighting against the Wasps,\n"
          "soon He would ran out of lives\n")
    print("He went to 'The Old Castle'to \n"
          "hide the ", g_list[-1], ".\n")
    questfin = valid_response("What would you do?\n"
                              "Press 1 to quiet and wait for 'Part2' or\n"
                              "Press 2 to play again", questfin)
    if "1" in questfin:
        prompt_pause("In this particular case, 'Part 2'\n"
                     "will be the best one\n"
                     "goodbye\n ")
        sys.exit()
    else:
        game_in()


# function to help the player map visualization
def cardinal_pos():
    print()
    print("                      .   N    .  ")
    print("                        . !  .    ")
    print("                         .:.      ")
    print("                  W- - -  O - - -E")
    print("                         .:.      ")
    print("                       .  !  .    ")
    print("                     .    S    .  ")
    print()


# refactoring game function
def game1():
    display_intro()
    game_in()
    player_choice()


game1()
