# this is the welcome and rules component V1
new_player_difficulty = 0
played_before = "/"
rules = 0
show_rules = ""
rules_text = "The rules are quite simple\nThis will be a multiple choice quiz. \nEnter either A, B, C or D to answer each question, and no cheating!"
# this component welcomes users
print("*** Welcome to the te reo maori quiz! ***\n"
      "We hope you have a fantastic time and good luck.\n")
# this component asks if the user has played before
while played_before == "/":
    played_before = input("Have you played this quiz before?: ")
    if played_before.lower() == "yes":
        # this changes the difficulty based on whether the player has played before
        new_player_difficulty = 1
        # this changes whether the rules are automatic
        rules = 1
        print("You're already a master then. Right, let's crack on")
    elif played_before.lower() == "no":
        print("Well, good luck!")
    else:
        print("Please pick yes or no")
        played_before = "/"
# this asks the user if they need the rules
print("************************************\nNow for the rules\n")
if rules == 1:
    show_rules = input("do you need a refresher on the rules?: ")
    if show_rules.lower() == "yes":
        print("\n", rules_text)
    elif show_rules.lower() == "no":
        print("\nAwesome, let's go!")
