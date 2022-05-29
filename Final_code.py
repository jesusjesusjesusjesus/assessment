import random

# checks if input is an int, if not returns an error
def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)

# checks if input is an str, if not returns an error
def string_checker(question):
    error = "\nSorry, you must enter a string\n"
    word = ""
    while not word:
        try:
            word = input(question)
            return word
        except ValueError:
            print(error)

#selects a random lead-in and returns it to the main code
def random_question_welcome():
    welcome = ["now for question", "now, onto question",
               "1,2,3,4... umm... time for question", "next question! question"]
    welcome_message = random.choice(welcome)
    return welcome_message

# finds where the duplicate is in a given 4 no list
def duplicate_finder(list):
    if list[0] == list[1]:
        return [0, 1]
    elif list[0] == list[2]:
        return [0, 2]
    elif list[0] == list[3]:
        return [0, 3]
    elif list[1] == list[2]:
        return [1, 2]
    elif list[1] == list[3]:
        return [1, 3]
    elif list[2] == list[3]:
        return [2, 3]
    else:
        return list

# checks if there is a duplicate in a given list
def checkIfDuplicates_1(listOfElems):
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True


# this is the play again loop and var
play_again = ""

while play_again == "":
    new_player_difficulty = 0
    played_before = "/"
    rules = 0
    show_rules = ""
    rules_text = "The rules are quite simple\n This will be a multiple choice quiz. \n Enter either A, B, C or D to answer each question, and no cheating!"
    age_difficulty = 0
    skill_level = 0
    skill_level_multiplier = 0
    total_difficulty = 0
    max_difficulty = 7
    difficulty = 0
    difficulty_percentage = 0
    question_difficulty = 0
    topic_selector = 6
    topic_choice = ""
    # topics database
    topics = ["days of the week", "numbers", "colours", "word translations", "actions", "months"]
    days_of_the_week_maori = ["rahina", "ratu", "raapa", "rapare", "ramere", "rahoroi", "ratapu"]
    days_of_the_week_english = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    numbers_maori = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau", "rua tekau", "rima tekau",
                     "kotahi rau"]
    numbers_english = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "twenty",
                       "fifty", "one hundred"]
    months_maori = ["Kohi-tātea", "Hui-tanguru", "Poutū-te-rangi", "Paenga-whāwhā", "Haratua", "Pipiri", "Hōngongoi",
                    "Here-turi-kōkā", "Mahuru", "Whiringa-ā-nuku", "Whiringa-ā-rangi", "Hakihea"]
    months_english = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
                      "november", "december"]
    word_translations_maori = ["aroha", "awa", "haka", "iwi", "kai", "karakia", "marae", "maunga", "moana", "tamariki", "tapu"]
    word_translations_english = ["love", "river", "dance", "river", "food", "prayer", "meeting house", "mountain", "ocean", "children", "sacred"]
    colours_maori = ["ma", "whero", "kowhai", "kakariki", "pango", "mawhero", "kahurangi", "kiwikiwi", "karaka", "tawa"]
    colours_english = ["white", "red", "yellow", "green", "black", "pink", "blue", "grey", "orange", "purple"]
    actions_maori = ["oma", "peke", "kikoi", "e tu", "e noho", "pakipaki", "hurihuri", "korero", "whakarongo", "tangi"]
    actions_english = ["run", "jump", "walking", "stand up", "sit down", "clap", "spin", "talk", "listen", "cry"]

    colours = [colours_maori, colours_english]
    months = [months_maori, months_english]
    days_of_the_week = [days_of_the_week_maori, days_of_the_week_english]
    numbers = [numbers_maori, numbers_english]
    word_translations = [word_translations_maori, word_translations_english]
    actions = [actions_maori, actions_english]

    all_topics = [days_of_the_week, numbers, colours, word_translations, actions, months]
    # wrong answers
    red_herrings = ["pūmau", "whakarite", "mema", "mate", "werawera", "ngawari", "pahua", "paunatia", "pounamu", "pupuhi",
                    "whitinga ra", "kia", "purini", "hararei", "muramura", "moemoeā", "hoko atu", "kawe waka"]
    #other vars
    asked_question = ""
    questions_asked = 1
    question = 0
    question_selected = ""
    used_list = []
    multi_choice = []
    double_no = 0
    wrong_answer_one = ""
    wrong_answer_two = ""
    wrong_answer_three = ""
    number_in_list = 0
    contains_duplicates = True
    answer = ""
    correct_answer = ""
    answer_right_int = 0
    answer_wrong_int = 0
    answer_int = 0

    # this component welcomes users
    print("*** Welcome to the te reo maori quiz! ***\n"
          "We hope you have a fantastic time and good luck.\n")
    # this component asks if the user has played before
    while played_before == "/":
        played_before = input("Have you played this quiz before?(yes/no): ")
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
        if show_rules.lower() == "no":
            print("\nAwesome, let's go!")

    else:
        print(rules_text)
    # asks for name and then says hello
    name = input("What is your name?: ")
    print("Hello", name)
    # asks for age and changes difficulty accordingly
    while age_difficulty == 0:
        age = integer_checker("\nWhat is your age?: ")
        if age <= 10:
            age_difficulty = 1
        elif 20 >= age > 10:
            age_difficulty = 2
        elif age > 20:
            age_difficulty = 3
        else:
            print("please pick a real age")
    # asks for skill level and changes difficulty accordingly
    while skill_level_multiplier == 0:
        skill_level = integer_checker("\nOn a scale from 1-10, what would you say your skill level is?: ")
        if 11 > skill_level > 0:
            if skill_level <= 3:
                # easiest skill level (easy)
                skill_level_multiplier = 1
            elif skill_level <= 5:
                # 2nd easiest skill level (medium)
                skill_level_multiplier = 2
            elif skill_level <= 8:
                # 2nd hardest skill level (hard)
                skill_level_multiplier = 3
            elif skill_level <= 10:
                # hardest skill level (insane)
                skill_level_multiplier = 4
    # calculates total difficulty
    total_difficulty = skill_level_multiplier + age_difficulty
