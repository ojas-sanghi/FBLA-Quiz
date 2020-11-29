import json
import random
from typing import List
import py_cui

from question import Question


data: list = []

def load_data():
    global data

    with open("questions.json", "r") as questions:
        raw_data = questions.read()
    data = json.loads(raw_data)
    

def begin_quiz():
    questions = get_questions(5)

    for q in questions:
        q.print_question()
        print(q.answer)
        while True:
            if q.is_answer_correct(get_input()):
                print("nice!\n")
                break
            else:
                print("no")
    
    print("\nGOOD JOB!!!!")

# function which returns specified number of unique questions
def get_questions(num: int) -> list:
    # list of `num` questions, returned to caller
    question_list = []

    # lists to keep track of question ids (to ensure each is unique)
    # and to keep track of question types (to ensure each question type is unique)
    ids_used = []
    types_used = []

    i = 0
    while i < num:
        new_q = get_question()

        # if we already used this question, then skip it
        if new_q.id in ids_used or new_q.type in types_used:
            continue
        # if it's a unique question, add it to the lists
        else:
            question_list.append(new_q)

            ids_used.append(new_q.id)
            types_used.append(new_q.type)

            i += 1
    
    return question_list
        

# return random question from questions lists
def get_question() -> Question:
    return Question(random.choice(data))


def get_input():
    raw_input = input("> ")
    raw_input = raw_input.strip().lower()

    return raw_input


def main():
    load_data()
    begin_quiz()

if __name__ == "__main__":
    main()    