import random


def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


def string_checker(question):
    error = "\nSorry, you must enter a string\n"
    word = ""
    while not word:
        try:
            word = input(question)
            return word
        except ValueError:
            print(error)


def random_question_welcome():
    welcome = ["now for question", "now, onto question",
               "1,2,3,4... umm... time for question", "next question! question"]
    welcome_message = random.choice(welcome)
    return welcome_message


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


def checkIfDuplicates_1(listOfElems):
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True


red_herrings = ["pūmau", "whakarite", "mema", "mate", "werawera", "ngawari", "pahua", "paunatia", "pounamu", "pupuhi",
                "whitinga ra", "kia", "purini", "hararei", "muramura", "moemoeā", "hoko atu", "kawe waka"]
example_list_one = ["one", "two", "three"]
example_list_two = [1, 2, 3]
example_list_1 = [example_list_one, example_list_two]
example_list_three = ["tahi", "rua", "toru", "wha", "rima", "ono"]
example_list_four = ["one", "two", "three", "four", "five", "six"]
example_list_2 = [example_list_three, example_list_four]
example_list = [example_list_1, example_list_2]
asked_question = ""
questions_asked = 1
topic_selector = 1
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

while question <= 5:
    asked_question = ""
    print(random_question_welcome(), questions_asked)
    while asked_question == "":
        question_selected = random.choice(example_list[topic_selector][1])
        number_in_list = example_list[topic_selector][1].index(question_selected)
        if question_selected not in used_list:
            used_list.append(question_selected)
            asked_question = question_selected

    print(question_selected, "translates to:")
    right_answer = random.randint(0, 3)
    wrong_answer_one = random.choice(red_herrings)
    wrong_answer_two = random.choice(red_herrings)
    wrong_answer_three = random.choice(red_herrings)
    multi_choice.append(wrong_answer_one)
    multi_choice.append(wrong_answer_two)
    multi_choice.append(wrong_answer_three)
    multi_choice.insert(right_answer, example_list[topic_selector][0][number_in_list])
    contains_duplicates = checkIfDuplicates_1(multi_choice)
    while contains_duplicates == True:
        dup_int = duplicate_finder(multi_choice)
        double_no = dup_int[0]
        multi_choice[double_no] = random.choice(red_herrings)
        contains_duplicates = checkIfDuplicates_1(multi_choice)


    print("A.", multi_choice[0])
    print("B.", multi_choice[1])
    print("C.", multi_choice[2])
    print("D.", multi_choice[3])

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
    if answer_int == right_answer:
        answer_right_int += 1
    elif answer_int != right_answer:
        answer_wrong_int += 1
    answer = ""

    del multi_choice[0:4]
    print("\nright:", answer_right_int, "wrong:", answer_wrong_int, "\n********************")
    questions_asked += 1
    question += 1

percentage_right = answer_right_int / question * 100
print("\n****************************\nfinal score\nright:", answer_right_int, "\nwrong:", answer_wrong_int, "\nattempted:", question, "\npercentage correct %", percentage_right)