# determines question difficulty based on difficulty
    if total_difficulty <= 2:
        question_difficulty = 1
    elif 2 < total_difficulty <= 3:
        question_difficulty = 2
    elif 3 < total_difficulty <= 5:
        question_difficulty = 3
    elif 5 < total_difficulty <= 7:
        question_difficulty = 4
    else:
        print("error")
# show avaliable topics based on question difficulty
    if question_difficulty == 1:
        print("These are your available topics", topics[0:2])
    elif question_difficulty == 2:
        print("These are your available topics", topics[0:4])
    elif question_difficulty == 3:
        print("These are your available topics", topics[0:5])
    elif question_difficulty == 4:
        print("These are your available topics", topics[0:])
# shows which topic you chose, and sets topic to that
    while topic_selector == 6:
        topic_choice = input("pick a topic: ")
        if topic_choice.lower() == "days of the week":
            print("you chose", topic_choice, "\ngreat choice")
            topic_selector = 0
        elif topic_choice.lower() == "numbers":
            print("you chose", topic_choice, "\ngreat choice")
            topic_selector = 1
        elif topic_choice.lower() == "colours":
            print("you chose", topic_choice, "\ngreat choice")
            topic_selector = 2
        elif topic_choice.lower() == "word translations":
            print("you chose", topic_choice, "\ngreat choice")
            topic_selector = 3
        elif topic_choice.lower() == "actions":
            print("you chose", topic_choice, "\ngreat choice")
            topic_selector = 4
        elif topic_choice.lower() == "months":
            print("you chose", topic_choice, "\ngreat choice")
            topic_selector = 5
        else:
            print("seems you either did not enter a valid answer or you spelt it incorrectly\nlets try again")
            topic_selector = 6
# it will determine a random word from the right list and also grab the corresponding translation
    while question <= 5:
        asked_question = ""
        print(random_question_welcome(), questions_asked)
        while asked_question == "":
            question_selected = random.choice(all_topics[topic_selector][1])
            number_in_list = all_topics[topic_selector][1].index(question_selected)
            # puts chosen word in a used list so it cannot be used again
            if question_selected not in used_list:
                used_list.append(question_selected)
                asked_question = question_selected
# prints the question and determines in what order the answers go and checks for duplicates
        print(question_selected, "translates to:")
        right_answer = random.randint(0, 3)
        wrong_answer_one = random.choice(red_herrings)
        wrong_answer_two = random.choice(red_herrings)
        wrong_answer_three = random.choice(red_herrings)
        multi_choice.append(wrong_answer_one)
        multi_choice.append(wrong_answer_two)
        multi_choice.append(wrong_answer_three)
        multi_choice.insert(right_answer, all_topics[topic_selector][0][number_in_list])
        contains_duplicates = checkIfDuplicates_1(multi_choice)
        # if contains duplicates it changes the first word of the two doubled up
        while contains_duplicates:
            dup_int = duplicate_finder(multi_choice)
            double_no = dup_int[0]
            multi_choice[double_no] = random.choice(red_herrings)
            contains_duplicates = checkIfDuplicates_1(multi_choice)
        # prints answers
        print("A.", multi_choice[0])
        print("B.", multi_choice[1])
        print("C.", multi_choice[2])
        print("D.", multi_choice[3])
        # askes for the correct answer and sets a var accordingly
        while answer == "":
            answer = input("\npick the correct answer (A B C or D)\n: ")
            if answer.upper() == "A":
                answer_int = 0
            elif answer.upper() == "B":
                answer_int = 1
            elif answer.upper() == "C":
                answer_int = 2
            elif answer.upper() == "D":
                answer_int = 3
            else:
                print("you answered", answer.upper(), "this is not a valid answer")
                answer = ""
        # adds to either the correct score or the wrong score depending on answer
        if answer_int == right_answer:
            answer_right_int += 1
        elif answer_int != right_answer:
            answer_wrong_int += 1
        answer = ""
        # clears the answer list and shows scores
        del multi_choice[0:4]
        print("\nright:", answer_right_int, "wrong:", answer_wrong_int, "\n********************")
        questions_asked += 1
        question += 1
    # at the end of the game after the six reps of the questions, displays correct, wrong, attempted and right percentage
    percentage_right = answer_right_int / question * 100
    print("\n****************************\nfinal score\nright:", answer_right_int, "\nwrong:", answer_wrong_int, "\nattempted:", question, "\npercentage correct %", percentage_right)
    # asks if they want to play again, and starts the game again if they say yes, and ends if they say no
    play_again = input("do you wish to play again?: ")
    if play_again.upper() == "YES" or "Y":
        play_again = ""
        print("Ok, let's go!")
    else:
        play_again = "no"
        print("Thanks for playing, see you next time!")
