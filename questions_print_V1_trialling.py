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


red_herrings = ["pūmau", "whakarite", "mema", "mate", "werawera", "ngawari", "pahua", "paunatia", "pounamu", "pupuhi", "whitinga ra", "kia", "purini", "hararei", "muramura", "moemoeā", "hoko atu", "kawe waka"]
example_list_one = ["one", "two", "three"]
example_list_two = [1, 2, 3]
example_list_1 = [example_list_one, example_list_two]
example_list_three = ["four", "five", "six"]
example_list_four = [4, 5, 6]
example_list_2 = [example_list_three, example_list_four]
example_list = [example_list_1, example_list_2]
asked_question = ""
questions_asked = 1
topic_selector = 1
question = 0
question_selected = ""
used_list = [""]
multi_choice = [""]

while question <= 3:
    print(random_question_welcome(), questions_asked)
    while asked_question == "":
        question_selected = random.choice(example_list[topic_selector][0])
        number_in_list = question_selected.index(question_selected)
        if example_list[topic_selector][0] in used_list:
            asked_question = ""
        else:
            used_list.append(question_selected)
            asked_question = question_selected

    print(question_selected, "translates to")
    right_answer = random.randint(1, 4)
    wrong_answer_one = random.choice()
    wrong_answer_two = random.randint(1, 4)
    wrong_answer_three = random.randint(1, 4)

    print(used_list)
    questions_asked += 1
    question += 1
