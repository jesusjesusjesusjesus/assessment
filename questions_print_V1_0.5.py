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
questions_asked = 1
question = 0
question_selected = ""
used_list = []


while question <= 3:
    asked_question = ""
    print(random_question_welcome(), questions_asked)
    while asked_question == "":
        question_selected = random.choice(red_herrings)
        number_in_list = question_selected.index(question_selected)
        if not question_selected in used_list:
            used_list.append(question_selected)
            asked_question = question_selected

    print(question_selected, "translates to")
    right_answer = random.randint(1, 4)
    print(right_answer)
    wrong_answer_one = random.randint(1, 4)
    wrong_answer_two = random.randint(1, 4)
    wrong_answer_three = random.randint(1, 4)

    print(used_list)
    questions_asked += 1
    question += 1
