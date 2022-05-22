def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


age_difficulty = 0
skill_level = 0
skill_level_multiplier = 0
total_difficulty = 0
max_difficulty = 7
difficulty = 0
difficulty_percentage = 0

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
# calculates total difficulty (when fully integrated add played_before)
total_difficulty = skill_level_multiplier + age_difficulty
print("\nYour total difficulty is", total_difficulty)
difficulty = max_difficulty / total_difficulty
difficulty_percentage = difficulty * 100
print("%", difficulty_percentage)
