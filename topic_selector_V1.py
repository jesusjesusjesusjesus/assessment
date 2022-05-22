difficulty = 7
question_difficulty = 0
topic_selector = 0
topic_choice = ""
topics = ["days of the week", "numbers", "months", "word translations", "common phrase translation", "simple sentence translations"]

if difficulty <= 2:
    question_difficulty = 1
elif 2 < difficulty <= 3:
    question_difficulty = 2
elif 3 < difficulty <= 5:
    question_difficulty = 3
elif 5 < difficulty <= 7:
    question_difficulty = 4
else:
    print("error")

if question_difficulty == 1:
    print("These are your available topics", topics[0:2])
elif question_difficulty == 2:
    print("These are your available topics", topics[0:4])
elif question_difficulty == 3:
    print("These are your available topics", topics[0:5])
elif question_difficulty == 4:
    print("These are your available topics", topics[0:])

while topic_selector == 0:
    topic_choice = input("pick a topic: ")
    if topic_choice.lower() == "days of the week":
        print("you chose", topic_choice, "\ngreat choice")
        topic_selector = 1
    elif topic_choice.lower() == "numbers":
        print("you chose", topic_choice, "\ngreat choice")
        topic_selector = 2
    elif topic_choice.lower() == "months":
        print("you chose", topic_choice, "\ngreat choice")
        topic_selector = 3
    elif topic_choice.lower() == "word translations":
        print("you chose", topic_choice, "\ngreat choice")
        topic_selector = 4
    elif topic_choice.lower() == "common phrase translation":
        print("you chose", topic_choice, "\ngreat choice")
        topic_selector = 5
    elif topic_choice.lower() == "simple sentence translations":
        print("you chose", topic_choice, "\ngreat choice")
        topic_selector = 6
    else:
        print("seems you either did not enter a valid answer or you spelt it incorrectly\nlets try again")
        topic_selector = 0
